---
name: evidence-led-game-development
description: Help create games from an idea or brief, and design, implement, assess or playtest existing games across genres and engines. Leads discovery, prepares an interactive HTML game plan for approval before building, then keeps it current while developing a playable slice from evidence.
---

# General game development

Start with what the player should experience, then prove the mechanics and presentation that create it. This applies to new games and existing projects, including action, puzzle, strategy, narrative, rhythm and simulation games. Choose the engine, platform, asset approach and game structure from the actual brief and project constraints.

## Preserve the user's authorship

The user writes the game description. Reuse description text already supplied by the
user verbatim; do not rewrite it, complete missing creative ideas, or present an
agent-written sample as the user's game. A generic request to choose, recommend or use
defaults cannot delegate authorship of the description. If no description has been
supplied, ask the user to describe the game in their own words and pause
game-dependent planning, comparison research and building until they do. You may still
explain the process and ask for that text through the normal questionnaire lifecycle.

Derive implementation recommendations and clarifying questions from the actual
description, and label agent recommendations as such. If the user later edits the
description, preserve the earlier wording in the plan history and revise every affected
decision, step and check for a new approval. A project file may preserve text, but it
does not by itself verify that the user authored or confirmed it. This authorship rule
does not create a questionnaire when the task is to edit or explain the skill itself.

## Own the workflow and explain its purpose

In a new-game context, invoking this skill is enough to start the introduction and intake. A bare invocation or "I want to make a game" does not require the user to add "ask me questions", "make a plan", "use tools" or "test it". Those functions belong to the skill. Do not ask whether the user wants the skill's workflow before beginning it. Distinguish creating a game from a request merely to explain or edit this skill.

Before the first questions, give a substantive, plain-language orientation, normally a few short paragraphs or a compact sequence. Explain the following in terms of the user's project, without requiring them to read the skill file:

- **Premise:** start with the intended player experience, then test whether mechanics, controls and presentation create it. More features, attractive screenshots and successful compilation alone do not establish a coherent, understandable or enjoyable game.
- **Process and outputs:** clarify the game, audience, format, challenge, style and constraints; turn the answers into a working brief and small proposed playable section; present an interactive HTML game plan that describes the game first, then the next work and how it will be judged; let the user amend and approve it; only then implement, inspect and playtest it. Keep the plan current after meaningful milestones so a resumed session can see what changed and what needs revisiting. Revise from evidence before expanding content and the longer game arc. Define a "playable slice" in ordinary language on first use.
- **Collaboration:** the user supplies the game description, preferences and corrections; the skill preserves that wording, connects it to concrete design and technical decisions, remembers settled answers and can recommend unspecified implementation details. It asks a few questions at a time. Respect a planning-only request or another explicit milestone rather than silently extending authorization.
- **Environment and limits:** use the available project files, terminal, engine/build/test tools, runtime input, visual/audio inspection, profiling and useful delegation. Preserve an existing stack. Actual device or human-player checks may remain necessary; a skill cannot supply unavailable capabilities or guarantee fun.
- **Engineering:** keep the implementation understandable, reproducible and safe for the player's progress. Explain briefly that rigor scales with consequences: a throwaway mechanic and a change to real saves or accounts need different checks. The agent owns these technical choices; the player questionnaire is not an architecture exam.
- **Efficiency:** the workflow is designed to reduce avoidable rework and token expenditure through a reusable brief, targeted context, small experiments and focused checks. Introduction, questions and verification also cost tokens; delegation adds overhead. Net savings depend on the task and are not measured or guaranteed unless a comparable evaluation establishes them.

Then initiate the first relevant questionnaire round yourself. Deliver one combined orientation when both game skills are active. Keep it with the chosen answer channel: in the persistent-text fallback, include the orientation and complete questions in the same response; with a supported interactive form, introduce it before dispatch and preserve its pending lifecycle. Do not send a second closing message over an unanswered form.

Explain the method once at the start of a new project or substantial reset. For an already-settled brief, continuation or narrow fix, give only the task-relevant explanation and act within scope. A brief that already contains a verified user-authored description can make further questions unnecessary; delegation can resolve other choices but never supply the description. Absence of the words "ask me questions" cannot prevent the required intake.

