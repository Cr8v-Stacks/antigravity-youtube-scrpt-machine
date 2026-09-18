# Master B-Roll Candidate Scout & 6-Spec Design Architecture
## EcoFlow vs Zendure vs Anker SOLIX — Engineering Documentary Standard

---

## 1. Executive Summary & Design System Evolution

### The Strategic Problem This Solves
Instead of improvising one-off visual designs for every paragraph (which causes fatigue and visual inconsistency), we scout all **65 B-roll candidates** across the script and partition them into **6 Reusable Design Specs (Archetypes)**. 

### Overcoming the "Dark & Boring" Critique
The previous dark background (`#080B10`) felt flat and heavy. The new visual architecture replaces flat black with:
1. **Multi-Stop Studio Gradients**: Deep slate navy (`#0B111E` ➔ `#162032`) with soft ambient volumetric light blooms behind active elements.
2. **Subtle Technical Micro-Dot Grid**: SVG-based procedural dot matrix (opacity: 0.05) providing tactile depth and scale.
3. **Layered Glassmorphism**: Cards rendered with semi-transparent surfaces (`rgba(22, 32, 50, 0.75)`), 1px luminous edge borders (`rgba(255,255,255,0.12)`), and multi-tier drop shadows.
4. **Non-Monotonous Design Rules**: Each spec has **3 visual variations** (e.g., Centered Hero vs Split Telemetry vs Horizontal Card Grid) so the video editor never sees repeated, predictable layouts.

---

## 2. The 6 Reusable Design Specs (Archetypes)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 THE 6 DESIGN SPECS                                     │
├──────────────────────────┬──────────────────────────┬──────────────────────────────────┤
│ SPEC 1: PRODUCT_SPEC     │ SPEC 2: RATING_SCORE     │ SPEC 3: COMPARISON_SPEC          │
│ • Hardware hero cutouts  │ • 3-layer scorecards     │ • Side-by-side versus splits     │
│ • Spec pill callouts     │ • Review star cards      │ • Software vs Hardware balance   │
│ • Exploded CAD views     │ • 65-point scoreboard    │ • Buyer persona 3-way match      │
├──────────────────────────┼──────────────────────────┼──────────────────────────────────┤
│ SPEC 4: METRIC_TELEMETRY │ SPEC 5: QUOTE_RECEIPT    │ SPEC 6: STATEMENT_SPEC           │
│ • Live decibel VU needle │ • Reddit dark-mode cards │ • Kinetic typography hooks       │
│ • 12°C freezing gauge    │ • Scorched connector     │ • Stat punches (£1,000+)         │
│ • Tariff price waveform  │ • Fuse box alert popups  │ • Asterisk stamp reality         │
└──────────────────────────┴──────────────────────────┴──────────────────────────────────┘
```

---

### SPEC 1: `PRODUCT_SPEC` (Hardware & Architecture)
* **Purpose**: Showcase physical hardware, internal engineering, modularity, and specs.
* **Core Visual Ingredients**:
  * Clean, high-resolution isolated product cutouts (`product_images/`).
  * 3 floating technical callout pills with monospace data (`3.84 kWh`, `4× MPPT`, `38.8 kg`).
  * Pedestal floor glow matched to brand color (EcoFlow `#007AFF`, Zendure `#FFB300`, Anker `#FF5722`).
  * Subtle 3D perspective tilt (3°–5°) with spring damping on entrance.
* **3 Layout Variations**:
  1. *Hero Centered*: Solitary product centered with orbiting technical spec callouts.
  2. *Exploded Blueprint*: 3D CAD schematic with leader lines pointing to microinverter and battery cells.
  3. *Modular Stacking*: Vertical assembly motion showing battery packs clicking together.
* **Remotion Component Base**: `<ProductSpecCard brand="ecoflow" layout="hero" />`

---

