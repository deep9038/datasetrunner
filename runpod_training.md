# Training the zarixa LoRA on RunPod (FLUX.2 Klein 9B)

Dataset: `ComfyUI\output\train\` — 82 images + 82 matching `.txt` captions (also zipped as `ComfyUI\output\zarixa_train.zip`).

## Before you start (one time)

1. **Hugging Face account** at huggingface.co.
2. Open `huggingface.co/black-forest-labs/FLUX.2-klein-base-9B` while logged in and **accept the license** (the model is gated).
3. Hugging Face → Settings → Access Tokens → create a **Read** token. Keep it private.
4. **RunPod account** at runpod.io → add about **$10** credit.

## 1. Start the pod

| Setting | Value |
|---|---|
| Template | **AI Toolkit - ostris - ui - official** |
| GPU (pick one) | **RTX A6000 48 GB** (cheapest with plenty of memory, ~$0.49/hr) or **RTX 5090 32 GB** (faster, ~$0.89–0.99/hr) |
| Avoid | RTX 4090 24 GB — cheapest, but 9B barely fits and may run out of memory |
| Disk | **150 GB** (the 9B model plus its text encoder are large) |
| Password | If the template shows a password variable under *Edit Template / Environment Variables*, set your own |
| Cloud type | Community Cloud is cheaper; Secure Cloud is more reliable |

Prices are approximate (from third-party price lists, Sept–Oct 2026). Check the live price on RunPod.

## 2. Open AI-Toolkit

Pod → **Connect** → open the HTTP link for the AI-Toolkit UI (usually port **8675**). Log in with your password if you set one.

**Settings** → paste your Hugging Face token → save.

## 3. Upload the dataset

**Datasets** → **New Dataset** → name it `zarixa` → upload **all 164 files** from the `train` folder (images and `.txt` files together). If the uploader accepts a zip, `zarixa_train.zip` also works.

Check: the dataset should show 82 images, each with its caption.

## 4. Create the training job

**New Job**:

| Setting | Value | Why |
|---|---|---|
| Training name | `zarixa_9b_v1` | |
| Model architecture | **FLUX.2 Klein 9B Base** | Train on Base; the LoRA still works on the fast 4-step model you use in ComfyUI |
| Trigger word | `zarixa` | Already at the start of every caption |
| Network | LoRA, **rank 16, alpha 16** | Recommended starting point for 9B |
| Quantize model / text encoder | **On** (float8) | Strongly recommended for 9B |
| Low VRAM | Off on 48 GB; **turn on if you get "out of memory"** | |
| Steps | **2000** | Character LoRAs: 1500–3000 |
| Learning rate | **0.0001** (1e-4) | Characters: 8e-5 to 1e-4 |
| Batch size | **1** | |
| Optimizer | adamw8bit (default) | |
| Resolutions | **512, 768, 1024** | Bucketing on |
| Save every | **250 steps**, keep at least 4 | Lets you pick the best checkpoint, not just the last |
| Dataset | `zarixa` | |

**Sample prompts** (sample every 250 steps, ~50 sample steps, guidance ~4 — the Base model needs more steps than the fast model):

```
zarixa, a young Indian woman, close-up portrait, front view, soft gentle smile, pink blush and glossy pink lipstick, high ponytail with face-framing strands, wearing a white tank top, plain light grey background, soft studio lighting
zarixa, a young Indian woman, half-body shot, three-quarter view, holding a coffee cup in a sunny cafe, long soft wavy black hair, wearing a cream knit sweater, warm window light
zarixa, a young Indian woman, full-body shot, walking on a busy street in Jaipur, long loose straight black hair, wearing a mustard cotton kurti and white palazzo pants, golden hour
zarixa, a young Indian woman, close-up portrait, side profile view, natural no-makeup look, sleek high ponytail with all hair pulled back, wearing a navy blazer, plain beige background
```

The last three show things that are **not** in the dataset (real places, new combinations, no makeup). If those still look like her, the LoRA has learned her face, not just copied the training images.

## 5. Train

**Training Queue** → start the job. Watch the **Samples** tab every 250 steps.

- Early samples: she won't look like zarixa yet.
- Around 1000–1500 steps: her face should appear.
- If late samples start copying the dataset too closely (same plain backgrounds ignoring the prompt, stiff poses), an earlier checkpoint is the better one.

## 6. Download — then stop paying

1. Job → **Checkpoints** → download the **last 3–4** `.safetensors` files (for example steps 1250, 1500, 1750, 2000).
2. Put them in `ComfyUI\models\loras\`.
3. **Terminate the pod** (the trash/terminate button), not just Stop. A stopped pod still charges for its disk.

## After training

Tell Claude the checkpoints are in `ComfyUI\models\loras\`. Next step: a text-to-image workflow with the LoRA and a test sheet to choose the best checkpoint.
