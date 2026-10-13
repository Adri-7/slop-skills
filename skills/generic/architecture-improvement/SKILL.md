---
name: architecture-improvement
description: Choose and incrementally improve software architecture when requested or when feature work exposes misplaced responsibilities, inconsistent rules, or costly coupling. Covers design and implementation trade-offs; excludes ADR authoring and unrelated repository-wide cleanup.
---

# Architecture improvement

## Find the design pressure

- Inspect the relevant flow, module boundaries, dependencies, and tests. Check applicable architecture guidance and existing decisions before proposing a direction.
- Identify concrete friction: a rule maintained in several places, changes spreading across unrelated modules, unclear ownership, dependency cycles, or a boundary that makes behavior difficult to test.
- Separate observed problems from anticipated needs. Base anticipated needs on known requirements or change patterns; name assumptions that affect the choice.

## Choose a useful design

- Compare the current structure with the smallest structural improvement that addresses the friction. Consider ownership, dependency direction, clarity, testability, and migration cost. Explain the determining trade-off briefly.
- Introduce an abstraction when it gives an invariant one owner, expresses a domain concept, separates independently changing concerns, or isolates an external dependency. Duplication is evidence, not a prerequisite.
- Group behavior that changes for the same reason. Keep distinct concepts separate even when their implementations look alike; avoid generic helpers with flags for unrelated cases.
- Prefer explicit boundaries and narrow contracts. Add layers, interfaces, or patterns only when they solve the identified problem; evaluate them against the project's stack and scale.
- Judge simplicity by the code a maintainer must understand and change, not by diff size. A larger refactor can be simpler overall when it removes repeated work or hidden coupling.

## Improve incrementally

- During implementation, improve the affected design when the benefit is clear and the migration fits the task. Preserve behavior and public contracts unless the requested change requires otherwise.
- Make each migration step leave the system usable. Move responsibilities and their callers together; remove replaced paths once their uses are accounted for. Temporary adapters need a concrete removal condition.
- Keep broader redesigns separate when they change product behavior, public contracts, or exceed the authorized scope. Describe the proposed boundary and benefit so that the next step is reviewable.
- Preserve security, validation, error handling, and performance constraints through the migration. Update guidance made inaccurate by the new structure; record lasting, non-obvious decisions using local ADR conventions when warranted.

## Check the outcome

- Verify behavior across affected callers and boundaries using relevant tests and required project checks.
- Revisit the original friction: confirm that ownership is clearer or changes require less coordination. Remove abstractions that merely relocate complexity.
- Stop when the identified problem is resolved. Report the chosen trade-off, verification, and any remaining migration work; do not turn continuous improvement into continuous scope growth.
