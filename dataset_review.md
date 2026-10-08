# Dataset review: ComfyUI/output/dataset

123 images checked: **73 keep** (11 of them need a small crop) and **50 delete**.

## Delete (50)

| File | Why |
|---|---|
| `p001_square_s1_00003_.png` | old scene test (bedroom). Good image; keep only if you want 1 real-background photo for variety |
| `p001_square_s2_00003_.png` | old scene test, same as the one above |
| `p001_square_s2_00004_.png` | near-duplicate of the other seed |
| `p002_portrait_s1_00002_.png` | old scene test, two laptops on the desk |
| `p002_portrait_s2_00001_.png` | old scene test, face drifts (heavier red lipstick) |
| `p003_square_s1_00001_.png` | near-duplicate of the other seed |
| `p004_square_s1_00001_.png` | near-duplicate of the other seed, bigger softbox in frame |
| `p005_square_s2_00001_.png` | near-duplicate of the other seed |
| `p006_square_s2_00001_.png` | near-duplicate of the other seed |
| `p007_square_s2_00001_.png` | near-duplicate of the other seed |
| `p008_square_s1_00001_.png` | bright glow artifact in her hair; came out front-facing |
| `p009_square_s1_00001_.png` | near-duplicate of the other seed |
| `p010_square_s1_00001_.png` | white light panel in frame |
| `p011_square_s2_00001_.png` | near-duplicate of the other seed |
| `p012_square_s2_00001_.png` | near-duplicate of the other seed |
| `p013_square_s2_00001_.png` | near-duplicate of the other seed |
| `p014_square_s2_00001_.png` | near-duplicate of the other seed |
| `p015_square_s1_00001_.png` | came out as a plain front view, same as p001 |
| `p016_square_s2_00001_.png` | near-duplicate of the other seed |
| `p018_square_s2_00001_.png` | near-duplicate of the other seed |
| `p020_square_s1_00001_.png` | softbox in the background |
| `p021_square_s2_00001_.png` | near-duplicate of the other seed (and of p001) |
| `p023_square_s1_00001_.png` | near-duplicate of the other seed, stiffer hands |
| `p025_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `p027_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `p028_portrait_s2_00001_.png` | near-duplicate of the other seed, softbox in frame |
| `p030_portrait_s2_00001_.png` | Apple logo on the phone |
| `p031_portrait_s1_00001_.png` | near-duplicate of the other seed |
| `p032_portrait_s1_00001_.png` | light stand at the left edge |
| `p035_portrait_s2_00001_.png` | softbox and stand in frame |
| `p037_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `p038_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `p039_portrait_s1_00001_.png` | softbox and tripod in frame |
| `p040_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `p041_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `p042_portrait_s1_00001_.png` | near-duplicate of the other seed |
| `p043_portrait_s1_00001_.png` | eyes closed and her ponytail is gone |
| `p045_portrait_s1_00001_.png` | three shoes (extra foot) |
| `p046_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `p048_portrait_s2_00001_.png` | large softbox in frame |
| `p049_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `p050_landscape_s1_00001_.png` | softbox in frame |
| `p051_landscape_s1_00001_.png` | near-duplicate of the other seed, hand touches the frame edge |
| `p052_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `p053_landscape_s1_00001_.png` | phone screen shows a second face; softbox in frame |
| `p055_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `p056_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `p058_landscape_s1_00001_.png` | on-screen content on the laptop; softbox in frame |
| `p059_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `p060_landscape_s1_00001_.png` | near-duplicate of the other seed; the other seed's heart shape is cleaner |

## Keep, but crop the edge first (11)

| File | What to crop out |
|---|---|
| `p004_square_s2_00001_.png` | softbox at right edge |
| `p008_square_s2_00001_.png` | softbox at right edge |
| `p015_square_s2_00001_.png` | ring light in top-left corner |
| `p020_square_s2_00001_.png` | faint softbox edge at right |
| `p028_portrait_s1_00001_.png` | softbox at right edge |
| `p035_portrait_s1_00001_.png` | softbox at right edge |
| `p039_portrait_s2_00001_.png` | softbox at right edge |
| `p048_portrait_s1_00001_.png` | softbox at right edge |
| `p050_landscape_s2_00001_.png` | softbox in top-left corner |
| `p053_landscape_s2_00001_.png` | softbox at right edge |
| `p058_landscape_s2_00001_.png` | softbox at right edge |

