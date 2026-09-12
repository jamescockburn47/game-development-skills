# Progression and causality

Read this when the work connects AI, factions, economies, quests, exploration or
lasting world change.

## Give each consequence one owner

For each important outcome, name the system that commits it and the systems that
observe it. A useful event carries a stable event ID, subject ID, cause or actor,
location or context when relevant, and the committed outcome. Contribution and source
provenance belong in the event when credit depends on them.

For example, combat owns an actor's defeat; an encounter controller owns capture;
inventory owns the transferred goods; a quest may grant progress only after observing
the relevant committed event. A quest flag should not create the defeated actor or
the cargo it claims was delivered.

Check repeated and reordered delivery. A duplicate event must not mint rewards twice,
and a later observer must be able to reconstruct the result from durable state.

## Couple systems without hidden omniscience

AI should act from information available to its role: current perception, memory,
orders, faction knowledge or a declared strategic simulation. Separate knowing a
target exists from knowing its exact current position. When an entity changes tier,
carry the knowledge state as well as its physical state.

Faction reactions should follow attributable acts. Define who observed the act, which
authority records it, how reputation propagates, and how standing can recover. Avoid
global hostility from an unobserved local incident unless the fiction explicitly
provides that network.

When players choose sides, give each an understandable purpose and a viable game arc,
with distinct privileges, restrictions, income or opportunities and recovery options.
Show material pros and cons before commitment. Settlement or territory access must
agree with the actual interaction rules; contested shared spaces should communicate
why using them is risky. Symmetry of motivation need not mean identical mechanics.

For communication and support, distinguish sending, receipt, acceptance and arrival.
Use the world's stated information and transport rules. Nearby help, remote orders
and replenishment can have different availability, delays and finite costs; test the
actual assistance or delivered stock rather than a request animation.

Economies need conserved quantities where scarcity matters. Track stock source,
transfer, consumption and sink; make replenishment rules explicit. Prices can be
abstract, but buying, looting, crafting and delivery should not refer to separate
copies of the same goods. Test capacity, insufficient funds, partial acceptance,
duplicate transaction IDs and save/reload midway through a transfer.

When population, companions or vehicles change consumption, show the resulting
endurance and replenishment cost at the decision point. Test a funded ordinary trip
and a weakened state with a smaller opportunity, retreat or other intended recovery.
Use this only where logistics belongs; scarcity should create the intended decisions,
not an accidental downward spiral hidden behind recruitment or upgrade menus.

## Reassign embodied agents without double-counting them

When workers, companions or vehicles are themselves finite resources, distinguish
reservation, travel, work, cancellation, delivery, return and release as the design
requires. An agent carrying goods or returning from a task cannot become available
elsewhere merely because its job label changed. Bind partial work to the target's
identity and relevant state, and debit finite costs at one committed boundary.
Test retasking mid-journey, reused target IDs, interrupted delivery and save/reload.
Intentionally abstract labor pools may reassign instantly; do not add travel merely
to mimic an embodied model.

## Bind quests to actual subjects

Specify each objective as a condition over authoritative events and state. Bind it to
the intended entity, location, faction, source or route when an arbitrary substitute
would undermine the task. Include a rejection test: a different target of the same
type, a fabricated counter, an allied outcome without required contribution, or cargo
that was bought rather than recovered.

Define terminal failure and recovery for unique subjects. If the only courier is lost,
the quest should complete by an intended alternative, fail clearly and become
retryable, or replace the subject under an explicit rule. It should not remain active
with no satisfiable path.

Keep progression rewards separate from the proof that earned them. Recheck eligibility
at the mutation boundary for purchases, unlocks and world changes; a stale or optimistic
UI must not authorize the change.

For guaranteed progression-critical items, reconcile earned entitlement across
inventory, pending grants, live drops and legitimate containers before replacing
anything. A full inventory should retain an undelivered entitlement. Save the earning
transition before or atomically with its grant; retry and reload must neither lose
the debt nor duplicate the item. Account for legitimately consumed or crafted
successors. This is not an automatic replacement policy for deliberately scarce goods.

## Keep context prompts and committed actions in agreement

When targets or action modes overlap, use one read-only resolution rule for action
kind, exact target, label, highlight and relevant held state. Resolve again when input
arrives, then revalidate at the mutation boundary. Test occlusion, range, foreground
priority and a target moving between prompt and input. Preserve deliberate target
locking where promised; a static menu need not use a spatial resolver.

## Make exploration useful

Classify information by source and freshness: directly observed, inferred, reported,
remembered or globally known. Store enough provenance to explain why the map or journal
believes it. Decide what expires when the world moves.

A discovery should usually change a choice: reveal a safer pass, locate a seasonal
resource, identify a faction custom, narrow a search, or explain a systemic pattern.
Reject a discovery that only increments a total while leaving the player's decisions
unchanged, unless collection itself is the intended pleasure.

Support uncertainty honestly. A rumour can be approximate; a current sighting can be
precise; an old sighting should remain at its last known position until renewed.

## Connect local action to the world arc

Plan change at more than one horizon: immediate response, regional persistence and
longer arc. The world should retain a small number of legible consequences before it
simulates many invisible ones. Examples include a reopened route changing traders,
a restored facility changing local services, or a faction loss changing patrol
coverage.

Measure whether later play actually differs. A changed banner or completed counter
does not establish systemic change. Compare traffic, access, prices, threats,
opportunities or dialogue that reads the committed state.

## Focused counterexamples

- Defeating any creature completes a named-target objective.
- A UI button grants an upgrade after its eligibility became stale.
- Offscreen production creates goods without consuming inputs.
- A faction retaliates despite no witness or declared information path.
- A unique objective disappears but the quest remains active forever.
- A map marker tracks a moving target through lost sight without an information source.
