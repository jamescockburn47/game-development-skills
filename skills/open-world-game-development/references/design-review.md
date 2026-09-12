# Game plan, review and approval checkpoint

Use this checkpoint after the questionnaire and working brief for every new game and
every materially revised game brief. It is required before game implementation begins.
The same page remains useful later: it records what the game is, what is being made
next, what has been learned and which decisions should be revisited.

## Preserve the user's game description

The description is written by the user. Copy their wording exactly from a concrete
user message or returned questionnaire response; do not rewrite it, infer missing
creative ideas, or substitute an agent-written example. A generic request to choose,
recommend or use defaults applies only to derived implementation choices and cannot
waive this authorship requirement. If the description is absent, use an awaiting-user
template with a blank description and no invented game, ask the user to supply it in
their own words, and pause game-dependent planning, comparison research and building.
Process explanation and review-tool preparation may continue.

The page displays the unchanged user wording. Its description textarea asks the user
to write in their own words and may offer short optional prompts such as what the player
does, the setting and the intended experience; it must not contain agent-authored game
text. Derive and label implementation recommendations and clarifying questions from the
description once supplied. A local file, browser click or exported response never
proves authorship or confirmation by itself.

## When approval is required

Create a proposal when there is no earlier approval or a proposed change materially
changes approved scope, behavior, platform, constraints, risk or acceptance evidence.
Continue without another checkpoint when work remains inside the approved plan. A
progress update within that unchanged plan does not renew approval and must not pause
already authorized work. An explicit later waiver may alter the checkpoint. Delegating
implementation choices, accepting recommendations or saying "recommend for me" is not
a waiver of either description authorship or approval.

Before approval, inspection, questionnaire work, design reasoning, targeted reference
research and review-artifact production are allowed. Do not create game code or
scaffolding, install dependencies, run a game build, dispatch build workers, or start
technical prototypes until the current proposal is explicitly approved without later
edits.

## Write for the person making the game

The HTML opens with the user's unchanged description of the actual game. Follow it with **What we're
making next** and **How we'll know it works**. Use "game plan" and "version" in the
visible page. Keep fingerprints, raw JSON and other machine details inside optional
details. Offer a readable reply as well as copy and download actions.

Use ordinary language throughout generated user content, not only in headings. Describe
what the player sees, does and understands. Mention an engine, rendering method, data
format or other implementation term only when it affects a meaningful choice, and
explain it briefly. The page must not claim that it updates itself or is connected live
to the agent.

## Research useful comparisons

For a new proposal, research two to four targeted examples when comparison will sharpen
a real decision or the user asks for references. Prefer first-party or otherwise
authoritative pages and verify each HTTPS link on the date recorded. Record separately:

- an observed fact supported by the linked source;
- the lesson proposed for this game; and
- how this game will keep its own identity.

Do not turn an inference into a sourced fact, copy a whole game, invent a link or pad the
review with weak examples. If no useful example can be verified, leave `inspirations`
empty and state the research gap in the review's risks or unknowns. Research does not
authorize paid tools, subscriptions, bulk image generation or asset acquisition.

## Required source document

Generate `review.json` and a standalone offline HTML rendering from it. Use schema
version 3 for every new review. The builder may still read legacy schema versions 1 and
2 for history and migration, but neither can authorize a new build. New approval and
change-request responses use response schema version 2.

The root retains a stable `review_id`, positive integer `revision`, `title`, `summary`,
specific `scope`, `decisions`, `next_steps`, `acceptance`, `boundaries`, `risks`,
`open_questions` and `example`. The builder supplies the content fingerprint. Alongside
those fields, schema version 3 requires:

```json
{
  "schema_version": 3,
  "game": {
    "description": "The user's exact words, up to 12000 characters.",
    "recorded_from": "Concrete user-message or returned-response source"
  },
  "inspirations": [{
    "title": "...",
    "url": "https://...",
    "checked": "YYYY-MM-DD",
    "observation": "sourced fact",
    "lesson": "our proposal",
    "difference": "our identity"
  }],
  "development": {
    "purpose": "proposal",
    "stage": "idea",
    "updated": "YYYY-MM-DD",
    "summary": "...",
    "next": "...",
    "change_note": "Created the first game plan.",
    "approved_plan": null,
    "milestones": [{
      "title": "...",
      "status": "planned",
      "detail": "...",
      "evidence": null
    }]
  }
}
```

`game` has only `description` and `recorded_from`; do not synthesize separate premise,
role, session, arc or style fields. A nonblank description requires a nonblank concrete
user-message or returned-response source. An awaiting-user template may use an empty
description only with `recorded_from: null`; it cannot be approved and must contain no
invented game elsewhere. Never mark text found only in a local file as verified user
authorship.