## Keep as is (62)

- `p001_square_s1_00004_.png`
- `p002_square_s1_00001_.png`
- `p002_square_s2_00001_.png`
- `p003_square_s2_00001_.png`
- `p005_square_s1_00001_.png`
- `p006_square_s1_00001_.png`
- `p007_square_s1_00001_.png`
- `p009_square_s2_00001_.png`
- `p010_square_s2_00001_.png`
- `p011_square_s1_00001_.png`
- `p012_square_s1_00001_.png`
- `p013_square_s1_00001_.png`
- `p014_square_s1_00001_.png`
- `p016_square_s1_00001_.png`
- `p017_square_s1_00001_.png`
- `p017_square_s2_00001_.png`
- `p018_square_s1_00001_.png`
- `p019_square_s1_00001_.png`
- `p019_square_s2_00001_.png`
- `p021_square_s1_00001_.png`
- `p022_square_s1_00001_.png`
- `p022_square_s2_00001_.png`
- `p023_square_s2_00001_.png`
- `p024_square_s1_00001_.png`
- `p024_square_s2_00001_.png`
- `p025_portrait_s1_00001_.png`
- `p026_portrait_s1_00001_.png`
- `p026_portrait_s2_00001_.png`
- `p027_portrait_s1_00001_.png`
- `p029_portrait_s1_00001_.png`
- `p029_portrait_s2_00001_.png`
- `p030_portrait_s1_00001_.png`
- `p031_portrait_s2_00001_.png`
- `p032_portrait_s2_00001_.png`
- `p033_portrait_s1_00001_.png`
- `p033_portrait_s2_00001_.png`
- `p034_portrait_s1_00001_.png`
- `p034_portrait_s2_00001_.png`
- `p036_portrait_s1_00001_.png`
- `p036_portrait_s2_00001_.png`
- `p037_portrait_s1_00001_.png`
- `p038_portrait_s1_00001_.png`
- `p040_portrait_s1_00001_.png`
- `p041_portrait_s1_00001_.png`
- `p042_portrait_s2_00001_.png`
- `p043_portrait_s2_00001_.png`
- `p044_portrait_s1_00001_.png`
- `p044_portrait_s2_00001_.png`
- `p045_portrait_s2_00001_.png`
- `p046_portrait_s1_00001_.png`
- `p047_portrait_s1_00001_.png`
- `p047_portrait_s2_00001_.png`
- `p049_landscape_s1_00001_.png`
- `p051_landscape_s2_00001_.png`
- `p052_landscape_s1_00001_.png`
- `p054_landscape_s1_00001_.png`
- `p054_landscape_s2_00001_.png`
- `p055_landscape_s1_00001_.png`
- `p056_landscape_s1_00001_.png`
- `p057_landscape_s1_00001_.png`
- `p059_landscape_s1_00001_.png`
- `p060_landscape_s2_00001_.png`

---

# Batch 2 review

100 images checked: **49 keep** and **51 moved to `to_delete`**.

## Keep, but crop the edge first

| File | What to crop out |
|---|---|
| `b2_p019_square_s2_00001_.png` | soft light glow at the right edge |
| `b2_p030_portrait_s2_00001_.png` | white strip at the right edge |

## Moved to to_delete (51)