## Begin with an adaptive game questionnaire

For a new game or a substantial change of direction, read [game questionnaire](references/game-questionnaire.md) and first obtain the user's own game description if it is absent. Use prior user-authored description text verbatim and prior answers to prefill the brief; ask a few useful questions at a time. Establish game type, delivery format, intended players, challenge, session shape and presentation before making dependent design choices. Treat age, experience, reading and motor demands, content suitability and preferred difficulty as separate dimensions.

Use the description and answers to make a short working brief that directly determines the next playable slice, controls, teaching, art direction, technical choices and acceptance checks. Preserve the description unchanged; write the derived user-facing review content in ordinary language and label its source. Include technical terms only when they change a meaningful choice and explain them. Distinguish user decisions, delegated implementation choices, provisional assumptions and unresolved questions. Ask only for missing choices that materially affect the next step, and respect an explicit request to choose implementation defaults. Delegating choices does not waive description authorship or the HTML approval checkpoint below. For a focused fix or assessment, reuse the existing brief and ask only about relevant gaps. When both game skills are active, conduct one shared intake and review.

Keep the questionnaire answerable. An asynchronous form's accepted/queued acknowledgement is not a user answer: preserve the pending interaction and use the host's supported wait instead of ending the turn with a closing message. If that lifecycle is unavailable or uncertain, put the complete questions and choices in an ordinary final chat message and await the next user reply. Do not leave the only questions in a transient card or collapsed commentary. Follow the [question lifecycle](references/game-questionnaire.md#keep-the-questions-answerable) before choosing the input tool.

## Review decisions before building

Before any game implementation outside an already-approved scope, read [game-plan review and approval](references/design-review.md). Create the versioned, standalone interactive HTML artifact from the working brief using the packaged builder and assets. Put the user's unchanged game description first, then show the derived decisions and their sources, useful verified reference examples, editable alternatives, the specific build scope, exclusions, next steps, acceptance checks and remaining questions. Present the actual artifact for explicit user approval. A brief being complete, a request for a quick prototype or an invitation to choose defaults does not bypass description authorship or this requested checkpoint.

Inspection, design, targeted reference research and producing/testing the review artifact are allowed before approval. Game code, scaffolding, dependency installation, implementation agents and technical prototype builds must wait. Edits invalidate the reviewed revision: incorporate them, update affected steps and checks, and present a new revision for approval. Validate any returned response against the current source review, and confirm an actual user approval through the task or verified host interaction; a local click, export or file alone is not authorization. Continue within an unchanged approved scope without repeating the checkpoint. Progress-only updates to the living game plan neither renew approval nor pause work. Material design or scope changes return to a new proposal and current approval gate. Honor an explicit later user waiver, and do not apply this game-build gate recursively to a request to edit the skill or review mechanism itself.

## Select the relevant workflow

For a new game, feature or broad expansion, read [design to build](references/design-to-build.md). For an assessment or uncertain mechanism, read [probe methods](references/probe-methods.md). Small fixes rarely need the full workflow. The separately installable `open-world-game-development` skill adds guidance for persistent explorable worlds; it is optional.

When the promise depends on simulated, procedural or physically meaningful appearance, read [model and presentation](references/model-and-presentation.md). It separates a correct component, the visible result and the playable experience.

## Define the playable claim

Identify the intended experience, a representative player action or decision, its feedback and consequence, and the session structure. A level, match, puzzle, story branch or freeform session can be the unit; do not impose travel, combat, progression or a win condition on a game that does not need them.

State the consequence and evidence needed using the project's risk conventions. A disposable prototype, reversible visual change, durable player save and real-money transaction need different assurance. Name the hardest uncertain mechanism and a pass/fail example, including a plausible result that would look successful to a weak test.

After approval of its review, build the smallest representative playable slice that can answer that question. Include essential sensory feedback when it is part of the mechanism: movement, timing, camera and sound cannot always be assessed behind a placeholder UI. Defer dependent content expansion until the slice supports the intended experience.

## Use the minimum sufficient evidence ladder

1. Exercise rules directly where quantities, eligibility, bounded effects, conservation or state transitions determine correctness. Control time and randomness when useful.
2. Exercise actual input and the production runtime when wiring, timing, save/reload or world state matters. Test the target platform; browser automation is only one possible driver.
3. Compare meaningful alternatives or a credible setback when the claim concerns choice, balance or recovery. Use player-visible outcomes rather than invocation counts.
4. Inspect and play the actual output for visual hierarchy, control feel, animation, audio feedback and readability claims. Numerical settings and captured artifacts alone do not establish quality.

Select the evidence that answers the claim. A color adjustment need not trigger a full campaign test; a green unit check cannot establish an unfamiliar player's understanding or enjoyment.

## Keep evidence honest

- Distinguish active simulation time, wall time, turns and fictional time where relevant. State any acceleration and what it can and cannot establish.
- Identify injected fixtures and granted state. Never present a fabricated completion, teleported outcome, or direct state mutation as proof of the corresponding journey.
- Treat counters, selected labels, elapsed timers, valid schemas, and successful rendering as observations. Require the intended consequence.
- Challenge surprising failures and successes against source and a discriminating rerun. Correct harness faults without converting them into product findings.

## Implement and revise

Check that the current scope and review revision are explicitly approved before beginning game implementation. Do not interpret a structurally valid response file or archived approved-plan identity as verified user authorization. Changes outside that scope return to the review checkpoint.

For substantial implementation, durable state or release preparation, apply [engineering hygiene](references/engineering-hygiene.md). Own the consequence classification, state boundaries and proof needed; follow the current project's policy and keep any added structure proportional. Preserve a canonical verification path and turn important guarantees into executable checks. Small reversible work uses the relevant subset without a new checklist or review process.

Keep the explanation operational: reuse the current brief and prior evidence; load only the relevant reference and project context; prefer targeted reads, small repeatable experiments and the existing verification path. Broaden a search, test run or delegation only when an unresolved claim justifies it. Do not cut agreed quality or omit necessary tests to make a token-saving claim, and do not repeat onboarding at each turn.

Before implementation or testing, read [development environment](references/development-environment.md). Inspect the actual project and available capabilities, then use the relevant editor, terminal, engine, automation, visual inspection, profiling and delegation tools to carry the work through to a verified playable result. Tool availability and authorization are discovered, not assumed; a text-only environment cannot establish that a build runs or feels right.

Keep authoritative rules, runtime effects and presentation coherent; use the existing engine's idioms and verification path. Define ownership for state and transactions before dividing implementation. Extract boundaries when they improve comprehension, reuse or testing, not to satisfy a preferred architecture.

Name concrete engine and UI structures only when the project establishes them. Otherwise describe the relevant ownership or input boundary without assuming a DOM, scene tree, entity framework or particular test runner.

Judge the result against the intended experience: mastery, comprehension, expression, tension, discovery or another stated purpose. A cosmetic or expressive choice need not have an economic effect. Failure may be deliberate; accidental softlocks and unexplained loss are different. Prefer the smallest revision supported by observations and preserve what already works.

Bound experiments and reassess after a failed revision. A further trial needs a changed hypothesis and a discriminating test; an exhausted budget does not make a failed central requirement pass. Preserve the goal or get agreement before reducing it.

Delegate separable tasks with owned files, contracts and acceptance examples when that saves useful work. Lower-cost models can handle bounded implementation; coordination owns integration and final player experience. Fresh review should inspect code and actual artifacts. Do not assume delegation is cheaper or more reliable without evidence.

Respect project scope, asset and persistence policies. A skill grants no permission to publish, deploy, commit, contact others, purchase services, or erase existing player data. After the required design approval, do authorized work within that scope without repeated approval ceremonies; retain existing user decisions.

Run the project's relevant verification path and check what it actually ran against the claimed acceptance criteria. Confirm that the ordinary entry uses the tested implementation. Preserve commands, measurements, fixture disclosures, actual-output verdicts and limits with the work. Use the [evidence record](references/evidence-record.md) for substantial assessments. Report implemented behavior separately from design intentions and untested quality claims. Read the latest project-owned game plan when resuming work and update it after a meaningful milestone, playtest, decision or handoff, rather than after every tool call; the page changes only when the agent rebuilds it.
