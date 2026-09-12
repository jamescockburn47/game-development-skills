# From player experience to a playable build

## Start from the user's words

The game description is user-authored input, not an agent deliverable. Carry its exact
wording and concrete user-message or returned-response source into the game plan. Do not
summarize it into a new creative premise, complete missing ideas, or let a request to
recommend defaults stand in for it. When it is absent, stop game-dependent design,
comparison research and implementation and ask the user for the description in their
own words. Process explanation may continue while that answer is pending.

Derive the player verbs, implementation recommendations and checks below from the
actual description, label agent recommendations, and ask focused clarifying questions
where the text leaves a material choice open. If the user revises the description,
preserve the earlier version in plan history and update affected design work for a new
approval.

## Choose the representative experience

Translate the brief into player verbs, feedback and consequences. State what the player must learn or perceive, what makes the action satisfying, and what can go wrong. Preserve the game's genre and tone: a meditative toy, deduction puzzle and competitive action game need different success criteria.

Describe the actual session structure. A puzzle may end in an insight, an arcade round in a score and retry, a narrative scene in a changed relationship, and a sandbox in a player-chosen stopping point. Use the game's structure instead of imposing an expedition, economy, quest or progression ladder.

For a new build, settle only choices needed for the next slice: target input and platform, engine constraints, camera, art direction, content or asset policy, and any necessary persistence or networking. Follow an existing stack unless a demonstrated limitation justifies a change. Do not inherit another project's procedural-only or browser-only rules. Apply the current project's source-size policy or the configurable default in [engineering hygiene](engineering-hygiene.md#keep-ownership-and-code-boundaries-clear).

When the brief promises historical, scientific or cultural accuracy, verify the facts that constrain a mechanic before expanding it. Separate sourced facts, deliberate fictional departures and unverified assumptions; a setting claim is not established by an attractive implementation.

Research two to four targeted examples when the user requests references or comparison
will help settle a material design choice. Prefer verified official sources. In the game
plan, keep what the source actually shows separate from the lesson proposed for this
game, and say how the game remains its own work. If nothing useful can be verified,
record the gap rather than inventing a link. Do not generate batches of reference images
or use paid tools unless the user separately authorizes that work.

## Test the mechanism with a small complete slice

Prepare the [interactive game plan](design-review.md) before implementing the
slice or a technical prototype. The proposed experiment and acceptance evidence are
part of that review. Proceed with game-building work only after its approval, or an
explicit later waiver; creating the review itself is authorized discovery work.

Choose a slice small enough to revise but representative enough to reject a bad idea. Examples include one puzzle with a wrong path and reset, one combat encounter with readable telegraphs, one rhythm phrase with input and audio timing, or one dialogue branch whose consequence can be observed.

Name the hardest assumption. A rhythm prototype that scores from an internal clock without measuring what the player hears and presses has not proved timing. A puzzle solver reaching a valid state has not proved that a human can infer the rule. A random reward increase has not proved that an upgrade changes strategy.

Include enough real presentation to judge the mechanism. For movement and action, camera motion, hit feedback, input buffering, animation and sound may be part of the first experiment. For deduction, clue order and wording may matter more than rendering detail. Further polish and content should build on a working slice.

## Give presentation a testable purpose

Choose a coherent visual language: silhouette, value hierarchy, palette, typography, motion and camera behavior appropriate to the game. Make critical affordances distinguishable from decoration. Inspect representative gameplay at the actual resolution and camera, including busy states, menus and transitions. Attractive promotional framing is not a substitute for the normal player view.

Match the accessibility check to the interaction: contrast and non-color cues, readable text, remapping, reduced motion, audio alternatives or timing options where relevant. Do not certify sound, touch, latency or control feel from screenshots. If the environment cannot reproduce them, record the remaining target-device or human check.

## Implement with clear ownership

Prefer testable domain rules where practical and runtime adapters for engine, I/O and side effects. Keep UI, physics and authoritative state in agreement; a displayed collision shape, inventory amount or cooldown must represent the rule the player encounters. Use existing engine patterns instead of adding abstraction for its own sake.

For persistent state, rewards or resources, identify the owner, sources, sinks and transaction boundaries. Inject clock, randomness or external dependencies where it makes a meaningful check possible. For online play, define authority and synchronization only when networking is in scope; do not turn a local prototype into a service project.

When optional generated dialogue or a remote assistant presents instructions, readings or command results, keep essential feedback available through a deterministic path. Ground its statements in current validated state. A model may choose or propose actions if the design calls for that, but execution and confirmation come from the authoritative runtime. Test outage and missing-context behavior. Cosmetic conversation need not have a duplicate canned script; a product whose core requires a service should disclose and handle that dependency rather than pretend it completed the action offline.

Delegate independently useful slices with explicit file ownership, shared interfaces, representative states and acceptance examples. Keep one coordinator responsible for integration and final experience. Ask reviewers to inspect the artifacts and relevant runtime paths, not merely the implementation summary.

## Expand only along a supported arc

Where progression belongs, state what changes over the game: the rules a player combines, expressive possibilities, strategic responsibility, relationships or stakes. More levels, higher health or additional menus alone do not establish variety. Teach before demanding mastery unless discovering the rule is itself the intended challenge.

Track which behavior is implemented, which is proposed and which has been tested. Use a representative early experience and a later combination of systems to challenge the arc; neither proves a whole campaign. Respect the authorized milestone and use the existing build, test and release workflow without inventing an additional process.

Treat the game plan as a living handoff, not a claim that the HTML changes by itself.
Read its latest version when resuming work. Rebuild it after a meaningful milestone,
playtest, decision or handoff, carrying forward the approved plan identity and adding
specific evidence before calling work done. A progress update inside unchanged approved
scope does not seek approval again. A material change to the design or scope becomes a
new proposal and returns to the approval checkpoint.
