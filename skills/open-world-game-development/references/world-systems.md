# World systems

Read this when the work changes traversal, scale, streaming, persistent entities,
simulation distance or runtime budgets.

## Scale and density

Treat scale as experienced time between decisions, not map area. Record the relevant
travel speeds and typical time between a landmark, hazard, resource, encounter or
route choice. Sample at least an ordinary route, a quiet route and a dense location.
Keep empty space when anticipation, orientation or contrast gives it a purpose.

Use one declared conversion for world units, display distance and simulation time.
If travel is compressed, specify where the factor changes and what remains invariant.
A counterexample is a huge map that crosses quickly but presents the same encounter
cadence everywhere: its dimensions do not prove scale or variety.

Traversal modes should change a relevant choice such as access, exposure, speed,
noise, cost or carrying capacity. A faster mode that only shortens a timer may still
be useful, but does not by itself deepen traversal. Automated travel needs explicit
arrival and safety handback rules; it must use the same passability constraints as
manual movement.

For delegated travel, make arrival, danger and handback understandable. Optional
activities can provide information, expression, preparation or skill without making
competent automation require repeated clicks. Compare attentive and unattended play
before claiming either meaningful activity or reliable delegation.

For bases, vehicles and interiors, define whether the surrounding world continues,
pauses or advances abstractly. Keep location, time, hazards and state consistent across
entry and exit. Inspect transitions and usable interior space at representative
sizes; a room count or exterior model does not establish a playable interior.

## Near, far and offscreen simulation

Define tiers by responsibility rather than draw distance:

| Tier | Keep authoritative | May simplify |
|---|---|---|
| Near | identity, position, condition, intent, collisions and visible actions | distant planning and inactive animation |
| Far | identity, coarse position, route, inventory, condition and scheduled outcomes | animation, fine steering and frequent sensing |
| Offscreen | identity, ownership, durable state, elapsed-time policy and pending events | continuous position and presentation |

Promotion and demotion must be explicit transformations. Compare the same declared
time near and far. Both must preserve invariants and causally valid transitions: no
created finite resources, impossible injuries, resurrected removals, lost ownership or
fabricated quest outcomes. Require identical results only when the design promises
deterministic equivalence; otherwise compare distributions and player-visible bounds.
Coarse simulation need not reproduce animation or centimetre-level positions.

Decide whether offscreen time advances while the game is closed. Either policy is
valid; mixing wall time and active time accidentally is not. Clamp or chunk large
deltas so a suspended frame cannot skip acquisition delays, cooldowns or safety
checks.

## Entity lifecycle and streaming

Give persistent entities stable IDs. Keep creation, live state, dormant state and
terminal records distinct. A terminal record or tombstone should prevent a collected
cache, defeated boss or purchased property from respawning when its cell streams in.

Exercise these transitions:

1. create → stream out → stream in;
2. mutate finite state → stream out → reload → stream in;
3. remove or transfer ownership → reload near the former location;
4. save during an in-progress pursuit, delivery, construction or world event;
5. cross a region seam by the shortest valid spatial relation.

Reject save rows with invalid IDs, non-finite coordinates, impossible quantities or
unknown closed-state values. Bound retained rows and histories. Preserve raw authored
or evidential inputs when normalisation would destroy meaning.

Treat asynchronous arrival or restoration as a barrier across gameplay actions,
advancement and saves that depend on the affected session, while cancellation and
unrelated UI or server work remain responsive. Restore authoritative state and required
destination data before releasing it; reject callbacks from replaced worlds or connections. When an authority
can reset the entire world, distinguish state generations so old memory cannot save
itself over a new world. Test replacement during load, not only eventual arrival.

Where version compatibility is promised, migrate supported older saves explicitly
and refuse unsupported future formats without overwriting them. A deliberate new-game
reset policy is different and should remain explicit.

For source-backed world data published with manifests or transforms, consume one
complete validated generation. Individually valid files can still form an invalid
mixture of old geometry and new metadata. Use atomic publication and interruption
recovery where such a mixture would corrupt authoritative output; a small static
asset need not acquire a publication service.

## Engineering boundaries and delivery

Give each durable fact one authoritative owner. Keep calculations and state
transitions pure or otherwise directly testable where the engine permits, and put
scene objects, engine callbacks, storage and network I/O at explicit boundaries.
Follow the engine's established component, scene and lifecycle idioms; do not build a
universal abstraction merely to make unlike engines look alike.

Declare the source of truth for authored and generated world data. For committed,
reproducible generated code/data, use one generation path and make the canonical
verifier regenerate and compare it. For stochastic media, retain provenance and the
accepted artifact instead of claiming byte-reproducibility. Check expected paths and
that ordinary play uses the verified code. Pin the
engine, exporter, importer and package versions that affect reproducibility, and keep
their lockfiles where the ecosystem supports them.

Read configuration through one validated boundary. Reject invalid units, paths,
ports, seeds, schema versions and incompatible feature combinations before play
begins. Surface failures with enough context to act on them. Support cancellation and
cleanup for loads, exports and network work; retry only transient, idempotent work
with bounded attempts. Apply the lifecycle, save-migration and interrupted-publication
rules above rather than inventing a second recovery model.

Protect real-player saves during development, migration and release checks: use
copies or disposable profiles, preserve unsupported data, and prove recovery before
overwriting. If multiplayer is present, define which process is authoritative for
each durable fact and reject stale, duplicated or unauthorised commits across reconnects
and world-generation changes. A standalone game need not acquire a network stack.

Unless the project sets a different convention, use 300 logical lines as a configurable
default and check for new handwritten source files. Split by coherent responsibility.
Allow justified exceptions for conventional engine structures and generated, vendored,
schema or data files; do not split scenes or data arbitrarily to satisfy a count.

Retain the build identity, verification result and relevant runtime evidence for a
release candidate. Exercise the delivered artifact's ordinary entry and critical
world journey when packaging can change behaviour. Publishing, deployment and other
external mutations require the authority already granted for them.

## Budgets, LOD and readability

Set budgets for the representative load: frame time, draw calls, active AI, dormant
records, memory, streaming latency and save size. Measure the bottleneck on the target
platform before adding a new scheduler or data structure.

LOD may simplify mesh, animation, sensing frequency or path detail. It should not
silently alter authoritative damage, stock, faction, quest eligibility or navigable
topology. If gameplay intentionally changes with distance, expose and test that rule.

Inspect transitions in motion and from the player's normal camera. Look for popping,
disappearing landmarks, unreadable silhouettes, late hazards and labels that imply
precision the simulation does not provide. A stable frame rate and a screenshot hash
cannot establish readability.

## Focused counterexamples

- A despawned entity reloads with full stock after a partial purchase.
- A far-simulated pursuer teleports through an impassable boundary on promotion.
- Fast travel advances one resource but not another governed by the same clock.
- Reducing visual LOD changes collision or quest reachability.
- Saving beside a cell boundary duplicates a reward on reload.