| File | Why |
|---|---|
| `b2_p001_square_s1_00001_.png` | near-duplicate of the other seed; saree has no blouse |
| `b2_p002_square_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p003_square_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p004_square_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p005_square_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p006_square_s2_00001_.png` | near-duplicate of the other seed; light glow at the right edge |
| `b2_p007_square_s1_00001_.png` | near-duplicate of the other seed; stronger frown than the other seed |
| `b2_p008_square_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p009_square_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p010_square_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p011_square_s1_00001_.png` | near-duplicate of the other seed; saree has no blouse |
| `b2_p012_square_s1_00001_.png` | meant to be a shy laugh, came out as a pained grimace |
| `b2_p012_square_s2_00001_.png` | meant to be a shy laugh, came out as a pained grimace |
| `b2_p013_square_s1_00001_.png` | near-duplicate of the other seed |
| `b2_p014_square_s1_00001_.png` | near-duplicate of the other seed; ripped jacket |
| `b2_p015_square_s1_00001_.png` | near-duplicate of the other seed; frayed jacket, head not tilted back |
| `b2_p016_square_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p017_square_s1_00001_.png` | near-duplicate of the other seed; harsh orange shadows |
| `b2_p019_square_s1_00001_.png` | logo on the headphones |
| `b2_p020_square_s1_00001_.png` | near-duplicate of the other seed |
| `b2_p021_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p022_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p023_portrait_s1_00001_.png` | malformed hands |
| `b2_p023_portrait_s2_00001_.png` | malformed hands |
| `b2_p024_portrait_s2_00001_.png` | label printed on the microphone |
| `b2_p025_portrait_s2_00001_.png` | tablet looks doubled |
| `b2_p026_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p027_portrait_s1_00001_.png` | near-duplicate of the other seed; hand cut off by the frame edge |
| `b2_p028_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p029_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p030_portrait_s1_00001_.png` | near-duplicate of the other seed; eyes closed |
| `b2_p031_portrait_s1_00001_.png` | near-duplicate of the other seed |
| `b2_p032_portrait_s1_00001_.png` | near-duplicate of the other seed |
| `b2_p033_portrait_s1_00001_.png` | small tattoo on her wrist |
| `b2_p034_portrait_s2_00001_.png` | extra shoes and feet |
| `b2_p035_portrait_s1_00001_.png` | near-duplicate of the other seed |
| `b2_p036_portrait_s1_00001_.png` | near-duplicate of the other seed; feet cut off |
| `b2_p037_portrait_s2_00001_.png` | near-duplicate of the other seed; feet cut off |
| `b2_p038_portrait_s2_00001_.png` | near-duplicate of the other seed; light patch on the floor |
| `b2_p039_portrait_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p040_portrait_s2_00001_.png` | near-duplicate of the other seed; odd saree drape |
| `b2_p041_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p042_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p043_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p044_landscape_s2_00001_.png` | near-duplicate of the other seed; cable crosses her body |
| `b2_p045_landscape_s1_00001_.png` | near-duplicate of the other seed |
| `b2_p046_landscape_s1_00001_.png` | near-duplicate of the other seed |
| `b2_p047_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p048_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p049_landscape_s2_00001_.png` | near-duplicate of the other seed |
| `b2_p050_landscape_s2_00001_.png` | near-duplicate of the other seed |

## Keep (49)

- `b2_p001_square_s2_00001_.png`
- `b2_p002_square_s1_00001_.png`
- `b2_p003_square_s1_00001_.png`
- `b2_p004_square_s1_00001_.png`
- `b2_p005_square_s1_00001_.png`
- `b2_p006_square_s1_00001_.png`
- `b2_p007_square_s2_00001_.png`
- `b2_p008_square_s1_00001_.png`
- `b2_p009_square_s1_00001_.png`
- `b2_p010_square_s1_00001_.png`
- `b2_p011_square_s2_00001_.png`
- `b2_p013_square_s2_00001_.png`
- `b2_p014_square_s2_00001_.png`
- `b2_p015_square_s2_00001_.png`
- `b2_p016_square_s1_00001_.png`
- `b2_p017_square_s2_00001_.png`
- `b2_p018_square_s1_00001_.png`
- `b2_p018_square_s2_00001_.png`
- `b2_p019_square_s2_00001_.png`
- `b2_p020_square_s2_00001_.png`
- `b2_p021_portrait_s1_00001_.png`
- `b2_p022_portrait_s1_00001_.png`
- `b2_p024_portrait_s1_00001_.png`
- `b2_p025_portrait_s1_00001_.png`
- `b2_p026_portrait_s1_00001_.png`
- `b2_p027_portrait_s2_00001_.png`
- `b2_p028_portrait_s1_00001_.png`
- `b2_p029_portrait_s1_00001_.png`
- `b2_p030_portrait_s2_00001_.png`
- `b2_p031_portrait_s2_00001_.png`
- `b2_p032_portrait_s2_00001_.png`
- `b2_p033_portrait_s2_00001_.png`
- `b2_p034_portrait_s1_00001_.png`
- `b2_p035_portrait_s2_00001_.png`
- `b2_p036_portrait_s2_00001_.png`
- `b2_p037_portrait_s1_00001_.png`
- `b2_p038_portrait_s1_00001_.png`
- `b2_p039_portrait_s1_00001_.png`
- `b2_p040_portrait_s1_00001_.png`
- `b2_p041_landscape_s1_00001_.png`
- `b2_p042_landscape_s1_00001_.png`
- `b2_p043_landscape_s1_00001_.png`
- `b2_p044_landscape_s1_00001_.png`
- `b2_p045_landscape_s2_00001_.png`
- `b2_p046_landscape_s2_00001_.png`
- `b2_p047_landscape_s1_00001_.png`
- `b2_p048_landscape_s1_00001_.png`
- `b2_p049_landscape_s1_00001_.png`
- `b2_p050_landscape_s1_00001_.png`

