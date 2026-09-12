# Probe methods

Use only the sections needed for the current claim.

## Deterministic core

Control clock and randomness when relevant. Compare fine and coarse timesteps where elapsed-time equivalence matters. For persistent systems, save midway and resume to test state equivalence. Check conservation across relevant sources and sinks, idempotency across retries, bounded effects and recovery from failed states. Do not impose these mechanisms on a game that does not contain them.

Mutation or counterexample cases should fail for the right reason. Useful examples include duplicate rewards, unavailable clues accepted by a puzzle, spending more stock than exists, a tactical choice with no promised effect, and an objective reported complete for the wrong subject.

## Real first-use path

Start where a player starts. Use production input and the actual runtime, physics, UI and persistence for claims they can affect. Choose native, device, editor or browser tools that match the target. Record relevant state transitions and stop on an unexpected blocker. Do not patch around the blocker and still call the journey complete.

Direct state injection may create a controlled setup after entry. Record every injected field and use the setup only for the claim it isolates. It cannot prove acquisition, onboarding, or natural frequency.

When a bot drives ordinary controls, distinguish its competence from the game's mechanics. Log the actual interaction preconditions: orientation, relative velocity, overlap, timing windows or sustained input may matter as much as proximity. Prove the uncertain action in a disclosed local experiment before spending another whole-session run on it; the isolated result still does not prove natural acquisition or completion. Retain failed traces and reject the wrong objective even if its reward or animation looks successful.

## Pacing and acceleration

Fixed-step acceleration can establish game-time rates, deterministic outcomes, and the order of events. It does not establish felt waiting, attention, delight, fatigue, or acceptable wall-clock duration. For those claims, observe a human-speed segment or label the remaining question for human playtest.

Report both simulated duration and elapsed wall time when useful. Keep pause states, loss of focus, menus, speed multipliers and fictional clocks explicit. For turn-based games, distinguish turn count, decision time and animation time.

For real-time mechanics, compare equal elapsed time under different frame budgets. Movement, cooldowns and resource rates must follow the declared clock, not accidentally the number of rendered frames. A frame-rate cap does not establish that independence. Distinguish a simulated update-count fixture from an actual target-device frame-rate measurement.

## Controlled comparisons and setbacks

Hold relevant conditions constant: seed, starting state, opponent behavior, input sequence, difficulty and duration. Change one decision or capability: defensive versus aggressive play, an early hint versus an unexplained rule, one upgrade versus another, sufficient versus exhausted stock. Compare intended player-visible outcomes, not invocation counts. Mechanical equivalence is not a defect in a choice intended only for expression.

Exercise a credible bad state where relevant: an unsolved puzzle, missed objective, exhausted resource, lost ally, full inventory, interrupted save or unavailable service. Distinguish intentional defeat from accidental dead ends. A designed retry, undo, checkpoint or lasting consequence should behave as communicated and should not duplicate rewards.

## Visual and interaction evidence

Render representative states at the viewport and camera players receive. Inspect framing, occlusion, hierarchy, contrast, readable labels, actionable feedback, and whether visual differences reflect real state. Compare before/after or alternative states under the same camera when possible.

Reject these proxy conclusions:

- a button exists, therefore the action is useful;
- a value changes, therefore the choice is consequential;
- an ally acted, therefore support helped;
- a screenshot was captured, therefore the scene reads well;
- a constant is declared, therefore runtime output uses it;
- a gate is green, therefore it covers the new journey.

## Integration and review

For changes crossing rules, runtime, save, UI, and world simulation, identify one coordinator contract and exercise it end to end. Keep pure arithmetic below the integration layer. Fresh review should inspect actual code and artifacts, reproduce material claims, and distinguish defects from test-harness mistakes.

Check the verification set as well as its result: which required checks ran, which were skipped or absent, and which implementation the player entry actually invokes. A dynamically discovered suite can stay green after a required file disappears. Enforce an expected inventory when completeness is part of the gate's promise; do not require a universal suite for a prototype.

When players receive a generated, offline or packaged artifact, prove its freshness against the source and test that exact artifact through the relevant player action. Development-page success is not delivery evidence. Validate the actual consumer when claiming parity across runtimes; comparing a producer with its own transcription is insufficient.

If automation adds privileged state arrangers or command bridges, bound their commands and restrict their build/profile exposure. Verify ordinary release artifacts exclude test-only capabilities, include a known forbidden artifact as a rejection case, and smoke-test the ordinary runtime without the bridge. Text-marker scans alone cannot establish semantic isolation. Intentional live admin features need their own authorization checks; external ordinary-input automation may need no bridge.

## Input transitions and restoration

When a surface shares tap, drag, pinch, selection or mode changes, test their boundaries: small jitter, adding or releasing a pointer, cancellation and the next action after a transition. Separate gesture tests and still screenshots can miss an accidental selection on release.

When restore or world replacement is asynchronous, hold gameplay actions, advancement and writes that depend on the affected session until authoritative state and required destination data are ready. Keep cancellation and unrelated UI or server work responsive. Bind callbacks to the session that created them and reject stale completions. Probe switching sessions during load and saving before restore; a final welcome screen alone cannot establish that existing progress was preserved. A synchronous disposable game need not acquire this machinery.

Where saves must survive application versions, test ordered migrations from supported older formats and refusal of unsupported future formats without overwriting them. A current-version round trip does not cover either. Follow explicit reset or downgrade policies when the product calls for them.

## Target-device performance and feel

Measure representative play on declared hardware, including input response and frame-time spikes where they matter. Report warm versus cold starts, scene complexity and target budgets. An average frame rate can hide stutter; an unloaded test scene cannot establish performance in busy play. Human trials are needed for comprehension and feel, with player familiarity and assistance disclosed. If only headless or accelerated evidence is available, limit the verdict accordingly.
