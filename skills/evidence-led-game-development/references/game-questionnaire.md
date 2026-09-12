# Game questionnaire and working brief

Use at the start of a new game or a material redesign. The purpose is to shape a
specific game, not to complete a form. Existing feature work needs only relevant gaps.

## Conduct the conversation

This is initiated by the skill for new-game work, not only when the prompt asks for
questions. Give the opening orientation required by `SKILL.md`, then ask the first
round. Do not ask permission to run the intake or repeat the overview each turn.

Read the user's request, earlier decisions and available project brief first. Reflect
the known choices in one short sentence and ask only what is missing. Do not infer
the intended players from the creator's age or technical experience.

The first required creative input is the user's own description of the game. Reuse any
description already supplied in the conversation verbatim. If none exists, ask the user
to describe the game in their own words; optional prompts may ask what the player does,
what the setting is, or what experience they want, but do not draft an answer for them.
Do not fill gaps, rewrite their prose, or use a sample concept as their game. Until a
description arrives, pause questions, research and planning whose answers depend on the
game's creative premise. You may explain the workflow and preserve the pending question.

Start with at most three or four short questions about the choices that most change
the next step. Choose an answer channel whose lifecycle you can preserve, as below.
Offer a few understandable examples where useful, allow free answers and
"recommend for me" for implementation choices, and keep engine jargon out of a
nontechnical user's first round. That delegation never applies to the game description.
Choose from the question bank below; do not deliver it all as a compulsory survey.
Keep examples on separate axes: do not bundle age with difficulty, or device with
session length, into profiles the user must select as a package. A child may want
demanding play, and a phone game may support a long session.

Ask a follow-up only when an answer changes the design materially. Resolve a conflict
such as "one-button touch controls" and "many simultaneous combat commands" with a
concrete tradeoff. Do not silently discard either preference. While an asynchronous
question remains active, inspect the project or do other independent work only if
that preserves the pending interaction; then use the host's supported wait.
Unanswered material preferences remain open; elapsed time is not a user's decision.
If the user delegates implementation choices or requests an immediate prototype,
choose appropriate defaults and label them. Delegation such as "recommend for me" does
not supply the description or waive the design-review checkpoint in `design-review.md`.

## Keep the questions answerable

Select the supported route before asking; tool availability alone is insufficient:

- A blocking question tool can return the actual submitted answers. Use it only in
  modes where the host permits it; inspect the result for answers or cancellation.
- An asynchronous question tool may return only acknowledgement, such as
  `accepted: true` or `queued`. The question is still pending. Do independent work
  while preserving the form, then use the host's interruptible wait until a user
  response arrives. Waiting may be bounded per call; a timeout is not an answer.
  Do not issue a closing/final response that would dismiss the form, create another
  question batch over it, or generate the dependent brief before receiving answers.
- When an interactive form cannot be kept pending, its lifecycle is uncertain, or a
  form was dismissed, use persistent chat: put the full unanswered questions and
  their options in the ordinary final response and stop for the next user reply.
  Do not use commentary alone or refer to a vanished form with "answer above".

One unanswered round stays active at a time. A highlighted/default option is not a
submission. Cancellation, dismissal, an empty tool result or ending unrelated work
does not supply preferences. Preserve received answers and carry unanswered items
forward without silently resetting the interview. An explicit request to stop ends
the interview; an explicit request to choose defaults delegates only the remaining
implementation choices, never the description.

On a real-host test, inspect what happens after the question request returns and
whether the user can still answer. A written sample questionnaire cannot establish
that its interactive card survives the surrounding agent turn. If visibility cannot
be observed, limit the claim to the recorded tool/turn lifecycle.

## Question bank