---

# Batch 3 review

48 images checked: **44 keep** and **4 moved to `to_delete`**.

## Moved to to_delete

| File | Why |
|---|---|
| `b3_p013_square_s1_00001_.png` | face looks older and heavier in this side profile |
| `b3_p016_square_s1_00001_.png` | strong orange light changes her face |
| `b3_p027_square_s1_00001_.png` | face looks less like her (fuller, different nose) |
| `b3_p039_square_s1_00001_.png` | face looks less like her (rounder, older) |

## Keep (44)

- `b3_p001_square_s1_00001_.png`
- `b3_p002_square_s1_00001_.png`
- `b3_p003_square_s1_00001_.png`
- `b3_p004_square_s1_00001_.png`
- `b3_p005_square_s1_00001_.png`
- `b3_p006_portrait_s1_00001_.png`
- `b3_p007_portrait_s1_00001_.png`
- `b3_p008_portrait_s1_00001_.png`
- `b3_p009_portrait_s1_00001_.png`
- `b3_p010_portrait_s1_00001_.png`
- `b3_p011_landscape_s1_00001_.png`
- `b3_p012_landscape_s1_00001_.png`
- `b3_p014_square_s1_00001_.png`
- `b3_p015_square_s1_00001_.png`
- `b3_p017_square_s1_00001_.png`
- `b3_p018_portrait_s1_00001_.png`
- `b3_p019_portrait_s1_00001_.png`
- `b3_p020_portrait_s1_00001_.png`
- `b3_p021_portrait_s1_00001_.png`
- `b3_p022_portrait_s1_00001_.png`
- `b3_p023_landscape_s1_00001_.png`
- `b3_p024_landscape_s1_00001_.png`
- `b3_p025_square_s1_00001_.png`
- `b3_p026_square_s1_00001_.png`
- `b3_p028_square_s1_00001_.png`
- `b3_p029_square_s1_00001_.png`
- `b3_p030_portrait_s1_00001_.png`
- `b3_p031_portrait_s1_00001_.png`
- `b3_p032_portrait_s1_00001_.png`
- `b3_p033_portrait_s1_00001_.png`
- `b3_p034_portrait_s1_00001_.png`
- `b3_p035_landscape_s1_00001_.png`
- `b3_p036_landscape_s1_00001_.png`
- `b3_p037_square_s1_00001_.png`
- `b3_p038_square_s1_00001_.png`
- `b3_p040_square_s1_00001_.png`
- `b3_p041_square_s1_00001_.png`
- `b3_p042_portrait_s1_00001_.png`
- `b3_p043_portrait_s1_00001_.png`
- `b3_p044_portrait_s1_00001_.png`
- `b3_p045_portrait_s1_00001_.png`
- `b3_p046_portrait_s1_00001_.png`
- `b3_p047_landscape_s1_00001_.png`
- `b3_p048_landscape_s1_00001_.png`
