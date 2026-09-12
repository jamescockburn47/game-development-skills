---
name: open-world-game-development
description: Help create an open-world game from an idea or brief, with discovery and an interactive HTML game plan for approval before building; keep that plan current while designing, implementing or reviewing traversal, persistent worlds and connected systems.
---

# Open-world game development

Build a world whose distance, information and systems create decisions, and whose
state remains coherent when the player travels, waits, saves or returns.

## Preserve the user's authorship

The user writes the game description. Reuse description text already supplied by the
user verbatim; do not rewrite it, fill missing creative ideas, or present an
agent-written example as the user's game. A generic request to choose, recommend or use
defaults cannot delegate authorship of the description. If it is absent, ask the user
to describe the game in their own words and pause game-dependent planning, comparison
research and building until they do. Process explanation and the request for their text
may continue through the normal questionnaire lifecycle.

Derive clearly labelled implementation recommendations and clarifying questions from
that actual description. If the user later edits it, retain the earlier wording in the
plan history and revise affected decisions, steps and checks for approval. Never treat
a local project file as verified user authorship. Do not start a game questionnaire
when the request is only to edit or explain this skill.

Start from the user's intended fantasy, platform, session length, production
constraints and existing architecture. Do not impose an engine, generation method,
camera, multiplayer model or progression shape. Preserve deliberate quiet, danger or
scarcity when they serve the experience.

## Own the workflow and explain its purpose

In a new-game context, a bare invocation or "I want to make an open-world game" starts this skill's introduction and questionnaire. The user need not restate any of its functions in the prompt. Do not ask whether to begin the intake; begin it. Distinguish game creation from a request merely to explain or edit the skill.

Before the first questions, give a substantive plain-language orientation. Explain that an open world earns its scale through worthwhile traversal, discovery and coherent consequences: map size and visual spectacle do not establish these. The workflow clarifies the player experience, audience, format, challenge and style, then world density, guidance, persistence and arc where relevant. Answers become a working brief and a small complete playable section that tests the hardest connected behavior before dependent regions and systems expand.

While the game is undecided, describe that section as a representative example of the player's chosen activity and relevant world behavior. Do not promise a fixed travel, encounter, setback and return itinerary before hearing the answers. The checks below are conditional candidates, not mechanics to add to the user's game.

Explain what happens next: create an interactive HTML game plan that shows the user's unchanged description first, then the next work, useful verified comparisons and how success will be judged. The user can change and approve it. After approval, use the actual development environment to implement, drive ordinary player actions, inspect presentation and profile representative loads; check a relevant leave/return or save consequence; revise from evidence and update the plan after meaningful milestones. The user supplies the description, preferences and corrections, while the skill remembers the answers and connects them to design, architecture and checks. It asks a few questions at a time and can recommend implementation details. Preserve existing engines and explicit planning-only or other scope limits. Do not promise unavailable tools, verified enjoyment, device performance or a whole finished world from a sample run.

Explain the efficiency premise candidly: a reusable brief, relevant context, small experiments, focused tests and selective delegation can avoid wrong turns, repeated explanation and unnecessary token use. Intake, verification and coordination have their own cost. Net token savings are task-dependent and have not been established without a comparable measurement; never guarantee a percentage or trade away the agreed outcome to claim savings.

Give one shared orientation when the general skill is also active, adding the world-specific purpose here. In the persistent-text fallback, keep the orientation and full questions together; for a supported form, introduce it before dispatch and preserve the pending answer channel. Explain once at a new project's start or substantial reset, not on every turn. For a supplied brief with a verified user-authored description, or for a focused correction, give a relevant short explanation, ask only material missing choices and proceed. A delegated brief without that description remains awaiting user authorship. Reuse recorded decisions and load only the references and project context needed for the current claim.

## Begin with the player's brief

For a new game or a material redesign, start with the adaptive [world questionnaire](references/world-questionnaire.md). First obtain the user's own game description if absent, or carry forward their supplied wording verbatim. Establish the game type, format, audience, challenge and session needs, then ask about the world choices that affect the next slice. Prefill from existing answers; keep age, experience, access needs and difficulty distinct. Derive a working brief with labelled decisions, provisional assumptions and open questions, then prepare the required HTML review below. Honor delegated implementation choices and immediate-prototype goals without treating them as a waiver of authorship or approval.

When both game skills are active, use the general questionnaire once and add only the relevant world questions. For focused corrections, reuse the existing brief and ask only about missing constraints that could change the fix. This skill remains usable alone.

Keep the answer channel alive: an asynchronous form acknowledgement is not a submitted answer. Preserve the pending interaction with the host's supported wait; do not follow it with a closing response that dismisses the form. If that lifecycle is unavailable or uncertain, place the complete questions and options in an ordinary final chat message and await the next reply. Follow the [question lifecycle](references/world-questionnaire.md#preserve-the-question-and-answer-turn) and retain prior answers.

## Review decisions before building

Apply the self-contained [game-plan review and approval checkpoint](references/design-review.md) before game implementation outside a currently approved scope. Generate the versioned offline HTML artifact with the packaged builder and assets. Present the user's unchanged game description before the derived decisions; then give useful verified reference examples, the exact first-build scope, exclusions, next steps, checks and unknowns, including relevant traversal, density, persistence and arc choices. Use ordinary language throughout user-facing content. Mention technical terms only when they affect a meaningful choice and explain them. When both game skills are active, produce one shared artifact and approval.