### SPEC 2: `RATING_SCORE_SPEC` (Scoreboards & Review Metrics)
* **Purpose**: Display objective category scores, customer review ratings, and the final scoreboard.
* **Core Visual Ingredients**:
  * Category title header with weight multiplier badge (`WEIGHT: ×1`, `×2`, or `×3`).
  * 3 simultaneous horizontal progress tracks filling smoothly from 0 to score out of 5.
  * Per-brand distinct color coding:
    * 🔵 EcoFlow: Electric Blue (`#007AFF`)
    * 🟡 Zendure: Sun Gold (`#FFB300`)
    * 🔴 Anker: Vivid Red-Orange (`#FF5722`)
  * Right-aligned receipt badge (`[🔬 55% Cold Drop]`, `[✅ Local MQTT]`).
* **3 Layout Variations**:
  1. *Standard 3-Bar Split*: Centered vertical stack of the 3 contender scores.
  2. *Trustpilot Star Profile*: 5-star rating card with verified consumer quote and rating badge.
  3. *Master Totalizer*: 65-point celebration scoreboard with animated numerical counters.
* **Remotion Component Base**: `<ScoreboardSpec category="Category 1" scores={...} />`

---

### SPEC 3: `COMPARISON_SPEC` (Versus, Splits & Paradoxes)
* **Purpose**: Clarify trade-offs, legal realities, and philosophical contrasts.
* **Core Visual Ingredients**:
  * 50/50 split-screen or dual floating glass cards.
  * Contrast indicators (e.g. `[OTA PATCH: CLEAN FIX ✅]` vs `[PHYSICAL RECALL: COSTLY ❌]`).
  * Glowing neon center divider with subtle animated electrical particle seam.
* **3 Layout Variations**:
  1. *Dual Contrast Split*: Left vs Right card comparison with opposing status badges.
  2. *3-Way Tri-Split*: 3 vertical pillars introducing the three brands.
  3. *Persona Match*: 3 cards highlighting the 3 buyer personas (Power Maximizer / Privacy / Everyday).
* **Remotion Component Base**: `<ComparisonSpec leftCard={...} rightCard={...} />`

---

### SPEC 4: `METRIC_TELEMETRY_SPEC` (Live Dynamic Gauges)
* **Purpose**: Make laboratory data points and invisible electrical measurements visually exciting.
* **Core Visual Ingredients**:
  * Live animated instrument gauges (VU meter needle, mercury thermometer tube, dynamic graph).
  * Big bold monospace numbers with unit labels (`39.1 dBA`, `12°C`, `13.2% LOSS`).
  * Color threshold shifts: green in safe zone ➔ amber in caution ➔ crimson in danger zone.
  * Verification stamp (`🔬 INDEPENDENTLY TESTED`).
* **3 Layout Variations**:
  1. *Acoustic Needle Gauge*: Semi-circular VU meter with needle swing and sound wave concentric rings.
  2. *Thermal Thermometer*: Vertical glass tube with mercury drop and frost crystallizing on borders.
  3. *Dynamic Tariff Waveform*: 24-hour electricity price curve showing cheap night charge vs peak discharge.
* **Remotion Component Base**: `<MetricTelemetrySpec type="decibel" value={39.1} />`

---

### SPEC 5: `QUOTE_RECEIPT_SPEC` (Forensic Community Proof)
* **Purpose**: Prove claims with authentic receipts from Reddit, Trustpilot, forums, and test reports.
* **Core Visual Ingredients**:
  * High-fidelity dark-mode card with authentic UI header (subreddit icon, username, timestamp).
  * Glowing yellow/gold forensic highlighter line drawing over the critical spoken sentence.
  * Evidence badge: `[✅ OWNER VERIFIED]`.
  * Forensic zoom/crop focusing viewer attention on the exact receipt text.
* **3 Layout Variations**:
  1. *Reddit Dark Mode Post*: Floating forum card with timestamp `02:15 AM` and highlighted quote.
  2. *Forensic Hardware Defect*: Charred connector photo with thermal circular target ring overlay.
  3. *System Error Modal*: Terminal warning dialog (`ERR_SMART_METER_OFFLINE`).
