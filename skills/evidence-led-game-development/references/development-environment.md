# Use the development environment as evidence

Discover the actual project and session before choosing a workflow. Read the project's
instructions, manifests, lockfiles and nearby documentation; inspect its existing engine,
editor conventions, scripts, test layout and release artifacts. Check which filesystem,
shell, browser, native-app, media, connector, skill and delegation capabilities are truly
available. Treat names in this guide as categories, not assumed tools.

Preserve the user's stack and normal entry points. Prefer an existing project command,
engine facility or maintained script over installing a dependency or building a new
harness. Do not introduce bespoke automation merely to standardise a reversible task.
Record material version, platform or device constraints when they affect the result.

## Match the tool to the claim

Choose the smallest available method that observes the claimed behaviour:

- Inspect source and configuration to establish ownership, wiring and static constraints.
- Edit through the environment's supported file operations, preserving unrelated work and
  generated-file rules. Use the project's formatter only where it owns the changed files.
- Run the established type, lint, build and test commands that cover the change. Inspect
  what each command exercised; a green command proves only its own assertions.
- Drive ordinary player input in the production runtime when input routing, camera,
  timing, physics, UI, persistence or scene transitions are part of the claim. Use the
  target editor, device, native runtime or browser according to the project, and do not
  assume any one driver is present.
- Inspect actual visual output at representative resolution, camera and game state for
  hierarchy, legibility, animation and feedback. Inspect or listen to actual audio for
  timing, balance and cues. Screenshots cannot prove motion, sound or control feel.
- Measure performance in representative play on the declared target when performance is
  claimed. Capture frame times or spikes, scene load and cold/warm conditions as relevant;
  build success and average frame rate are insufficient substitutes.
- Test the exact packaged or generated artifact when delivery, freshness or runtime parity
  is claimed. Verify it came from the current source, excludes forbidden development
  capabilities where relevant, and completes the intended player action through its
  ordinary entry point.

If the chosen tool observes a proxy, narrow the verdict or choose another tool. Prefer a
direct runtime probe over adding layers around an unproved mechanism.

## Create controlled evidence

Use project-supported seams to control clock, randomness and starting state when they
materially isolate the claim. Record seeds, injected state, time scale, simulated time and
wall time. Compare relevant seeds, timesteps, save/resume points or bad states rather than
claiming generality from one favourable run. Keep fixtures out of ordinary builds unless
the product deliberately exposes them.

For qualitative behavior, retain the actual output and assess it against named criteria.
For deterministic behavior, add or run focused assertions with a counterexample that
would fail under a plausible broken implementation. Do not infer quality from hashes,
schema validity, logged calls or successful capture alone.

## Use optional capabilities deliberately

Available skills, connectors, asset sources and external services may help when they fit
the brief and authorization. Read their instructions, confirm scope and provenance, and
use only what the project permits. A skill or connector does not authorize publication,
deployment, purchases, messages, account changes, licensing assumptions or collection of
new player data. Avoid paid or remote tooling when it was not authorized or when an
existing local path answers the claim.

Delegate only separable work that benefits from parallel attention and only when the
environment permits it. Give each worker owned files or artifacts, a stable interface and
a concrete acceptance example; keep one coordinator responsible for integration and the
player-facing verdict. Do not hard-code a model, provider, agent API or delegation pattern
into a platform-independent workflow.

## Handle environment limits honestly

Tooling unavailable in the current session is not a product defect. First seek an
equivalent existing project path or lower-layer check. If none can establish the claim,
report the untested condition and the exact editor, browser, device, audio output, account
or human playtest still required. Likewise, distinguish a harness failure from a runtime
failure with the smallest discriminating check before changing product code.

Run only the checks proportionate to the change. Do not make screenshots, browser runs,
subagents, asset searches, packaging or full-suite verification universal requirements.
Do not deploy, publish, commit, push or mutate live services unless the user or an existing
authorized project workflow expressly includes that action.