Game code, scaffolding, dependency installation, implementation-worker dispatch and prototype builds wait for explicit user approval of the current unchanged review. Inspection, design, targeted reference research and review-artifact preparation/testing may proceed. User edits require an updated brief, affected plan/checks and a new review revision. A local click, downloaded response, archived plan identity or valid file is not user authorization; verify the returned revision against the current source and an actual user action in the task or supported host interface. Continue unchanged approved scope without another gate. Progress-only game-plan updates do not renew approval or pause authorized work; a material design or scope change becomes a new proposal and returns to the gate. Honor an explicit later waiver. The gate concerns building games, not an already-authorized request to modify this skill or its review tools.

## Choose the smallest representative vertical slice

Before expanding content, identify the applicable parts of the chosen game's slice:

- the ordinary way a player enters the world and chooses where to go;
- one traversal decision where route, time, risk or resources matter;
- one encounter between at least two connected systems;
- one consequence that remains after leaving and returning;
- one credible setback and a legible recovery path.

This is a test shape, not a mandatory quest formula. Adapt it to the game. Name the
hardest uncertain mechanism and a plausible counterexample that could make a weak
demo look successful. Prove that mechanism before adding dependent regions or quests.
Include sensory feedback early when camera, movement or readability is part of the
mechanism being tested.

For spatial scale, streaming, persistence, simulation tiers and performance, read
[world systems](references/world-systems.md). For factions, economies, quests,
exploration information and lasting world change, read
[progression and causality](references/progression-and-causality.md). For browser,
engine, comparative or pacing probes, read
[evidence probes](references/evidence-probes.md).

## Establish the world contract

Own the engineering consequences as well as the design. State the critical player
journey, credible failure and proof needed using the current project's risk scheme.
Keep prototypes and reversible changes small; persistent player flows need focused
regressions and integration evidence, while account-security/real-money changes or credible loss of
irreplaceable saves need deterministic enforcement, fresh review and verified recovery.
For multi-module durable work or release preparation, get one fresh review and one
focused fix/recheck unless material critical risk justifies more. Do not make users
answer an architecture questionnaire or impose a universal test/review framework.

Apply the [engineering boundaries and delivery guidance](references/world-systems.md#engineering-boundaries-and-delivery)
when implementation, persistence or release work warrants it. It keeps state ownership,
configuration, modules, generated artifacts and the verification path coherent while
retaining this skill's independence from the general companion.

Make these decisions explicit where they affect behavior:

- coordinate, distance and time units, travel compression, boundaries and transitions;
- how often traversal asks for a choice, and where density intentionally changes;
- which state is simulated near, far away and offscreen;
- which entities have durable identity, ownership and lifecycle records;
- which system may commit damage, stock, allegiance, quest and world-state changes;
- what survives save/load, streaming, death, fast travel and version changes;
- frame, memory, population and content budgets, including what LOD may simplify.

Near and far simulation may differ in detail, but must preserve the same authoritative
facts. Streaming must not duplicate rewards, reset finite stock, resurrect removed
entities or erase an in-progress consequence.

## Make systems causally legible

Prefer events that name the subject, cause and committed outcome. Quests and
achievements should observe authoritative results rather than mint them. Bind proof
to the intended entity, place or source when substitutes would change the meaning.

Where continued play is intended, give consequential states a recovery path: reroute,
repair, retreat, retry, replace a lost objective, or fail explicitly and issue fresh
work. Deliberate permanent loss is valid when it matches the brief. Avoid an objective
that stays active after its only subject is gone.

Exploration should change what the player can infer or choose. Distinguish current
sight, remembered information, rumours and omniscient data. Let discoveries expose
routes, risks, opportunities or explanations rather than only incrementing a counter.

## Verify the connected experience

Use the actual development environment: inspect the project instructions, engine,
build and verification commands, then discover available runtime automation,
debuggers, visual/audio inspection and profiling tools. Use supported engine or
device interfaces for native games and browser tools for browser games. Test the
player-delivered build where delivery matters. Delegate independent tasks with
explicit ownership when available and useful, retaining integration responsibility.
Use relevant installed skills and authorized asset tools; no specific tool, model,
service or companion skill is required. Unavailable device or sensory evidence stays
an explicit gap; do not invent a successful run. Use the scope and permissions already
granted; tool availability alone does not authorize spending, publishing or deployment.

Use the minimum evidence that can establish the claim:

1. Test deterministic rules for bounds, conservation, identity, eligibility,
   persistence and recovery, including a known-wrong counterexample.
2. Exercise the ordinary first-use path through the real coordinator when streaming,
   input, timing, save/load or system interaction matters.
3. Trigger one representative setback and verify that the next action is possible and
   clear.
4. Inspect actual rendered output for landmark readability, navigation cues, LOD
   transitions, encounter legibility and interface obstruction.
5. Measure frame, memory or population budgets only on representative world loads.

State whether elapsed time is active simulation time, wall time or fictional time.
Disclose teleports, accelerated stepping, seeded populations and granted inventory;
they can isolate a mechanism but cannot prove the ordinary journey they bypass.

Run one bounded experiment and one evidence-led revision before reassessing a failed
central mechanism. Preserve raw measurements and the verdict, including failures.
Do not require every probe for a small reversible change.

Read the latest project-owned game plan when resuming work. Update it after a meaningful
milestone, playtest, decision or handoff rather than every tool call, and record evidence
before marking a milestone done. The HTML does not update itself; the agent rebuilds it.

The optional `evidence-led-game-development` companion can help with a broader
cross-system assessment, but this skill has no dependency on it.