* **Remotion Component Base**: `<QuoteReceiptSpec source="reddit" quote="..." />`

---

### SPEC 6: `STATEMENT_SPEC` (Kinetic Typography & Thesis Hooks)
* **Purpose**: Slam home key insights, thesis paradoxes, and big statistical punches.
* **Core Visual Ingredients**:
  * Large, bold editorial typography (72pt–104pt) with varied font weights.
  * High-impact keyword color highlighting (Yellow / Crimson / Emerald).
  * Spring-driven staggered word entrance (2–3 frames offset per word).
  * Subtle camera dolly/push forward for continuous forward momentum.
* **3 Layout Variations**:
  1. *Giant Stat Punch*: Enormous numbers (`£1,000+`, `38.8 kg`, `80 kg`) with supporting descriptor.
  2. *Asterisk Reality Stamp*: Words appear, then a massive red asterisk `*` slams down with screen shake.
  3. *Thesis Statement*: Multi-line kinetic sentence revealing the core video message.
* **Remotion Component Base**: `<StatementSpec headline="..." subhead="..." />`

---

## 3. Scouted Candidate Master Map (65 B-Roll Moments)

Every candidate is indexed with its **first 6 words**, exact cue phrase, and mapped to its reusable **Design Spec**.

| # | First 6 Words of Paragraph | Cue Phrase / Spoken Sentence | Designated Spec Type | Visual Layout Treatment |
|---|---|---|---|---|
| **01** | `Before you spend over £1,000 on` | `"over £1,000 on a plug-in battery"` | **SPEC 6: STATEMENT** | Stat Punch: `£1,000+` counter + Anker unibody stack |
| **02** | `Before you spend over £1,000 on` | `"serious problem with the way these systems"` | **SPEC 6: STATEMENT** | Kinetic Hook: `THE HONEYMOON ILLUSION` |
| **03** | `Whether you call it balcony solar` | `"balcony solar, plug-in solar, or Balkonkraftwerk"` | **SPEC 3: COMPARISON** | 3 Cycling Taxonomy Pills with country standards |
| **04** | `Whether you call it balcony solar` | `"free daytime energy stored in a plug-in battery"` | **SPEC 4: METRIC/TELEMETRY** | Day/Night Circuit Flow: Sun ➔ Battery ➔ Home |
| **05** | `Almost every comparison online shows you` | `"brand new box, a clean balcony, celebrating"` | **SPEC 3: COMPARISON** | Unboxing Honeymoon Card vs 6 Months Later |
| **06** | `Almost every comparison online shows you` | `"reading what real owners post at 2:00 AM"` | **SPEC 5: QUOTE_RECEIPT** | Reddit Dark Mode: `02:14 AM` issue megathread |
| **07** | `You find frozen companion apps, unexpected` | `"frozen companion apps, unexpected circuit breaker"`| **SPEC 5: QUOTE_RECEIPT** | 4-Quadrant System Alert Grid (Tiles 1 & 2) |
| **08** | `You find frozen companion apps, unexpected` | `"locked down by local regulations... lose half eff"`| **SPEC 5: QUOTE_RECEIPT** | 4-Quadrant System Alert Grid (Tiles 3 & 4) |
| **09** | `We investigated the 3 dominant brands` | `"EcoFlow, Zendure, and Anker SOLIX"` | **SPEC 3: COMPARISON** | 3-Pillar Brand Hero Card (Blue / Gold / Red) |
| **10** | `We investigated the 3 dominant brands` | `"tagged by its proof: owner-verified, lab, claims"` | **SPEC 2: RATING_SCORE** | Proof System Key: The 4 Badges Reveal |
| **11** | `Three storage systems represent the bulk` | `"Three storage systems represent the bulk"` | **SPEC 1: PRODUCT_SPEC** | Contenders Digital Plinths Showcase |
| **12** | `EcoFlow brings the Stream Ultra X` | `"Stream Ultra X, expandable 3.84 kWh, 4 inputs"` | **SPEC 1: PRODUCT_SPEC** | Hero Centered: 4 MPPT glowing blue inputs |
| **13** | `Zendure is represented by the Hyper` | `"Hyper 2000 hybrid inverter and SolarFlow 2400"` | **SPEC 1: PRODUCT_SPEC** | Modular Stacking: Inverter clicks to AB2000X |
| **14** | `Anker SOLIX competes with the Solarbank` | `"Solarbank 2 Pro, widely recommended for beginners"`| **SPEC 1: PRODUCT_SPEC** | Exploded CAD View: Internal LFP & Inverter |
| **15** | `All 3 manufacturers print the words` | `"plug-and-play" on packaging... asterisks` | **SPEC 6: STATEMENT** | Asterisk Stamp: `"PLUG & PLAY"` + Red `*` Slam |
| **16** | `Consider EcoFlow. The Stream Ultra X` | `"Stream Ultra X weighs 38.8 kg... two people"` | **SPEC 4: METRIC/TELEMETRY** | Industrial Load Cell Scale: 0 ➔ 38.8 kg |
| **17** | `Consider EcoFlow. The Stream Ultra X` | `"hardwired connection... electrician... G98/G99"` | **SPEC 5: QUOTE_RECEIPT** | Regulatory Notice & Blueprint Wiring Route |
| **18** | `Zendure's Hyper 2000 comes closest` | `"solar panels connect directly... modular packs"` | **SPEC 1: PRODUCT_SPEC** | Snap-Lock DC Bus & Zero Cable Wiring |
| **19** | `Anker's Solarbank 2 Pro also earns` | `"Smart Meter inside fuse box... fail entirely"` | **SPEC 5: QUOTE_RECEIPT** | DIN-Rail Fuse Box Alert: `ERR_NO_COMMS` |
| **20** | `All 3 systems involve real installation` | `"friction: weight, legal certification, or meters"`| **SPEC 3: COMPARISON** | 3-Column Friction Matrix |
| **21** | `Category 1 Scores: Setup and Installation` | Category 1 Scorecard Reveal (3.0, 4.0, 4.0) | **SPEC 2: RATING_SCORE** | Standard 3-Bar Scoreboard (Weight ×2) |
| **22** | `This category generated the highest volume` | `"companion app is how you interact every day"` | **SPEC 6: STATEMENT** | Mobile Screen Floating Dashboard |
| **23** | `Before looking at specific quirks, there` | `"software glitches: OTA patch vs hardware recall"` | **SPEC 3: COMPARISON** | Dual Contrast Split: Code Patch vs Recall Box |
| **24** | `That said, here is the shared` | `"automation logic through remote cloud servers"` | **SPEC 3: COMPARISON** | Cloud Network Outage Diagram |
| **25** | `EcoFlow provides one of the most` | `"app displaying yellow solar in middle of night"` | **SPEC 5: QUOTE_RECEIPT** | Reddit Card: 340W Solar at 2:15 AM Bug |
| **26** | `EcoFlow provides one of the most` | `"advanced tariff tools: optional €4 subscription"` | **SPEC 5: QUOTE_RECEIPT** | Glass Paywall Card: €3.99/mo Lock |
| **27** | `Zendure offers the most capable local` | `"MQTT, local HTTP API, native Home Assistant"` | **SPEC 4: METRIC/TELEMETRY** | Local LAN Terminal: 1.0s Polling Rate |
| **28** | `Zendure offers the most capable local` | `"firmware updates caused data sync freezes"` | **SPEC 5: QUOTE_RECEIPT** | Forum Thread: Wi-Fi Drop / Reset Cue |
| **29** | `Anker's SOLIX app delivers the cleanest` | `"cloud latency: 1-2s delay... solar slips unpaid"` | **SPEC 4: METRIC/TELEMETRY** | Latency Stopwatch: 2.4s Grid Leakage |
| **30** | `Category 2 Scores: App and Software` | Category 2 Scorecard Reveal (2.0, 3.5, 3.0) | **SPEC 2: RATING_SCORE** | Standard 3-Bar Scoreboard (Weight ×2) |
| **31** | `Marketing brochures claim maximum efficiency numbers`| `"efficiency numbers recorded under room temp"` | **SPEC 6: STATEMENT** | Lab Room Temp vs Real Balcony Weather |
| **32** | `Independent lab evaluations of the EcoFlow` | `"efficiency plummets to 55% around 12°C"` | **SPEC 4: METRIC/TELEMETRY** | Thermal Thermometer: 12°C & 55.4% Freeze |
| **33** | `Independent lab evaluations of the EcoFlow` | `"smartphone battery drops from 40% to dead"` | **SPEC 3: COMPARISON** | Phone Battery in Snow Anchor Visual |
| **34** | `Zendure achieved an impressive 87%` | `"87% efficiency vs 39 dB measured noise (25 spec)"`| **SPEC 4: METRIC/TELEMETRY** | VU Decibel Needle Jump: 25 dB ➔ 39.1 dB |
| **35** | `Anker's Solarbank was measured by` | `"approximate 13% energy loss during AC charging"` | **SPEC 4: METRIC/TELEMETRY** | Stacked Energy Waterfall: 86.8% Stored / 13.2% Loss |
| **36** | `Across all 3 brands, modern lithium` | `"LFP chemistry durable... firmware is the cause"` | **SPEC 6: STATEMENT** | LFP 6,000 Cycle Graph vs Firmware Bug |
| **37** | `Category 3 Scores: Lab Performance Over` | Category 3 Scoreboard Reveal (3.0, 4.0, 3.5) | **SPEC 2: RATING_SCORE** | Standard 3-Bar Scoreboard (Weight ×2) |
| **38** | `All 3 systems carry an IP65` | `"IP65 ingress protection: driving rain and dust"` | **SPEC 1: PRODUCT_SPEC** | 3 Enclosures with Water Bead Physics |
| **39** | `EcoFlow uses heavy-gauge aluminum enclosures` | `"integrated heaters allow operation down to -20°C"` | **SPEC 1: PRODUCT_SPEC** | Aluminum Shell Cutaway with Internal Heaters |
| **40** | `Zendure's metal casing feels premium and` | `"MC4 connectors overheating and melting under load"`| **SPEC 5: QUOTE_RECEIPT** | Forensic Card: Scorched Connector & Warning |
| **41** | `Anker's Solarbank 2 Pro earns the` | `"die-cast aluminum dissipates heat without fans"` | **SPEC 1: PRODUCT_SPEC** | Die-Cast Heatsink Thermal Flow |
| **42** | `A crucial rule shared by owners` | `"IP65 protects moisture, not direct baking sun"` | **SPEC 6: STATEMENT** | Solar Flare Warning: >50°C Thermal Throttle |
| **43** | `Category 4 Scores: Build Quality and` | Category 4 Scorecard Reveal (4.0, 3.5, 4.5) | **SPEC 2: RATING_SCORE** | Standard 3-Bar Scoreboard (Weight ×1) |
| **44** | `Does installing one of these systems` | `"Does installing one actually save you money?"` | **SPEC 6: STATEMENT** | Payback Question Card: Hype vs Math |
| **45** | `EcoFlow owners utilizing dynamic, time-of-use` | `"Octopus dynamic tariffs... £600-£900/yr... 2 yrs"` | **SPEC 4: METRIC/TELEMETRY** | Dynamic Price Waveform: Arbitrage Savings |
| **46** | `EcoFlow owners utilizing dynamic, time-of-use` | `"discontinued PowerStream... ecosystem risk"` | **SPEC 3: COMPARISON** | Obsolescence Card: Slashed Compatibility Line |
| **47** | `Zendure owners who possess technical programming` | `"local MQTT automations maximize self-consumption"` | **SPEC 4: METRIC/TELEMETRY** | Home Electrical Baseline 365-Day Graph |
| **48** | `Anker owners report a longer financial` | `"longer payback horizon, typically 4.5 to 6 years"`| **SPEC 4: METRIC/TELEMETRY** | Payback Timeline Bar: 2.1 yrs vs 5.2 yrs |
| **49** | `Category 5 Scores: Value and Payback` | Category 5 Scorecard Reveal (3.5, 3.5, 3.0) | **SPEC 2: RATING_SCORE** | Standard 3-Bar Scoreboard (Weight ×1) |
| **50** | `When high-voltage electronics malfunction, customer service`| `"working power system or expensive paperweight"` | **SPEC 6: STATEMENT** | Kinetic Warning: Support Stakes |
| **51** | `EcoFlow exhibits a distinct split in` | `"hardware DOA (days) vs software tickets (weeks)"` | **SPEC 3: COMPARISON** | Support Split: Fast Courier vs 14-Day Calendar |
| **52** | `EcoFlow exhibits a distinct split in` | `"monthly product issues thread for stalled tickets"`| **SPEC 5: QUOTE_RECEIPT** | Reddit Megathread Verified Card |
| **53** | `Zendure support is highly unpredictable. Some` | `"ignored by chatbots vs dev forum rapid fixes"` | **SPEC 3: COMPARISON** | Chatbot 12 Days vs Dev Forum 24 Hours |
| **54** | `Anker holds the cleanest customer service` | `"4.3 Trustpilot rating... 30 kg hazmat freight"` | **SPEC 2: RATING_SCORE** | Trustpilot Verified Star Profile (4.3 / 5) |
| **55** | `Category 6 Scores: Customer Support Response` | Category 6 Scorecard Reveal (2.0, 2.5, 3.5) | **SPEC 2: RATING_SCORE** | Standard 3-Bar Scoreboard (Weight ×2) |
| **56** | `This is the most critical category` | `"Safety track record carries triple weight (×3)"` | **SPEC 6: STATEMENT** | Triple Weight Badge (×3) Warning Flare |
| **57** | `EcoFlow has issued formal product recalls` | `"DELTA Max recall 2025 vs Balcony Stream 0 fires"` | **SPEC 3: COMPARISON** | Disambiguation Shield: Camping vs Balcony |
| **58** | `Zendure faces a confirmed hardware vulnerability` | `"melted MC4 connectors... space heater plug"` | **SPEC 5: QUOTE_RECEIPT** | Forensic Zoom: Forum Post + Scorched Cable |
| **59** | `Anker SOLIX maintains an unblemished safety` | `"phone charger 1M recall vs clean LFP Solarbank"` | **SPEC 3: COMPARISON** | Chemical Molecular LFP Stability Lock |
| **60** | `Category 7 Scores: Safety Track Record` | Category 7 Scorecard Reveal (12, 9, 15 / 15) | **SPEC 2: RATING_SCORE** | Standard 3-Bar Scoreboard (Weight ×3) |
| **61** | `Anker launched the SOLIX Solarbank 4` | `"Solarbank 4 E5000 Pro: 5 kWh, IP66, Local HA"` | **SPEC 1: PRODUCT_SPEC** | Flagship Showcase Card: IP66 Coastal Seal |
| **62** | `Zendure released the SolarFlow 4000 Mix` | `"SolarFlow 4000 Mix Pro: 8-50 kWh, 80 kg monster"`| **SPEC 1: PRODUCT_SPEC** | Monster Spec: 80 kg Hand Truck Alert |
| **63** | `EcoFlow announced the Stream 5000 In` | `"Stream 5000: 5,000W solar input, pre-order"` | **SPEC 1: PRODUCT_SPEC** | Unreleased Pre-order Warning (❓ Not Enough Data) |
| **64** | `Here is the final weighted scoreboard` | Final 65-Point Total Scoreboard Reveal | **SPEC 2: RATING_SCORE** | Master Scoreboard (39.5, 44.0, 51.0 / 65) |
| **65** | `The reason this entire product category` | `"Substation hardware with smartphone software"` | **SPEC 3: COMPARISON** | Paradox Merge: 10,000V Substation vs Smartphone |
