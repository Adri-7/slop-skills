---
name: architecture-improvement
description: "Choose an architecture or resolve concrete design friction such as unclear ownership, scattered rules, dependency cycles, or hard-to-test boundaries."
---

# Architecture improvement

## Choose the design

- Trace the affected flow, owners, dependencies, and tests. Read applicable architecture decisions. Ground the design in observed friction or a known requirement.
- Identify who owns each invariant or state transition, what crosses each boundary, and which direction dependencies should flow. Compare the current design with the smallest structural change that addresses the problem. Explain the determining trade-off in terms of callers, testability, and migration cost.
- If a design choice hinges on an observable fact, use a small, disposable prototype in isolation to test that fact before committing to a design.

## Plan or make the transition

- For a design request, give the proposed boundaries, trade-off, and migration path.
- For multi-step migrations, test the riskiest assumption first and define the evidence needed to advance each step. During implementation, move responsibilities with their callers, keep each step usable, and give temporary adapters a removal condition.
- After implementation, exercise the affected contracts and check whether the original friction is resolved. Update stale architecture guidance and use the project's ADR convention when a lasting rationale needs recording.
