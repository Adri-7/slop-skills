---
name: minimal-change
description: "Simplify an implementation or make a behavior-preserving refactor. Also use for coding work when a proposed fix or feature adds avoidable complexity."
---

# Minimal change

- Establish the behavior and constraints that must hold. Trace the affected callers and look for an existing project or platform capability that can carry the change.
- Before a refactor that risks changing a contract, capture current behavior with a focused existing test or a reproducible baseline. Run the same check after the refactor.
- Choose the simplest complete implementation a maintainer can follow. Add abstractions, dependencies, or extension points when they remove a concrete maintenance burden. Keep separate concepts independent even when their implementations look similar.
- Put the change where the affected behavior belongs. Update callers and related data together, preserve contracts outside scope, and remove obsolete paths after checking their uses.
- Review the diff for missing integration and unrelated changes. Verify the affected behavior and required project checks, and report verification gaps.

Inspired by [Ponytail](https://github.com/DietrichGebert/ponytail).
