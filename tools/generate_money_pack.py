from pathlib import Path
import textwrap

OUT = Path("production-packs/what-did-ancient-humans-do-before-money.md")
STYLE = "Hybrid Sketch System Map, ancient/system-map identity"

SCRIPT = """This clay tablet was doing a money job before coins were even in the room.

That is the first crack in the story most of us were given.

The usual answer is simple: before money, people bartered. A farmer had grain. A potter had bowls. They swapped, everyone went home, and eventually someone invented coins because swapping was annoying.

But that story only works if everyone is a stranger, everyone needs the opposite thing at the same moment, and nobody remembers anything after the trade.

That is not how small human groups work.

Before money, many exchanges did not look like purchases. They looked like obligations. A hunter shared meat. A neighbor helped repair a roof. A family gave grain during a hard season. Nobody pulled out a price list. But nobody forgot either.

The payment system was memory.

And memory had teeth.

If you kept taking and never gave back, people noticed. They stopped helping you. They talked. Your reputation shrank. In a small community, that could be more dangerous than an unpaid bill, because survival was not private. Food, marriage, labor, protection, and trust were social.

So before money, humans used relationships. They used gifts that were not exactly free. They used favors, feasts, promises, kinship, ritual valuables, cattle, grain, shells, beads, metal, and eventually records.

The better question is not, "What object replaced cash?" The better question is, "How did people stop a promise from disappearing?"

Start with the smallest scale.

In a band or village where people know one another, direct barter is not the main tool. If your cousin helps you today, you may help their family later. If someone shares meat after a hunt, the return may come as labor, protection, marriage alliance, or future food. The exchange is not clean, but it is legible because the group remembers the relationship.

Wealth, in that world, is not just owning things. Wealth is being surrounded by people who owe you, trust you, fear disappointing you, or depend on you.

A person with cattle may be wealthy. A person with stored grain may be wealthy. A person with shells used in ceremonies may be wealthy. But so is the person who can call twenty relatives to build a house, defend a boundary, arrange a marriage, or organize a feast.

That is why gift systems can look generous and competitive at the same time. Giving creates honor. Giving creates obligation. A feast can feed the community, but it can also announce, "I have enough surplus to make other people remember me."

Now the conflict appears.

What happens when someone refuses to return the favor? What happens when the helper dies? What happens when two families remember the debt differently?

Before formal money, many conflicts were handled by reputation, elders, witnesses, compensation customs, oath-taking, public shame, or negotiated settlement. The point was not always to find the exact market price. The point was to restore a relationship, prevent revenge, or mark that a debt had been recognized.

But those systems weaken at the edges.

If you meet a stranger from another village, memory cannot do as much. You may never see them again. Their uncle does not know your uncle. Their reputation does not travel far enough to protect you.

That is where direct barter becomes more useful. It is also where portable valuables matter.

A shell, a bead, a metal weight, a piece of cloth, a cattle head, a salt block, or a measured quantity of grain can move between people who do not fully trust each other. These things are not always money in the modern sense, but they can do some of money's jobs: store value, signal status, settle claims, or make comparison easier.

Different societies used different objects because value depends on the local problem. Cattle are visible wealth, but hard to divide. Grain feeds people, but spoils and needs storage. Shells can be durable and countable, but only if the supply is controlled enough to keep them special. Metal can be weighed, melted, and moved, but someone must trust the weight and purity.

Then population changes the whole machine.

When communities grow into towns and cities, memory becomes overloaded. You cannot know every debt, every promise, every household, every worker, every trader, and every stranger passing through the gate.

At that scale, institutions start to matter.

In ancient Mesopotamia, temples and palaces collected goods, stored grain, assigned labor, paid rations, and recorded obligations. Clay tablets could remember what a person could not. Barley could be used for everyday payments. Silver could serve as a unit of account for larger value. The breakthrough is not that everyone walked around with coins. The breakthrough is that value became measurable across people who did not personally know each other.

That is a major leap.

A promise written down can outlive a conversation. A measured weight can travel farther than a reputation. A witness mark can turn an argument into evidence. A standard unit can let two people compare grain, labor, animals, land, and debt without renegotiating the entire universe every time.

But it also makes conflict sharper.

Once value is measured, debt can be enforced. Once debt is recorded, it can accumulate. Once records belong to powerful institutions, the person holding the tablet may have more power than the person holding the memory.

Money did not simply remove conflict. It changed the battlefield.

Coins came later as one solution to a specific problem: how do you make metal value portable, recognizable, and trusted without weighing and testing every piece? A stamped coin says, in effect, "Someone with authority stands behind this object."

That is why money is not just a thing. It is a social agreement wearing a physical disguise.

Cowrie shells, silver weights, cattle, grain measures, clay tablets, and coins are very different objects. But they all answer versions of the same human problem: how do we remember value when trust is thin, groups are large, and conflict is possible?

So what did ancient humans do before money?

They did not live in one giant barter market.

They shared, owed, gifted, stored, counted, witnessed, punished, negotiated, displayed wealth, and converted trust into objects when memory was no longer enough.

And that is the part that still has not disappeared.

A payment app looks nothing like a clay tablet. But it still works because a record says who owes whom, a system decides whether the transfer counts, and a dispute process exists when people disagree.

The oldest money was not a coin.

It was a remembered obligation.

The coin only arrived when the memory became too heavy to carry."""