| Area | Ask in the user's language | Design decisions informed |
|---|---|---|
| Game description | In your own words, describe the game you want to make. If useful, include what the player does, the setting, and the experience you want. | Authoritative user-written description. Preserve it verbatim; derive and label later recommendations rather than rewriting it. |
| Game and experience | From your description, which activities or feelings matter most? Any examples to borrow from or avoid? | Main player actions, source of enjoyment, genre boundaries and first experiment. References describe qualities, not a mandate to clone a whole game. |
| Players | Who is it for: age range, previous gaming experience and any reading, control or accessibility needs? | Teaching, text load, input demands and accessible feedback. Ask about these separately when relevant rather than equating young players with easy games. |
| Delivery and view | Where should people play: browser, desktop, mobile, console or another format? Do you have a preference for 2D, 3D or text, camera view and controls? | Runtime, device and input constraints, layout, performance and packaging. Resolve only choices needed now; recommend technical details when the user has no preference. |
| Challenge and consequences | What should be challenging: reflexes, puzzles, strategy, exploration or something else? How forgiving should mistakes be? | Difficulty dimensions, hints, assists, adjustable settings, retry/undo, checkpoints and stakes. Content maturity is a separate choice. |
| Sessions and company | Is this solo, shared locally or online? How long is a typical session, and should progress carry between sessions? | Session loop, pause/save behavior, networking and onboarding. Distinguish the first milestone from eventual ambitions. |
| Presentation and content | What visual and audio style, mood and themes fit? What should be excluded, and are there existing assets or rules about creating or using them? | Art direction, sound, feedback, content boundaries and asset workflow. Do not infer a formal age rating from the audience description. |
| Scope and constraints | What should the first playable version include, what can wait, and are there time, budget, engine or release constraints? | Milestone, available tools, reuse, technical feasibility and checks. Inspect an existing stack before asking the user to repeat its details. |

Branch only when relevant: educational goals, language/localization, controller or
touch specifics, multiplayer fairness, monetization, modding, player-created content,
or an explicit accuracy requirement. Do not add these systems merely by asking.

## Preserve the description and derive the working brief

Maintain a compact brief in the project's existing design location. If none exists,
use `docs/game-plan/review.json` and `docs/game-plan/index.html` for the review, plus a
short Markdown brief only when it helps; otherwise retain the brief in the conversation.
Keep it current as answers change. Begin with the user's description exactly as
supplied, without paraphrase, completion or stylistic editing. Record a concrete source
for it from the user message or returned questionnaire response. A local file is not
proof that the user authored or confirmed the words. If the description is still
awaiting the user, leave it blank with no invented example and do not expand into
game-dependent recommendations.

Then derive and clearly label the choices that support that description:

- intended experience and main player actions;
- audience, experience, relevant access needs and content boundaries;
- delivery platform, view, inputs and play mode;
- challenge dimensions, recovery, teaching and session/persistence model;
- visual/audio direction, asset policy and concrete quality criteria;
- first playable milestone, later ambitions and deliberate exclusions;
- relevant technical constraints and the tools available to build and test it;
- hardest assumption and the evidence that would accept or reject the slice.

Mark each unsettled item as a provisional assumption or an open question; distinguish
implementation choices explicitly delegated to the agent. Do not present defaults as
user answers, and do not use delegation to supply or alter the description.
Map the important answers to an implementation choice and an observable check. For
example, touch-only play needs layout and gesture trials on the target input; short
sessions need a complete small loop and the agreed exit/resume behavior; novice
players need an observable learn-first interaction before a mastery challenge.

Age is not a difficulty algorithm. An experienced nine-year-old can want demanding
strategy with little reading; an adult beginner can want complex themes with generous
control assists. Derive teaching and challenge from the stated needs, and keep any
target-player validation explicit before claiming age suitability or enjoyment.

Present the brief and next slice through the versioned HTML game plan required by
`design-review.md`. Where examples will sharpen a material choice, research two to four
targeted official or authoritative sources and keep each observed fact separate from
the proposed lesson and the game's own identity. Never invent a link; record a research
gap if none can be verified. Do not begin game implementation until the user explicitly
approves the current unchanged proposal. Continuations and progress updates inside an
already approved scope do not repeat the checkpoint merely because the same answers are
written elsewhere. On later work, read the latest plan and revisit affected answers
after meaningful playtests, milestones, decisions or handoffs.

When the user edits the description, keep the previous exact wording in the archived
plan history, replace the current description with the new exact wording and source,
and revise every affected recommendation, step and check before presenting a new
proposal for approval.
