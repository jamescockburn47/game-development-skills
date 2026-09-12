# Evidence record

Use this template for a substantial assessment. Omit sections that do not serve the claim.

```markdown
# <Feature or journey> — evidence record

Date / revision:
Scope and consequence tier:
Critical player journey:
Verdict: pass | partial pass | fail

## Claim and acceptance

- Intended behavior:
- Credible failure:
- Pass condition:
- Counterexample the checks must reject:

## Method

- Production path exercised:
- Deterministic core or controlled comparison:
- Clock, seed, timestep, and acceleration:
- Injected fixtures or granted state:
- Visual states inspected:
- Commands and environment:
- Evidence type: design intention / inspected source / test present / recorded run / fresh reproduction:
- Lineage: active implementation, historical copy, fork, shared code or dataset; what was independently revalidated:
- Expected checks versus those actually run; delivered artifact and production entry:

## Results

| Probe | Measurement or observation | Result |
|---|---|---|
| | | |

Separate:
- Measured behavior:
- Source-confirmed mechanism:
- Design judgment:

## Decision

- What works and should be preserved:
- Material failure and player consequence:
- Smallest supported revision:
- Result after one revision and rerun:
- Dependent work or claims invalidated or superseded by a failed central result:

## Limits and durable evidence

- Questions this evidence does not answer:
- Human playtest still needed:
- Raw output, screenshots, reports, and test paths:
- Canonical verification result:
```

Do not average conflicting runs away. Keep them separately attributed and explain which changed condition can account for the difference. A partial pass states both the working mechanism and the unmet intended capability.

Copied policies, forks and shared fixtures do not become independent corroboration merely by appearing in different projects. Preserve their lineage and distinguish reuse from a new validation on the changed engine, scale, camera or behavior.