SHOT_BEATS = [
    ("This clay tablet was doing a money job", "clay tablet with wedge marks, grain measure, and absent coin clue", "close-up proof object", "mystery tension"),
    ("first crack in the story", "barter myth diagram cracking beside tablet evidence", "split correction panel", "curious doubt"),
    ("before money, people bartered", "farmer grain and potter bowls connected by a too-neat swap arrow", "simple myth diagram", "skeptical mood"),
    ("farmer had grain, potter had bowls", "barley bundle, clay bowls, farmer hut, and potter kiln", "side-by-side role scene", "practical tension"),
    ("they swapped, everyone went home", "two figures walking away from a fading swap arrow", "two-panel action strip", "uneasy simplicity"),
    ("only works if everyone is a stranger", "two unknown traders at a boundary line with no witness marks", "medium boundary scene", "wary pressure"),
    ("opposite thing at the same moment", "grain, fish, pottery, and tool needs failing to align", "triangle need map", "frustrated tension"),
    ("nobody remembers anything after the trade", "obligation marks fading from a village memory web", "overhead erasure scene", "fragile trust"),
    ("small human groups work differently", "settlement fire circle with relationship arrows among huts", "wide community map", "warm social pressure"),
    ("exchanges did not look like purchases", "roof repair help replacing a crossed-out price tag", "split comparison", "calm correction"),
    ("they looked like obligations", "hands passing grain with an owed-later arrow", "foreground hand scene", "quiet pressure"),
    ("a hunter shared meat", "hunter distributing portions near a fire while families watch", "medium camp scene", "survival urgency"),
    ("neighbor helped repair a roof", "two figures tying reed thatch with future-return mark", "work scene", "cooperative tension"),
    ("family gave grain during a hard season", "grain sack passed between worried households under dry sun mark", "seasonal hardship scene", "empathetic anxiety"),
    ("nobody pulled out a price list", "price list crossed out while witness faces remember the exchange", "symbolic correction card", "serious accountability"),
    ("payment system was memory", "human memory web filled with goods, names, and favor arrows", "central diagram", "reflective tension"),
    ("memory had teeth", "isolated taker outside the fire circle as help arrows withdraw", "social consequence scene", "warning mood"),
    ("kept taking and never gave back", "one household receiving repeated food and labor while watchers grow skeptical", "storyboard strip", "rising pressure"),
    ("they stopped helping you", "neighbors redirect assistance arrows away from an unreliable household", "overhead settlement map", "cold exclusion"),
    ("survival was not private", "food, labor, marriage, protection, and trust ropes linking huts", "wide systems map", "serious dependence"),
    ("humans used relationships", "relationship web replacing a pile of crossed-out coins", "myth-busting diagram", "thoughtful insight"),
    ("gifts were not exactly free", "gift basket with hidden obligation arrow curling back", "medium exchange scene", "generous unease"),
    ("favors, feasts, promises, kinship", "constellation of feast bowl, kinship cord, shell, cattle, grain, metal, tablet", "object constellation", "discovery mood"),
    ("stop a promise from disappearing", "spoken promise fading as a hand presses it into clay", "transition close-up", "urgent memory pressure"),
    ("where people know one another", "compact village where relationship arrows outnumber barter arrows", "overhead village map", "familiar trust"),
    ("cousin helps today", "two related households linked by roof repair now and grain later", "two-stage map", "patient obligation"),
    ("return may come as labor or protection", "labor, boundary defense, marriage cord, and future food branching from one gift", "four-panel grid", "social complexity"),
    ("exchange is not clean but legible", "messy obligation web made readable by witness dots", "diagram scene", "careful clarity"),
    ("wealth is not just owning things", "object wealth pile beside a larger network of people obligations", "split wealth comparison", "belief-shift tension"),
    ("surrounded by people who owe you", "central giver surrounded by owe, trust, dependence, and disappointment arrows", "status network", "tense prestige"),
    ("cattle and stored grain", "cattle enclosure and sealed grain baskets beside owner figures", "paired object portrait", "grounded wealth"),
    ("shells used in ceremonies", "shell string passing during ritual exchange with witnesses", "ceremonial close scene", "formal status"),
    ("call twenty relatives", "organizer activating relatives for house, boundary, marriage, and feast", "social power map", "mobilized pressure"),
    ("gift systems look generous and competitive", "feast giver gaining status ladder behind food bowls", "social feast scene", "competitive warmth"),
    ("giving creates honor and obligation", "basket branching into honor arrow and obligation arrow", "symbolic diagram", "uneasy insight"),
    ("surplus makes people remember me", "overflowing feast pot sending memory lines to guests", "wide feast map", "confident pressure"),
    ("conflict appears", "red rupture mark cutting a calm obligation web", "system shock card", "urgent conflict"),
    ("refuses to return the favor", "accused figure holding back grain while old help arrows point at them", "medium dispute scene", "tense refusal"),
    ("helper dies", "faded helper node leaving unresolved arrows between families", "somber memory map", "fragile uncertainty"),
    ("families remember debt differently", "two households showing mismatched memory counts for one basket", "split dispute panel", "argument pressure"),
    ("reputation, elders, witnesses", "elder circle with witness marks, oath hand, compensation grain", "community mediation scene", "civic tension"),
    ("restore relationship or prevent revenge", "broken household arrow repaired by compensation knot", "settlement repair diagram", "fragile peace"),
    ("systems weaken at the edges", "village trust web fading near boundary river", "wide boundary map", "cautious transition"),
    ("stranger from another village", "traveler outside the fire-circle trust bubble", "gate scene", "wary distance"),
    ("may never see them again", "footprints leaving along route as return arrow fades", "route map", "anxious risk"),
    ("barter becomes more useful", "strangers making immediate exchange at boundary with shell bundle nearby", "boundary exchange", "practical caution"),
    ("portable valuables matter", "shells, beads, metal weight, grain measure traveling between settlements", "object route map", "trust-thin tension"),
    ("some money jobs", "cowrie shell surrounded by store value, status, settle claim, compare goods", "function diagram", "thoughtful distinction"),
    ("value depends on local problem", "regions matched to cattle, shells, grain, metal, and beads", "comparative map", "curious analysis"),
    ("cattle hard to divide", "cattle enclosure with awkward division mark and small-payment problem", "tradeoff scene", "practical awkwardness"),
    ("grain spoils and needs storage", "barley baskets, damp spoilage corner, hungry household marks", "storehouse close scene", "anxious practicality"),
    ("shells durable and countable", "cowrie string counted beside distant source route", "object-and-map frame", "scarcity tension"),
    ("metal trust weight and purity", "hands weighing silver fragment with suspicious eyes nearby", "verification scene", "serious trust"),
    ("population changes the machine", "village web expanding into dense town nodes", "growth timeline", "rising pressure"),
    ("towns overload memory", "elder overwhelmed by too many household strings", "medium overload scene", "anxious scale"),
    ("cannot know every debt", "workers, traders, households, strangers entering town gate with stacked arrows", "wide gate scene", "confused pressure"),
    ("institutions start to matter", "temple storehouse becoming larger node between many households", "institution map", "administrative tension"),
    ("Mesopotamia temples and palaces", "barley sacks entering temple storehouse, ration bowls leaving, scribe recording", "process scene", "controlled pressure"),
    ("collected goods and stored grain", "grain jars stacked in institutional storehouse with intake arrows", "interior storehouse", "organized weight"),
    ("assigned labor and paid rations", "workers receiving measured barley bowls while scribe records marks", "ration distribution", "practical payment"),
    ("recorded obligations", "scribe pressing reed stylus into clay beside debtor and witness figures", "record close-up", "evidence tension"),
    ("tablets remember what people could not", "overwhelmed memory web condensing into clear tablet marks", "memory-to-record diagram", "breakthrough mood"),
    ("barley everyday payments", "barley measure labeled food and payment beside worker household", "object explanation", "careful clarity"),
    ("silver unit of account", "silver weight mark comparing cattle, grain, labor, and debt", "comparison diagram", "abstract value tension"),
    ("not everyone carried coins", "crossed-out coin pouch beside tablet-measure network", "myth correction split", "nuanced pressure"),
    ("value measurable across strangers", "unknown traders linked by shared unit labels instead of kinship arrows", "town network map", "scale insight"),
    ("written promise outlives conversation", "spoken bubble fading while clay tablet stays solid", "time contrast", "quiet authority"),
    ("weight travels farther than reputation", "standard weight moving along route while reputation circle stays local", "route comparison", "distance tension"),
    ("witness mark turns argument into evidence", "elder presses witness mark beside grain debt", "proof-object close-up", "solemn pressure"),
    ("standard unit compares unlike things", "grain, labor, cattle, field, and debt linked to one measure", "unit diagram", "intellectual tension"),
    ("conflict gets sharper", "ledger line turning into debt hook around worried debtor", "symbolic warning", "uneasy power"),
    ("measured debt can be enforced", "authority points from tablet to debtor grain basket", "enforcement scene", "serious pressure"),
    ("recorded debt can accumulate", "stacked tablets grow while household grain shrinks", "accumulation scene", "anxious weight"),
    ("tablet holder gains power", "scribe with tablet larger than elder with fading memory cords", "power shift split", "institutional unease"),
    ("money changed the battlefield", "face-to-face dispute becoming tablet-and-unit dispute", "two-arena comparison", "sobering tension"),
    ("coins came later", "timeline from gift web to tablet to weighed metal to stamped coin", "progression strip", "anticipation"),
    ("make metal portable and trusted", "metal fragments, scale, purity mark, and stamp problem labels", "problem board", "focused tension"),
    ("stamped coin says authority stands behind object", "simple stamped disk linked to authority node", "institutional trust diagram", "official pressure"),
    ("social agreement physical disguise", "coin outline peeled back to reveal trust, law, memory, witnesses", "symbolic reveal", "quiet revelation"),
    ("different objects same problem", "cowries, silver weight, cattle mark, grain measure, tablet, coin row", "artifact lineup", "comparative curiosity"),
    ("remember value when trust is thin", "three pressure nodes squeezing memory into record and object", "central system map", "tense question"),
    ("what before money", "question card over grain, shell, cattle mark, tablet, and relationship arrows", "title-question card", "curiosity"),
    ("not one giant barter market", "oversized barter market sign crossed out by smaller real systems", "myth-ending composition", "decisive correction"),
    ("shared, owed, gifted, stored", "action strip of sharing meat, owing grain, gifting shell, storing barley", "multi-action montage", "energetic synthesis"),
    ("counted, witnessed, punished, negotiated", "hands counting marks, elder witnessing, exclusion mark, settlement knot", "process grid", "serious civic pressure"),
    ("displayed wealth and converted trust", "cattle, feast bowl, shell string, tablet turning trust arrows into objects", "transformation diagram", "final clarity"),
    ("memory was no longer enough", "elder lowers tangled cords while scribe lifts tablet", "transition scene", "bittersweet progress"),
    ("part has not disappeared", "ancient clay tablet facing modern phone sketch over timeline bridge", "past-present split", "reflective surprise"),
    ("payment app and clay tablet contrast", "phone payment record and clay tablet side by side", "clean comparison", "curious continuity"),
    ("record says who owes whom", "same debtor-creditor arrow on phone and tablet", "parallel record diagram", "record-based trust"),
    ("system decides transfer counts", "validation gate with witness mark and modern check mark", "approval system map", "cautious authority"),
    ("dispute process exists", "ancient elder circle and modern support path around broken transfer arrow", "parallel dispute map", "tense resolution"),
    ("oldest money was not a coin", "coin silhouette crossed out beside obligation knot", "bold correction card", "final revelation"),
    ("remembered obligation", "fire-circle gift arrow glowing between households", "quiet community scene", "emotional payoff"),
    ("memory became too heavy", "memory web sagging into tablet, weight, coin, and phone record", "final synthesis", "satisfying closure"),
    ("end-card thesis hold", "money is portable trust timeline with empty end-screen space", "clean end screen", "calm ending"),
    ("end-screen background", "subtle clay tablet, shell, grain, and trust loop motifs with safe empty areas", "minimal background", "warm reflective mood"),
    ("final object recap", "barley, cowrie, cattle mark, silver weight, clay tablet, coin, and phone arranged around one trust arrow", "overhead recap tableau", "calm synthesis"),
    ("viewer memory lock", "wrong barter arrow erased while remembered obligation remains beside fire circle", "closing correction panel", "quiet confidence"),
    ("modern echo hold", "ancient witness dots mirrored by modern validation marks across a record bridge", "parallel systems frame", "thoughtful continuity"),
    ("soft fade to trust loop", "fire circle, tablet, and phone record fading into a single trust loop", "wide closing tableau", "reflective payoff"),
    ("final end-screen safe frame", "paper-texture background with small clay tablet corner mark and shell route arrow leaving blank space", "minimal end frame", "calm retention tail"),
]