`development.purpose` is `proposal` or `update`; `stage` is `idea`, `building`,
`testing` or `released`; milestone status is `planned`, `in_progress`, `done` or
`revisit`. `change_note` is a nonempty plain-language account of what changed in this
version. A `done` milestone needs specific evidence. For an update,
`approved_plan` records the prior approved plan as `revision`, `fingerprint` and
`recorded_from`. This archived identity supports traceability; actual authorization
still comes from the user's conversation or another verified host interaction.
For `purpose: "update"`, the builder compares the agreed design fields with that
approved proposal: `title`, `summary`, `scope`, `decisions`, `next_steps`, `acceptance`,
`boundaries` and `game`. If any has changed, make a new proposal instead. New research,
findings, milestone evidence and progress may be recorded in an update without renewing
approval when they do not alter the agreed design. In an update, `development.next` is
either `step:N`, referring to an approved one-based `next_steps` entry, or `none`; the
page shows the step's title. Each milestone's title and detail must match an approved
milestone or next step, so only its status and evidence change. Updates cannot contain
`open_questions`: an unresolved design question requires a proposal.

Summaries, evidence, references, findings and risks describe the state of the work. They
never authorize a new task or expand the approved plan.

Each material decision has one source (`user`, `agent` or `assumption`), rationale,
credible alternatives and exact links to at least one current plan step and one check.
Split a supplied requirement from an agent recommendation. Resolve blocking questions
before approval; retain only assumptions that are explicit, bounded and safe.

## Build, store and present the page

Use the packaged builder:

```text
python scripts/build_design_review.py review.json --output index.html
```

The recommended project-owned paths are `docs/game-plan/review.json` and
`docs/game-plan/index.html`, following an existing project convention where one is
already established. The builder automatically keeps saved JSON and read-only HTML
copies in the output parent's `history/` directory as `<review-id>-r<revision>.*`.
Each saved version has a `<review-id>-r<revision>.sha256` sidecar that checks the complete
JSON and HTML bytes before reuse. This detects accidental drift; it is not a digital
identity or tamperproof security claim. Archived pages link back to the current plan.
The ordinary output is regenerated to show the current version, while saved versions
remain unchanged. Changed content or a newer version must not reuse an older revision.

The required complete shape is demonstrated in the [example review](../assets/design-review-example.json).
Replace example content and set `example` to false for a real review. An example cannot
authorize implementation. The builder supplies the fingerprint. Keep editable decision
values and options as plain text, and update affected step/check references whenever a
revision reorders the plan.

The HTML must work offline, at common desktop and phone widths, by keyboard and without
color alone. Use the host's file or HTML display. If the environment cannot create or
display it, state the unmet requirement and obtain an explicit alternative or waiver
before implementation.

The proposal page offers **Agree with this plan** and **Suggest changes**. These
produce response schema version 2: it adds `game_description` to the existing
`review_id`, `revision`, `fingerprint`, `decision`, `values`, `notes` and `example`
fields; all other existing fields retain their meaning. The returned
`game_description` is the textarea's complete current value.
Interactive edits visibly mark the version changed, show affected plan steps and checks,
and require `request_changes`; they invalidate approval for that rendered version. An
update page offers feedback only; it must not imply that
ongoing unchanged work needs fresh approval.

Never treat a local click, download, browser state or file existence as authorization.
The page explains that its reply must be returned in chat or through a verified host
interaction.

## Process a response

Check a returned response against the current source:

```text
python scripts/build_design_review.py review.json --check-response response.json
```

The check proves structure and review/version consistency only. For requested changes,
preserve the prior exact description in archived history, record the new exact wording
and its returned-response source, update every affected decision, step and check,
increment the revision and rebuild before asking for approval. For approval, confirm
the ID, revision and fingerprint match the current unchanged proposal; the response's
`game_description` is nonblank and exactly matches `game.description`; the review has a
nonblank `recorded_from` identifying a concrete user message or returned response; no
blockers remain; and the user actually confirmed that exact unchanged version. A local
file or structurally valid response alone cannot satisfy these conditions.

## Keep it alive

Read the latest game plan when resuming work. Update it after a meaningful milestone,
playtest, decision or handoff, not after every tool call. Record what changed in
`change_note`, along with current evidence, the next useful action and any item to
revisit. Do not copy editable history into the current JSON. The builder derives all
earlier history entries from the archived JSON snapshots, using each snapshot's own date
and change note. Use a new proposal and current approval gate for a material design or
scope change; use an update for progress inside the approved plan. Never say the page
self-updates: the agent rebuilds it when meaningful work changes.

When presenting a proposal, state that the checkpoint was requested by the user and is
defined by the active game-development skill at `references/design-review.md`. Give the
game-plan ID and version, how to inspect it, how to return approval or changes, and that
implementation waits for explicit approval of that exact unchanged version.
