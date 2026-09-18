# Scoring System Motion Graphics Specification (Editor Design Guide)
**Document Version**: 1.0  
**Target Video**: EcoFlow vs Zendure vs Anker SOLIX (Plug-in Battery 6-Month Reality Check)  
**Primary Reference**: [`versus_script_v2.md`](file:///C:/Users/user/.gemini/antigravity/brain/1ed53369-7969-435e-a7b5-75222ec788e6/versus_script_v2.md)

---

## 1. Executive Summary & Design Objective
This specification defines the exact visual system, motion behavior, typography, color codes, and sound cues for the **Modular 3-Layer Scorecard Template**. 

The editor should build **one single reusable template** in Adobe After Effects, Premiere Pro Essential Graphics (MOGRT), or DaVinci Resolve Fusion. For all 7 categories, only the text labels, bar fill percentages, and badge tags are updated.

---

## 2. Canvas & Safe Layout Margins

*   **Master Resolution**: 1920 × 1080 (16:9 Full HD) or 3840 × 2160 (4K UHD)
*   **Frame Rate**: 24.00 fps or 29.97 fps (match timeline)
*   **Action / Title Safe Margin**: 10% inner margin (192px left/right, 108px top/bottom at 1080p)
*   **Scorecard Placement**:
    *   *Lower-Third Mode*: Anchored at bottom-center (Y: 780px, Width: 1400px, Height: 240px). Used when narrator or B-roll hardware fills the upper frame.
    *   *Full Split-Card Mode*: Centered on screen (Width: 1520px, Height: 680px). Used during the transition beat between categories.

---

## 3. Brand Color Palette & UI Tokens

| Token Name | HEX Code | RGB | Role / Application |
|---|---|---|---|
| **EcoFlow Blue** | `#007AFF` | `rgb(0, 122, 255)` | Bar fill, brand logo accent, EcoFlow typography |
| **Zendure Sun Gold** | `#FFB300` | `rgb(255, 179, 0)` | Bar fill, brand logo accent, Zendure typography |
| **Anker Vivid Orange** | `#FF5722` | `rgb(255, 87, 34)` | Bar fill, brand logo accent, Anker SOLIX typography |
| **Card Background** | `#0E1118` | `rgb(14, 17, 24)` | Card panel surface (set at 92% opacity with 20px blur) |
| **Card Border / Divider** | `#222836` | `rgb(34, 40, 54)` | 1.5px solid border and subtle horizontal split lines |
| **Primary Text** | `#F8FAFC` | `rgb(248, 250, 252)` | Category titles, score numbers, brand headers |
| **Muted Text / Guides** | `#8692A6` | `rgb(134, 146, 166)` | Multiplier text (`WEIGHT: ×2`), baseline grid marks |
| **Evidence Gold** | `#FFD600` | `rgb(255, 214, 0)` | Evidence badges (`🔬 LAB TESTED`, `✅ OWNER VERIFIED`) |

---

## 4. Typography Hierarchy

*   **Category Title (Header)**:
    *   *Font*: Inter Black or Montserrat ExtraBold
    *   *Style*: ALL CAPS, letter-spacing +1.5px
    *   *Size*: 26pt (at 1080p)
    *   *Color*: `#F8FAFC`
*   **Weight Multiplier Tag**:
    *   *Font*: Space Mono Bold or Roboto Mono Bold
    *   *Style*: `[WEIGHT: ×2]` in small pill container (`#1A202C` BG, `#FFD600` text)
    *   *Size*: 18pt
*   **Brand Names**:
    *   *Font*: Inter Bold or Helvetica Neue Bold
    *   *Size*: 22pt, `#FFFFFF`
*   **Score Digits (0.0 / 5.0)**:
    *   *Font*: Space Mono Bold (fixed-width prevents digit jitter during count-up)
    *   *Size*: 24pt, bold
*   **Evidence Receipts / Badges**:
    *   *Font*: Inter SemiBold
    *   *Size*: 15pt in rounded capsule pill (`border-radius: 4px`)

---

## 5. Visual Wireframe Layout

```
+---------------------------------------------------------------------------------------+
|  CATEGORY 2: APP & SOFTWARE STABILITY                        [WEIGHT: x2]             |
|  -----------------------------------------------------------------------------------  |
|                                                                                       |
|  [BLUE]   EcoFlow Stream Ultra X    [========............]   2.0 / 5   [WARNING: Bugs]|
|                                                                                       |
|  [GOLD]   Zendure Hyper 2000        [==============......]   3.5 / 5   [LOCAL: MQTT]  |
|                                                                                       |
|  [ORANGE] Anker Solarbank 2 Pro     [============........]   3.0 / 5   [LAB: Lag]     |
|                                                                                       |
+---------------------------------------------------------------------------------------+
```

---

## 6. Motion Choreography & Keyframe Timings

Total On-Screen Duration: **4.50 to 5.00 seconds**

```
Timeline (seconds):
0.0s        0.4s        0.8s        1.2s                               4.5s        4.9s
 |-- In-Slide-|
             |--- Bar Fill Wipes ---|
                         |-- Badge Pop-|
                                       |---------- HOLD ON SCREEN ----------|-- Out-Slide|
```

1.  **Card Entry (`0.00s - 0.40s`)**:
    *   Card slides up Y (+60px to 0px) and fades opacity (0% to 92%).
    *   *Easing*: Quartic Ease-Out `cubic-bezier(0.165, 0.84, 0.44, 1)`.
2.  **Bar Wipes & Number Count-up (`0.30s - 0.90s`)**:
    *   All 3 horizontal progress bars wipe left-to-right from 0% width to exact target score (e.g. 4.0 / 5 = 80% bar width).
    *   Score digits count up simultaneously from `0.0` to target number.
    *   *Easing*: Quintic Ease-Out `cubic-bezier(0.23, 1, 0.32, 1)`.
3.  **Evidence Badge Pop (`0.75s - 1.00s`)**:
    *   Evidence badge scales from 80% to 100% with subtle bounce.
4.  **Static Hold (`1.00s - 4.50s`)**:
    *   Graphic remains rock-solid while narrator speaks the category takeaway.
5.  **Exit Wipe (`4.50s - 4.90s`)**:
    *   Card slides down Y (0px to +40px) and fades out (92% to 0%).
    *   *Easing*: Quadratic Ease-In `cubic-bezier(0.55, 0.085, 0.68, 0.53)`.

---

## 7. Audio / SFX Design Cues

*   **`0.00s` (Card Pop-In)**: Sub-bass air whoosh + light tactile mechanical click (`sfx_ui_slide_in.wav`). Soft, high-pass filtered at 120Hz so it doesn't mask narration voice.
*   **`0.30s` (Bar Fill)**: Subtle data-meter shimmer or rising digital sweep (`sfx_data_meter_rise.wav`, -18 dB LUFS).
*   **`0.85s` (Score Lock-In)**: Crisp digital chime / metallic tap when the highest score locks (`sfx_score_ding.wav`, -16 dB LUFS).
*   **`4.50s` (Card Exit)**: Soft paper-snap or quick air release (`sfx_ui_slide_out.wav`).

---

## 8. Retention Directive for Editor (CRITICAL)

> [!WARNING]
> **DO NOT SHOW RUNNING CUMULATIVE TOTALS UNTIL THE VERDICT.**
> If the cumulative running score is displayed on screen after each category, viewers will see Anker pulling ahead and click off the video before reaching the 2026 flagship preview or verdict.
> Keep each category scorecard strictly isolated to its **1 to 5** score. The master 65-point calculation is only animated in the final **Verdict** scene.
