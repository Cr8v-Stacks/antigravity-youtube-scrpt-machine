# Fact-Check Gate

## When This Gate Runs

Run this gate **after the script is written** and **before shot-by-shot image prompts begin**.

Do not skip this gate for factual, historical, science, archaeology, economics, or origin videos. It is optional for clearly opinion-based or anecdote-based content where no specific claims are made.

The gate exists because:

- Script corrections are fast and cheap.
- Shot-by-shot image prompt corrections are expensive and tedious.
- An inaccurate script that passes into shot-by-shot work locks in the error across timestamps, narration lines, and prompt copy.

---

## What To Check

Run a claim-by-claim sweep of the script. For each factual claim, check:

1. **Specificity accuracy**: Is the number, date, name, or timeline correct? Flag if an approximation is being used with false precision (e.g., "30 million years ago" when "10 million years ago" is the actual defensible event).
2. **Mechanism accuracy**: Is the causal chain correct? Flag oversimplifications that are technically false even if they feel intuitively right (e.g., "we share a blueprint with bugs" implies identical reaction, when the correct version is "overlapping receptor families produce a different but related effect").
3. **Evidence certainty**: Does the script present contested or debated evidence as confirmed fact? Flag these and add appropriate hedging language (e.g., "strong evidence of," "chemical indicators suggest," "debated but pointing toward").
4. **Context accuracy**: Is the surrounding context correct even if the core claim is accurate? A claim can be technically true but misleading because its context is stripped (e.g., Sumerian beer as a "perk" vs. a survival staple that also functioned as a labor tool).
5. **Timeline accuracy**: Are the events in the correct chronological order, and do the time gaps between them match the historical record?

---

## How To Run The Check

### Step 1: Extract All Factual Claims

Read through the script and list every claim that contains:

- A specific number, date, or duration ("30 million years ago," "6,000 years," "13,000 years ago")
- A causal mechanism ("caffeine paralyzes bugs, and we share their blueprint so it affects us")
- A historical event or artifact attributed to a real site, group, or culture ("Göbekli Tepe stone vats," "Cueva de los Murciélagos baskets")
- A scientific or biological claim ("gene ADH4 mutation," "opioid receptor," "nicotinic acetylcholine receptor")
- A behavioral or institutional claim with historical attribution ("Sumerian beer as payment/incentive")

### Step 2: Flag Each Claim By Risk Level

Assign each claim one of three risk levels:

| Risk Level | Meaning | Action |
|---|---|---|
| ✅ Verified | Widely accepted, cross-referenced, defensible | Keep as-is |
| ⚠️ Hedged | Supported but contested, or approximate | Soften language to "evidence suggests," "strong indicators," "likely," "approximately" |
| ❌ Inaccurate | Demonstrably wrong, oversimplified to the point of error, or misleading | Rewrite the claim |

### Step 3: Apply Corrections

For each ❌ or ⚠️ claim, rewrite the narration sentence using the Correction Principles below. Do not change the script's narrative structure, tone, or rhythm — only correct the claims. If a correction changes the sentence length significantly, flag this so the timestamp map can be adjusted.

### Step 4: Spot-Check The Opening

The opening 60 seconds usually carries the highest density of bold claims because it is trying to destroy viewer misconceptions fast. Check every specific claim in the first two paragraphs with extra care.

---

## Correction Principles

### Principle 1: Replace False Precision With Defensible Approximation
Instead of stating an exact number that is wrong, use the correct number or a defensible range.

- ❌ "It starts about 30 million years ago with the evolution of our mammalian receptors."
- ✅ "It starts about 10 million years ago with a specific mutation in our hominid ancestors — a gene called ADH4."

### Principle 2: Hedge Contested Evidence Without Killing The Story
Do not drop contested evidence — it is often the most interesting material. Instead, signal the uncertainty honestly.

- ❌ "Chemists found traces of fermented grain porridge."
- ✅ "Analysts found chemical residues — calcium oxalate traces that are strong indicators of fermented grain. The evidence is debated, but it points toward ritual feasting."

### Principle 3: Correct Mechanism Without Losing The Viewer
Mechanism corrections often feel complicated. Simplify to the essential truth without reverting to the original oversimplification.

- ❌ "We share basic blueprint components with bugs, so those chemicals hack us too."
- ✅ "Those same molecules accidentally hack the mammalian nervous system through overlapping receptor families. Our brains are far more complex than an insect's, so the effect is different — but the vulnerability was already there."

### Principle 4: Restore Stripped Context
When a claim is technically true but misleading because its context is removed, restore the context in a way that actually strengthens the narrative argument.

- ❌ "The elite realized controlling the beer supply was a powerful way to manage the labor force." (Strips the survival context, makes it sound like pure manipulation)
- ✅ "Sumerian beer was a thick, nutrient-dense porridge packed with B vitamins — safer to drink than the river water. Controlling that supply meant controlling survival itself." (Restores context and actually makes the control argument more compelling)

---

## Common Failure Patterns By Content Type

### History / Archaeology Scripts
- Overstating certainty of excavation evidence (use "strong indicators," "traces consistent with," "suggests")
- Collapsing broad evolutionary timelines into a single wrong date
- Attributing cultural practices to a single site when they are actually diffuse
- Confusing correlation evidence with causation in behavioral archaeology

### Science / Biology Scripts
- Mapping complex receptor biology onto insect-vs-mammal analogies that are technically false
- Using the wrong timeline for evolutionary events (gene mutations vs. receptor origin vs. species divergence)
- Presenting one model of a disputed mechanism as settled science

### Economics / Finance Scripts
- Describing ancient economies using modern economic vocabulary that did not exist as concepts
- Presenting redistribution or ration systems as modern-style markets or incentive structures
- Attributing intentionality ("the elite realized") when the evidence only shows correlation

### Technology / Energy Scripts
- Treating engineering feasibility as commercial viability
- Conflating proof-of-concept dates with deployment dates
- Misattributing inventions or first uses when the actual record is more ambiguous

---

## When A Script Passes The Gate

A script passes the fact-check gate when:

- All ❌ claims are corrected.
- All ⚠️ claims are hedged with appropriate language.
- The opening 60 seconds has been checked with extra care.
- The corrections do not break the narrative structure or create new logical gaps.
- Any timing changes caused by correction are flagged for the timestamp map.

Only after the script passes this gate should shot-by-shot image prompt work begin.

---

## Gate Output Format

After running the fact-check, report the results in this format before proceeding to shot-by-shot work:

```
## Fact-Check Gate Results

| # | Claim | Risk | Correction Applied |
|---|---|---|---|
| 1 | [original claim] | ✅ / ⚠️ / ❌ | [correction or "none needed"] |
| 2 | ... | ... | ... |

Gate: PASS / FAIL
Timing impact: [none / minor — N shots affected / significant — see notes]

Proceeding to shot-by-shot prompts.
```

If the gate fails (any ❌ remains uncorrected), stop and fix before proceeding. Do not note a failure and continue anyway.