def timestamp(index):
    if index <= 15:
        start = (index - 1) * 4
        end = start + 4
    else:
        start = 60 + (index - 16) * 5
        end = start + 5
    return f"{start//60}:{start%60:02d}-{end//60}:{end%60:02d}"

def prompt(beat, variant, index):
    phrase, subject, frame, mood = beat
    variants = {
        "A": [
            f"{STYLE}, {frame} built around {subject}; black ink figures lean toward the object as if the clue has just interrupted the easy barter story, off-white paper texture, muted earth and teal accents, {mood} mood, clean foreground framing, no modern cash, no fantasy costume detail.",
            f"{STYLE}, close foreground study of {subject} with two small ancient role figures half-visible behind it, the composition makes '{phrase}' feel like evidence rather than narration, rough tablet-paper grain, angled annotation arrows, {mood} tension, no glossy realism or dollar symbols.",
            f"{STYLE}, split-frame sketch where {subject} occupies the heavier side and the wrong assumption is smaller and crossed out, simple faces register doubt, crisp black linework, restrained amber accent, {mood} pressure, avoid crowded marketplace filler and modern shops.",
            f"{STYLE}, map-like scene showing {subject} inside a small settlement path, huts and witness dots arranged with clear hierarchy, the viewer can read '{phrase}' from action before labels, calm documentary sketch texture, {mood} unease, no cinematic realism.",
            f"{STYLE}, object-led transition frame with {subject} moving across a hand-drawn timeline tick, small arrows show memory, obligation, or scale changing around it, centered composition, paper-grain background, {mood} curiosity, exclude wrong-era tools and decorative clutter.",
            f"{STYLE}, social-pressure sketch of {subject} being watched, counted, refused, or remembered by nearby role figures, medium framing with visible hands and simple expressive faces, muted clay and teal palette, {mood} atmosphere, no royal fantasy styling or modern props.",
            f"{STYLE}, evidence-card composition featuring {subject} pinned like a notebook source beside one short handwritten label for '{phrase}', diagonal shadow from a reed stylus or shell string, focused visual hierarchy, {mood} mood, no unreadable text wall.",
            f"{STYLE}, wide settlement diagram where {subject} becomes the active node between households, route marks, or storage baskets, arrows are sparse and purposeful, role figures remain simple and period-neutral, {mood} pressure, no 3D, no glossy ancient stock look.",
            f"{STYLE}, two-step storyboard panel using {subject} to show before and after of '{phrase}', first panel calm, second panel strained by memory or trust, clean ink borders on notebook paper, {mood} tension, avoid modern coins unless specifically requested.",
            f"{STYLE}, low-angle tabletop sketch of {subject} beside grain marks, shell string, tablet edge, or witness dots as appropriate to the beat, shallow compositional focus within a hand-drawn world, {mood} feeling, no fake readable paragraphs or random crowd."
        ],
        "B": [
            f"{STYLE}, overhead village-network frame where {subject} sits among named-feeling huts, kin lines, and witness dots; one broken or reinforced arrow explains '{phrase}', muted earth tones, careful negative space, {mood} pressure, no generic whiteboard style.",
            f"{STYLE}, character-action version of {subject}: a hunter, elder, scribe, trader, or household figure performs the visible exchange tied to '{phrase}', medium shot, expressive minimal faces, exact prop emphasis, {mood} mood, no fantasy armor or modern storefront.",
            f"{STYLE}, route-and-boundary drawing with {subject} placed at a river line, town gate, storage room, or trade path depending on the beat, small arrows show distance weakening memory, off-white map texture, {mood} caution, no decorative pins.",
            f"{STYLE}, artifact insert showing {subject} on a rough archive scrap with one small date tick or account mark, surrounding objects are limited to the relevant grain, shell, cattle, weight, or tablet clue, macro-style framing, {mood} seriousness, no museum glamour shot.",
            f"{STYLE}, cause-and-effect flow panel where {subject} triggers three compact consequences around '{phrase}', arrows are thick enough to read but not crowded, simple ancient figures react with skepticism or relief, {mood} tone, no abstract spaghetti diagram.",
            f"{STYLE}, social memory scene where {subject} is remembered by watching faces around a fire circle, the important hand gesture or object transfer is centered, warm clay accent against paper texture, {mood} tension, no modern price tags except crossed-out myth symbols.",
            f"{STYLE}, comparison plate with {subject} on one side and its limitation or conflict on the other, labels stay short and hand-lettered, split composition makes the tradeoff instantly visible, {mood} mood, no dollar signs or polished infographic gradients.",
            f"{STYLE}, institutional sketch placing {subject} near a temple storehouse, elder circle, or scribe station when the beat needs scale, foreground shows the object in use rather than posed, measured arrows and tally marks, {mood} pressure, no fantasy palace.",
            f"{STYLE}, close hand-and-tool composition focused on {subject}: reed stylus, measuring bowl, shell cord, silver weight, grain basket, or stamped disk interacts with it, strong foreground framing, black ink texture, {mood} focus, no wrong-era writing tools.",
            f"{STYLE}, progression strip with {subject} changing meaning across two or three small dated stages, timeline arrows stay clean, role figures are silhouettes with expressive posture, muted amber and teal accents, {mood} curiosity, no cluttered ancient crowd."
        ],
        "C": [
            f"{STYLE}, symbolic system frame for '{phrase}' where {subject} is surrounded by only the necessary nodes: memory, trust, obligation, conflict, or scale; centered composition, handwritten micro-labels, {mood} mood, no modern cash icons or glossy effects.",
            f"{STYLE}, dispute-focused version of {subject} with two households, traders, or institutions pulling different arrows away from the same object, elder or witness marks visible when relevant, tense balanced framing, {mood} pressure, no chaotic crowd scene.",
            f"{STYLE}, quiet aftermath frame showing what changes after {subject}: withdrawn help arrows, settled compensation, recorded debt, or validated transfer depending on the beat, wide negative space, paper texture, {mood} reflection, no random marketplace background.",
            f"{STYLE}, object constellation built from {subject} plus two supporting anchors such as barley sacks, cowrie shells, cattle marks, silver weight, clay tablet, or phone record, overhead composition, one central arrow explains '{phrase}', {mood} clarity, no decorative filler.",
            f"{STYLE}, myth-versus-mechanism panel where {subject} replaces a crossed-out simple swap, the correct system is shown through memory marks, witnesses, routes, or records, high contrast ink, {mood} curiosity, no textbook chart look.",
            f"{STYLE}, pressure-map composition with {subject} squeezed between group size, distance, cheating, death, or disagreement labels as fits the narration, small figures show consequences rather than standing idle, {mood} tension, no futuristic elements.",
            f"{STYLE}, end-of-beat synthesis card using {subject} as a clean visual thesis, one short handwritten phrase from '{phrase}', sparse arrows, off-white notebook grain, muted earth palette, {mood} mood, no long readable paragraphs.",
            f"{STYLE}, scale-shift drawing where {subject} starts in a small village circle and points toward a busier town, storehouse, route, or authority stamp, diagonal composition suggests pressure building, {mood} seriousness, no modern buildings in ancient scenes.",
            f"{STYLE}, emotional reaction panel for '{phrase}' with one figure accepting, refusing, recording, weighing, or questioning {subject}; face and hands carry the story, medium close framing, sketch-map background, {mood} feeling, no realistic portrait style.",
            f"{STYLE}, final-choice editor option showing {subject} as a minimal but specific production frame, anchored by the exact prop, setting, and social rule of the narration beat, balanced composition, {mood} tone, no generic people or vague ancient scenery."
        ],
    }
    key_offset = {"A": 0, "B": 3, "C": 6}[variant]
    prompt_text = variants[variant][(index + key_offset) % len(variants[variant])]
    if not any(term in prompt_text.lower() for term in ("close-up", "medium shot", "wide shot", "overhead", "foreground", "framing", "composition", "split frame", "timeline", "map-like")):
        prompt_text = prompt_text.rstrip(".") + ", foreground action."
    return prompt_text

