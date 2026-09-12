# Engineering hygiene for games

Apply the relevant sections to implementation, stored state and delivery. Follow the
current project's policy, engine conventions and explicit user choices. The agent
owns engineering classification; ask the user only for a material product consequence
or owner decision that cannot be established from context. Do not make the game
questionnaire require choices of architecture, test runner or process terminology.

## Classify by consequence and bound the work

Before substantial work, state the critical player journey, credible failure and
proof needed. Use the project's risk scheme, or these fallback levels:

| Level | Typical consequence | Appropriate assurance |
|---|---|---|
| Prototype | Disposable learning build with no sensitive or irreplaceable state | Label the scope; prove the hardest mechanism with minimal checks and a playable example. |
| Reversible/supporting | Styling, local tools, documents or isolated reversible refactors | Small change, focused checks and relevant output inspection; no automatic review swarm. |
| Durable product | Ordinary player flows, recoverable progress, integrations or recurring work | Focused regressions and needed integration evidence; one fresh review for multi-module or release changes. |
| Critical | Account security/authorization, secrets, real money, destructive migration, loss of irreplaceable progress or irreversible public effects | Deterministic enforcement, regression tests, fresh independent review and an appropriate authorized end-to-end probe; preserve recovery. |

A prototype label does not lower a concrete account-security, real-money or data-loss consequence.
Escalate from evidence, not hypothetical additions to the game. For noncritical work,
normally stop after implementation, one review and one evidence-led fix/recheck.
If support code exceeds the feature or checks no longer reduce material uncertainty,
reassess reuse, deletion or deferral. An unresolved central requirement still blocks
its dependent expansion; do not quietly reduce the promised outcome to finish.

## Keep ownership and code boundaries clear

Give each important state transition one authoritative owner. Separate rules from
rendering, input, persistence and networking where that improves testing or design;
use engine scenes/components/events when they are the appropriate boundary. Avoid
recreating the engine or introducing an entity framework for an isolated mechanic.
Inject mutable clock, randomness, storage or services when a meaningful test needs it.
Remove dead code, choose clear names and preserve unrelated working changes.

Unless the project sets a different convention, use **300 logical lines as the
default limit for new handwritten source files**. Split by coherent responsibility,
not arbitrary fragments. Record justified exceptions for generated/vendor code,
schemas/data, snapshots and conventional engine or single-file structures that are
clearer intact. In a maintained project, enforce the adopted rule with the existing
linter/verifier or a small check; define its counting convention and exception list.
Do not split a legacy engine file wholesale to land an unrelated fix, or create a
cross-platform analysis framework solely to count lines.

Keep configuration at a clear boundary: read environment and external settings there,
validate types, ranges and required values at startup and on relevant runtime changes,
then pass validated settings to consumers. Distinguish intentional player tuning
from scattered reads and silent fallback to a different simulation configuration.

## Preserve progress and handle failure explicitly

Validate untrusted saves, network commands and imported content at their boundaries.
Keep the last known-good save intact when validation or migration fails. Where progress
must survive versions, test supported older formats, refusal of unknown newer formats,
interruption, and restoration from the actual recovery copy. Prefer the platform's
atomic-write/transaction facility or a small equivalent appropriate to storage.
Do not replace damaged or incompatible real-user data with an empty game silently.
An explicit disposable-save/reset policy remains valid within its authorized scope.

Handle or propagate errors with useful, redacted context. A failed save, rejected
action or missing required resource must not appear successful. Use cancellation,
timeouts and cleanup where work can hang or outlive its scene/session; reject stale
callbacks. Retry only demonstrated transient and idempotent operations, with bounded
attempts/backoff. Test double input, overlapping writes and disconnect/reconnect when
they affect the changed feature. The detailed probes live in
[probe methods](probe-methods.md#input-transitions-and-restoration).

For online or monetized games, validate consequential actions at the appropriate
authority rather than trusting client labels, counters or a model's assertion. Keep
secrets out of game clients, fixtures and logs; use established auth/payment facilities
and relevant dependency/secret scans where available. A solo offline game does not
need to acquire a server, telemetry or account system to satisfy this section.

## Make checks and builds reproducible

Keep one canonical local verification entry point for a maintained project; reuse it
in CI when CI fits the product. Do not duplicate its logic in a second pipeline or
impose cloud CI on a throwaway or deliberately local/confidential build. A prototype
may begin with one small repeatable command; record genuinely manual steps honestly.
Use focused checks during edits, then the relevant canonical gate before release.

Record/pin engine, runtime, dependency, import/export and automated-tool versions where
they affect reproduction. Preserve suitable lockfiles and pin CI actions where used;
avoid floating `latest` in automation. Keep setup, required device steps and configurable
development ports discoverable. Probe port availability instead of assuming a number
is permanently free. Avoid unrelated upgrades while repairing a game feature.

Edit the source of generated code/data and regenerate it. When reproducible generated
output is committed, the canonical gate regenerates and compares it. Authored or
stochastic media needs retained provenance, recipes and the accepted artifact; do not
claim a byte-reproducible generator when the pipeline cannot supply one. Disposable
build output remains outside source control unless the release workflow requires it.

Important guarantees need executable enforcement at the relevant layer: a schema,
type, assertion, test, hook or build gate. Include a plausible broken example that the
check rejects. Verify the expected tests actually ran and the normal player entry uses
the tested implementation. Do not silently weaken a failing gate or confuse a harness
fault with a product defect. Existing [probe methods](probe-methods.md#integration-and-review)
cover these evidence boundaries; do not generate an additional process around them.

## Keep delivery and project policy explicit

For a maintained deliverable, use one release path that runs the relevant verification
and identifies the exact artifact players receive. Exercise its actual entry and core
action. For consequential state changes, verify backup/restoration, migration
compatibility and rollback or roll-forward recovery as appropriate; code rollback
alone may not restore saved state. Release tools do not authorize publishing, deployment,
commits, pushes or changes to live services. Preserve existing user authorization.

Record durable project decisions in the existing policy/design location, with current
commands and justified exceptions; do not duplicate equivalent AGENTS.md/CLAUDE.md
rules or copy another project's private infrastructure. Keep a short evidence record
of what changed, what passed and what remains unverified. If model-generated behavior
is central, version its prompts/schema and evaluate representative produced outcomes;
valid output structure alone is insufficient. Scale this to the actual feature.
