# Open-world questionnaire

Begin a new game or substantial redesign with the user's missing choices. When using
the general game-development skill too, reuse its intake and brief; do not interview
the user twice. For an existing game's focused repair, preserve settled choices.

## Establish the base brief when using this skill alone

Initiate this intake for new-game work even when the user simply invokes the skill.
Give the opening orientation described in `SKILL.md`, then begin the first questions;
do not require the prompt to repeat the workflow or repeat the overview each turn.

Read the conversation and available project design first. Ask a few short questions
at a time, choosing an answer channel whose lifecycle you can preserve, as below. Start
by obtaining the user's own description of the game if it is absent. Reuse description
text already supplied in the conversation verbatim. Optional prompts may ask what the
player does, what the world is like or what experience they want, but do not write or
complete the description for them. Pause game-dependent questions, research and
planning until it arrives. Then ask the missing essentials: intended age range and
gaming experience; target platform, view and inputs. Follow up as needed on challenge
and recovery, session length, solo/local/online play, persistence, visual/audio style,
content boundaries, access needs, first milestone and production constraints.

Separate age from reading demands, dexterity, content maturity and difficulty. Offer
plain examples and a recommendation option for implementation choices; do not require a novice to select an
engine. Inspect an existing stack rather than asking the user to reconstruct it.
Honor requests to choose implementation defaults and state those choices in the design
review. A generic delegation such as "recommend for me" cannot supply, rewrite or fill
gaps in the game description. Delegation or a request for an immediate prototype does
not waive description authorship or the approval checkpoint.
Offer examples for audience, challenge, device and session length independently;
do not bundle "families/easy/phone/short" or "adults/hard/desktop/long" into profiles.
A young experienced player can want hard planning, and a phone game can have long sessions.

## Preserve the question and answer turn

Use a blocking question tool only where the host supports that mode. If using an
asynchronous form, distinguish request acknowledgement (`accepted` or `queued`) from
actual user answers. Keep one unanswered round pending; use independent work only
while it preserves the form, then the host's interruptible wait. Do not send a closing
response that dismisses the form, replace it with another round, or write the dependent
brief before a reply. A wait timeout or preselected option is not a submitted answer.

If the form cannot remain active, its lifecycle is uncertain, or it was dismissed,
place every unanswered question and its options in a persistent final chat message
and await the next user reply. Commentary alone and "answer the questions above" do
not recover a disappearing card. Retain earlier answers; empty or cancelled results
do not select defaults. Respect an explicit stop or delegation of remaining choices.

Check tool/turn behavior in a real-host trial when claiming an interactive intake
works. Sample response text cannot prove card visibility; distinguish observed UI
behavior from a transcript that only establishes a pending request.

## Add only world questions that change the next slice

| Question | Implication |
|---|---|
| What makes going somewhere interesting, and how does the player move? | Traversal actions, route choice, information and what must be playable first. Preserve peaceful or expressive travel when intended. |
| Do you want a compact dense world, long quiet journeys, connected regions or something else? | Density, distance/time scale, streaming and pacing checks. Do not equate map size with value. |
| What should the player discover, and how much guidance should they receive? | Landmarks, maps, hints, information uncertainty, teaching and exploration rewards where appropriate. |
| What should keep happening while the player is elsewhere, and what should remain changed on return? | Persistent identity, simulation ownership, near/far behavior and save/return evidence. Explain the visible consequence before asking about technology. |
| What does a setback mean here, and how does the player continue? | Recovery, retry, intentional lasting loss or an explicit no-failure design. Do not introduce hunger, combat or survival meters without a reason in the brief. |
| What changes across a session and the longer game, if anything? | Learning, expression, relationships, responsibilities, progression or a deliberately freeform arc. Factions, crafting and economies are conditional. |

Choose the two or three world questions that most affect the immediate design. Defer
the rest if they do not affect the slice. If preferences conflict, describe the
tradeoff and resolve it; unanswered material choices are not permission to guess.
Continue independent inspection only while preserving the pending answer channel.

## Produce one living game plan

Record the base choices plus world scale, traversal, guidance, lasting changes,
recovery and arc in the existing design document. If the project has no convention,
use `docs/game-plan/review.json` and `docs/game-plan/index.html`; in a text-only
environment, retain the brief in the conversation. Start with the user's exact game
description and its concrete user-message or returned-response source. Never treat a
local file as verified authorship. If the user has not supplied the description, leave
it blank with no invented game and wait. Distinguish user answers, delegated
implementation choices, provisional assumptions and open questions in the material
derived from the description.

Connect each material answer to the next playable slice and its evidence: a short
session needs an achievable stopping point; navigation without markers needs readable
landmarks; a lasting animal encounter needs stable identity across leave/save/return.
Specify the actual platform and player view for visual, input and performance checks.
Do not label an injected destination as proof that the journey is engaging.

Present the brief and next slice through the versioned HTML game plan required by the
general game-development skill's `references/design-review.md`. Where comparison helps
a material world choice, research two to four targeted official or authoritative
sources. Keep the sourced observation separate from the proposed lesson and explain how
this world retains its own identity; never invent a link. Begin game implementation only
after explicit approval of the current unchanged proposal. Continuations and progress
updates inside an already approved scope do not repeat the checkpoint. Read the latest
plan when resuming work and update it after a meaningful milestone, playtest, decision
or handoff. Revisit affected decisions and checks when the user changes an answer;
preserve unrelated agreements and use a new proposal before seeking approval again for
a material design or scope change.

If the user edits the description, retain the earlier exact wording in archived plan
history, store the new wording unchanged with its new source, and revise affected world
recommendations, steps and checks before approval.