def shot_list():
    lines = []
    for i, beat in enumerate(SHOT_BEATS, 1):
        lines.append(f"{i}. {timestamp(i)}")
        lines.append(f"Narration: {beat[0]}")
        lines.append(f"A: {prompt(beat, 'A', i)}")
        lines.append(f"B: {prompt(beat, 'B', i)}")
        lines.append(f"C: {prompt(beat, 'C', i)}")
        lines.append("")
    return "\n".join(lines)

FRONT = f"""# What Did Ancient Humans Do Before Money? - Full Production Pack

## Title

Primary title: What Did Ancient Humans Do Before Money?

Alternative titles:
- Money Was Not Invented Because of Barter
- Before Coins, Wealth Was a Memory Problem
- The Strange Things Humans Used Before Money
- The Myth of Barter Before Money
- Before Money, Everyone Owed Someone
- How Humans Paid Each Other Before Coins
- Why Ancient Money Started as Trust, Debt, and Grain

## Runtime

Target runtime: 8:05-8:25.
Word budget: 1,080-1,130 spoken words.
Estimated script word count: 1,103 words.
Estimated runtime at 135 words per minute: about 8:10.
Content type: faceless long-form historical systems explainer.

## Misconception Map

- Wrong answer 1: Before money, everybody simply bartered. This is too neat because barter is awkward among neighbors who already know each other and remember obligations.
- Wrong answer 2: Money began when someone picked a shiny object everyone liked. This misses the older jobs of money: measuring, remembering, settling, punishing, and scaling trust.
- Wrong answer 3: Wealth always meant owning a pile of currency. In many early societies, wealth meant livestock, stored grain, dependents, bridewealth, ritual valuables, land access, reputation, and the ability to mobilize people.
- Partial truth: Direct barter existed, especially with strangers or at the edges of communities, but it was not the whole pre-money economy.
- Stronger truth: The road to money runs through relationships first, then memory systems, then standard valuables and units of account when population, distance, institutions, and conflict made memory too fragile.

## Opening Targets

- The barter myth, because it is the viewer's fastest likely answer.
- The shiny-object assumption, because money first needs to be framed as a social technology.
- The cash-only wealth assumption, because status, conflict, and population pressure drive the episode.

## Script Control Brief

- Topic promise: Explain what humans used before money, how exchange worked, how conflicts were handled, how wealth was defined, and why larger populations pushed societies toward measurable money.
- Target runtime and word budget: 8:05-8:25, about 1,080-1,130 spoken words.
- Content type: historical systems explainer with misconception attack.
- Viewer starting belief: Before money, people bartered goods directly until coins solved the inconvenience.
- Opening targets: the barter myth, the assumption that money started as shiny objects, and the assumption that wealth was only stored currency.
- Core replacement idea: Before money became familiar objects, economic life was a web of memory, obligation, redistribution, reputation, valuables, and records.
- Retention engine: every section changes the viewer's answer from barter, to debt, to gift, to status, to ledger, to conflict, to population pressure, to coinage.
- Scene ladder: small camp sharing food, village obligation ledger in memory, stranger trade, ritual gift, cattle wealth, temple grain store, clay tablet account, cowrie and silver object, crowded city conflict, minted coin payoff.
- Re-hook plan: every 20-30 seconds introduce a pressure question: What if the other person forgets, moves away, cheats, dies, becomes powerful, or becomes a stranger?
- Forbidden drift: no fantasy kingdom framing, no generic economics lecture, no modern office examples, no overselling barter as totally nonexistent, no pretending all cultures followed one identical path.
- Ending target: Make money feel less like a clever invention and more like a social technology for replacing fragile memory with portable trust.

## Opening Attack Ladder

- 0:00-0:05: A clay tablet doing a money job before coins appear; the contradiction is that there is no coin in the scene.
- 0:05-0:15: The simple barter answer breaks when needs fail to match.
- 0:15-0:30: Neighbors did not need instant payment as much as memory, reputation, and obligation.
- 0:30-0:45: Strangers, travel, failed promises, and disputes make memory less reliable.
- 0:45-1:00: Money emerges when human groups become too large for trust to stay inside everyone's head.

## Retention Beat Map

- 0:00-0:20: Was barter really first? Clay tablet proof object. Update: money's job existed before familiar money.
- 0:20-0:45: Why is the swap story weak? Farmer, potter, fisher, and mismatched needs. Update: barter is too narrow for daily village life.
- 0:45-1:10: What replaced it? Kin sharing around a fire. Update: memory and relationship handled many exchanges.
- 1:10-1:35: Was it charity? Gift under watching faces. Update: gifts carried obligation.
- 1:35-2:00: How was wealth defined? Cattle, grain, shells, labor access. Update: wealth was social power.
- 2:00-2:30: Why did generosity create status? Feast and surplus. Update: giving can bind people.
- 2:30-3:05: What if someone disagrees? Elder circle, witnesses, compensation. Update: conflict was socially settled.
- 3:05-3:40: What changes with strangers? Boundary trade. Update: direct barter and portable valuables matter where trust is thin.
- 3:40-4:20: Why valuables? Cowries, beads, cattle, grain, metal. Update: each solves a different value problem.
- 4:20-4:55: Did population matter? Town nodes overload memory. Update: scale demands records and institutions.
- 4:55-5:35: What did Mesopotamian records do? Storehouse, barley rations, silver account. Update: records make value measurable.
- 5:35-6:15: How did records affect conflict? Witness marks and debt accumulation. Update: money changes the battlefield.
- 6:15-6:55: Why coins? Metal weight, stamp, authority. Update: coins compress trust into an object.
- 6:55-7:35: What is the deeper pattern? Many objects, one problem. Update: remember value when trust is thin.
- 7:35-8:15: What survives today? Payment app and clay tablet. Update: modern money still runs on records.
- 8:15-8:25: Ending payoff. Final timeline from gift to ledger to coin to screen. Update: memory became too heavy to carry.

## Narrative Texture Rules

- Voice texture: calm, serious, curious, with quiet correction energy.
- Sentence rhythm: short hook attacks, then scene-first paragraphs with pointed questions.
- Scene rule: most paragraphs must contain a visible object, role, place, or conflict.
- Re-hook rule: every 20-30 seconds, update what breaks when memory, trust, distance, group size, or enforcement changes.
- Forbidden phrases or moves: avoid starting with definitions, avoid broad textbook bridges, avoid full-model reveal too early, avoid treating barter as completely absent.
- Model-drip rule: delay the thesis until viewers have seen memory, gift obligation, valuables, conflict, and institutional records.

## Channel Visual Identity Lock

- Channel/niche identity: ancient human systems explained through visible objects, social pressure, and system evolution.
- Default episode visual system: Hybrid Sketch System Map.
- Identity preset name: Ancient/system-map identity.
- Approved alternates or inserts: archive artifact inserts in sketch style, date cards, map routes, clay-tablet close-ups, clean system-loop diagrams, split myth-versus-evidence panels.
- Style DNA: off-white notebook paper texture, black ink linework, muted earth tones, simple role-based human figures, clay tablets, shells, grain sacks, cattle, witness marks, timeline labels, and clear arrows showing trust, memory, exchange, scale, and conflict.
- Thumbnail art DNA: artifact-first composition, crossed-out barter swap or coin assumption, one strong object clue, 2-5 word text, high contrast earth palette, no busy crowd.
- Forbidden drift: no cinematic realism as main style, no polished fantasy villages, no modern props in ancient scenes, no random dollar signs, no border-left accent styling in design notes, no cluttered diagrams.

## Selected Visual System

{STYLE}

Reason: This topic is both ancient economic history and system evolution. It needs people, objects, routes, trust arrows, conflict loops, and timeline progression in one stable visual world.

## Thumbnail

Thumbnail image prompt variation 1:
{STYLE}, artifact-first thumbnail composition showing a clay tablet with debt marks in the center, a crossed-out simple barter swap on one side, tiny grain sacks and cowrie shells on the other, bold empty space for text, off-white paper texture, muted earth tones, black ink arrows, curious myth-busting tension, no coins as the main object, no fantasy marketplace, no modern money.
Text options: \"NO BARTER?\" / \"BEFORE COINS\" / \"NOT BARTER\" / \"MONEY BEFORE MONEY\"

Thumbnail image prompt variation 2:
{STYLE}, split comparison thumbnail with left side showing two confused ancient villagers failing to swap fish for pottery, right side showing a memory web of gifts, grain, shells, and a clay ledger, strong red X over the simple swap, centered composition, high contrast paper texture, skeptical faces, no crowded market, no realistic costumes, no dollar symbols.
Text options: \"THE BARTER MYTH\" / \"WRONG STORY\" / \"WHO OWED WHO?\" / \"TRUST BROKE\"

Thumbnail image prompt variation 3:
{STYLE}, close-up of a small ancient community drawn as nodes around a fire, arrows of obligation leading toward a clay tablet and a stamped coin shadow at the edge, object-first historical mystery mood, clean negative space, muted amber and teal accents, no fantasy palace, no glossy realism, no decorative clutter.
Text options: \"MEMORY FAILED\" / \"TRUST BECAME MONEY\" / \"BEFORE CASH\" / \"DEBT FIRST?\"

Recommendation: Use variation 1 with \"NOT BARTER\" because it attacks the viewer's likely answer in under one second while showing the correct clue object.

## Recurring Character Set

- Ancient community member: {STYLE}, simple adult figure in plain woven tunic, dark ink outline, muted brown clothing accent, expressive but minimal face, often holding grain, tool, fish, or pottery, drawn on off-white notebook texture, no realistic anatomy, no fantasy armor.
- Elder or mediator: {STYLE}, older seated figure with short gray hair marks, plain robe, calm stern expression, one raised hand, small witness dots around them, used for conflict and reputation scenes, no throne, no royal costume.
- Scribe or record keeper: {STYLE}, focused adult figure kneeling beside a clay tablet with reed stylus, simple robe, small grain measure nearby, attentive expression, no modern pen, no scroll if the scene is Mesopotamian clay accounting.
- Stranger trader: {STYLE}, cautious traveler figure with shoulder bundle, shell string or metal weight pouch, standing slightly outside the group circle, skeptical expression, no horse unless specified, no fantasy merchant robes.
- Modern viewer echo: {STYLE} with modern insert restraint, simple contemporary figure holding a phone payment screen as a sketch object, connected by arrows to clay tablet and ledger, no brand logos, no neon app interface.

## Script

{SCRIPT}

## Shot By Shot Image Prompts

"""

