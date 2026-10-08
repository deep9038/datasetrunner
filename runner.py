import copy 
import csv
import json
import random
import sys
import time
import urllib.error
import urllib.request


DRY_RUN = True
COMFY_URL = "http://127.0.0.1:8000"
WORKFLOW_FILE = "workflow_api.json"
PROMPTS_FILE = "prompts.txt"
LOG_FILE = "dataset_log.csv"
SEEDS_PER_PROMPT = 2
MAX_PENDING = 5
CHECK_EVERY = 10
PLACEHOLDER = "__PROMPT__"
SIZES = {
    "square": (1024, 1024),
    "portrait": (832, 1216),
    "landscape": (1216, 832),
}


def load_prompts(path):
    items = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "|" in line:
                size, text = line.split("|", 1)
                size, text = size.strip().lower(), text.strip()
            else:
                size, text = "square", line
            if size not in SIZES:
                print(f"  Unknown size '{size}', using square")
                size = "square"
            items.append((size, text))
    return items


def build_job(base, text, size, seed, prefix):
    wf = copy.deepcopy(base)
    w, h = SIZES[size]
    for node in wf.values():
        ctype = node["class_type"]
        inp = node["inputs"]
        if ctype == "CLIPTextEncode" and inp.get("text") == PLACEHOLDER:
            inp["text"] = text
        elif ctype == "RandomNoise":
            inp["noise_seed"] = seed
        elif ctype in ("Flux2Scheduler", "EmptyFlux2LatentImage"):
            inp["width"], inp["height"] = w, h
        elif ctype == "SaveImage":
            inp["filename_prefix"] = prefix
    return wf



def api(path, payload=None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        COMFY_URL + path, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)
def pending_count():
    q = api("/queue")
    return len(q.get("queue_running", [])) + len(q.get("queue_pending", []))

def send_job(job):
    return api("/prompt", {"prompt": job})["prompt_id"]


# ---------- Step 5: resume support ----------
def load_done():
    """Prefixes already sent in an earlier run, so they are skipped."""
    if not os.path.exists(LOG_FILE):
        return set()
    with open(LOG_FILE, encoding="utf-8") as f:
        return {row["file_prefix"] for row in csv.DictReader(f)}


# ---------- main ----------
def main():
    with open(WORKFLOW_FILE, encoding="utf-8") as f:
        base = json.load(f)
 
    if not any(
        n["class_type"] == "CLIPTextEncode" and n["inputs"].get("text") == PLACEHOLDER
        for n in base.values()
    ):
        sys.exit(f"No CLIPTextEncode with '{PLACEHOLDER}' found. Fix the prompt box and re-export.")
 
    prompts = load_prompts(PROMPTS_FILE)
    total = len(prompts) * SEEDS_PER_PROMPT
    done = set() if DRY_RUN else load_done()
    print(f"{len(prompts)} prompts x {SEEDS_PER_PROMPT} seeds = {total} images "
          f"({len(done)} already done){' [DRY RUN]' if DRY_RUN else ''}")
 
    if not DRY_RUN:
        try:
            pending_count()
        except urllib.error.URLError as e:
            sys.exit(f"Can't reach ComfyUI at {COMFY_URL} ({e}). Is it running? Check the port.")
        new_log = not os.path.exists(LOG_FILE)
        logf = open(LOG_FILE, "a", newline="", encoding="utf-8")
        log = csv.writer(logf)
        if new_log:
            log.writerow(["file_prefix", "size", "seed", "prompt"])
 
    count = 0
    for i, (size, text) in enumerate(prompts, 1):
        for s in range(1, SEEDS_PER_PROMPT + 1):
            count += 1
            prefix = f"dataset/p{i:03d}_{size}_s{s}"
            if prefix in done:
                continue
 
            seed = random.randint(1, 2**31 - 1)
            job = build_job(base, text, size, seed, prefix)

            if DRY_RUN:
                name = f"dryrun_{i:03d}_s{s}.json"
                with open(name, "w", encoding="utf-8") as f:
                    json.dump(job, f, indent=2)
                print(f"  [{count}/{total}] saved {name} ({size}, seed {seed})")
                continue

            # wait until ComfyUI's queue has room
            while pending_count() >= MAX_PENDING:
                time.sleep(CHECK_EVERY)

            send_job(job)
            log.writerow([prefix, size, seed, text])
            logf.flush()   # write immediately so a crash doesn't lose the log
            print(f"  [{count}/{total}] queued {prefix}")

    if not DRY_RUN:
        logf.close()
        print("All jobs queued. Waiting for ComfyUI to finish...")
        while pending_count() > 0:
            time.sleep(CHECK_EVERY)
        print("Done! Images are in ComfyUI/output/dataset/")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped. Run again to continue where you left off.")