BACK = """
## SEO Meta Description

What did ancient humans do before money? The simple answer is usually barter, but the history of money is stranger than that. Before coins became common, many human communities relied on memory, reciprocity, gift obligations, reputation, cattle, grain, shells, metal weights, and eventually written records to manage exchange.

This video explores how early humans handled value before cash: how gifts created debt, how wealth could mean cattle or social power, how conflicts were settled through elders and witnesses, and why strangers, growing populations, temples, palaces, and cities pushed societies toward more measurable systems of value. From clay tablets in Mesopotamia to cowrie shells, barley payments, silver units of account, and stamped coins, money emerges as a solution to a deeper human problem: how to carry trust when memory is no longer enough.

Topics covered:
- Why the barter myth is incomplete
- Gift economies, reciprocity, and obligation
- How ancient wealth was defined
- Conflict resolution before formal money
- Cattle, grain, shells, beads, metal, and clay tablets
- Mesopotamian barley and silver accounting
- Population growth and the rise of records
- Why coins compressed trust into portable objects

#HistoryOfMoney #AncientHistory #EconomicHistory #Anthropology #HumanOrigins

## Hashtags

#HistoryOfMoney #AncientHistory #EconomicHistory #Anthropology #HumanOrigins #Mesopotamia #MoneyExplained

## Tags

what did humans do before money, before money, history of money, origin of money, barter myth, barter before money, ancient money, ancient currency, gift economy, reciprocity, debt before money, cowrie shells, clay tablets, Mesopotamia money, barley money, silver money, cattle wealth, economic history, anthropology of money, how money began, first money, money explained, ancient humans, early trade, wealth before money, conflict before money

## Research Material

Sources used:
- Britannica, \"A Brief History of Money\" - https://www.britannica.com/story/a-brief-and-fascinating-history-of-money. Used for broad historical framing and examples of early currency objects including cowrie shells.
- British Museum collection record for Babylonian clay tablet promissory note for barley - https://www.britishmuseum.org/collection/object/W_1898-0215-862. Used as a concrete proof object for clay records handling payment/debt functions.
- World History Encyclopedia, \"Summary Account of Silver for the Governor\" - https://www.worldhistory.org/image/4854/summary-account-of-silver-for-the-governor/. Used for a visual and factual anchor of Sumerian accounting of silver and commodities on clay tablets.
- National Museum of African American History and Culture, \"Cowrie Shells and Trade Power\" - https://nmaahc.si.edu/cowrie-shells-and-trade-power. Used for cowrie shells as trade money across regions and later West African trade context.
- Open Encyclopedia of Anthropology, \"Gifts\" - https://www.anthroencyclopedia.com/entry/gifts. Used for gift, reciprocity, Mauss/Malinowski framing and the warning that gift systems are not simple free charity.
- Open Encyclopedia of Anthropology, \"Debt\" - https://www.anthroencyclopedia.com/entry/debt. Used for debt as a social relation linked to reciprocity and interdependency.
- Brill / Journal of the Economic and Social History of the Orient, \"Money in Mesopotamia\" - https://brill.com/view/journals/jesh/39/3/article-p224_2.pdf. Used for the statement that barley and silver served money functions in ancient Mesopotamia.
- American Numismatic Association, \"Lydia & the First Coins\" - https://www.money.org/money-museum/virtual-exhibits-hom-case1/. Used for the later coinage section: early coins in Asia Minor were electrum pieces of regular weight with stamped or impressed marks.
- Smithsonian repository, \"Stone Money of Yap\" - https://repository.si.edu/handle/10088/2422 and National Museum of American History object page - https://www.americanhistory.si.edu/pt/collections/object/nmah_1069139. Used as a supporting example that wealth and money can operate through public knowledge and social status, not only pocket-sized payment.

Key facts used:
- Anthropologists and economic historians dispute the textbook sequence where pure barter naturally becomes money; barter existed, but the pure barter economy story is too simple.
- Gift exchange and reciprocity can create obligation, hierarchy, and reputation, not just generosity.
- In Mesopotamia, clay tablets recorded obligations and accounts; barley and silver could perform money functions before widespread coin use.
- Population scale, strangers, institutions, and long-distance exchange make personal memory and reputation less reliable.
- Wealth before coinage could include cattle, grain stores, shells, ritual valuables, dependents, status, and the ability to mobilize labor.

Misconception map:
- The viewer likely thinks barter was the universal pre-money system.
- The viewer likely thinks money began as one convenient object everyone agreed to use.
- The viewer likely assumes wealth meant piles of currency rather than obligations, stored goods, labor access, and reputation.

Opening targets chosen:
- The barter myth, because it is the fastest clickable contradiction for this title.
- The object-first assumption, because the episode needs to shift the viewer from money as object to money as social technology.
- The wealth-as-cash assumption, because it opens the status, conflict, and population angle.

Uncertainty and publishing notes:
- Do not claim barter never happened. The stronger claim is that pure barter as the dominant universal pre-money economy is not well supported.
- Do not imply all societies followed one sequence from gift to barter to coin. Different societies used different mixtures of reciprocity, redistribution, valuables, accounting, and market exchange.
- If adding examples from a specific culture beyond Mesopotamia, Yap, or cowrie-shell trade, verify dates and local meaning before production.
"""

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(FRONT + shot_list() + BACK, encoding="utf-8")

if __name__ == "__main__":
    main()
