---
name: minimal-change
description: Implement features, fixes, or refactors with the least complexity that fully meets the request. Use for coding work, especially simplifying a proposed solution or avoiding overengineering. Excludes standalone reviews, dependency audits, and documentation workflows.
---

# Minimal change

## Choose the solution

- Establish the requested behavior and constraints. Remove speculative scope from the design, not requirements from the task.
- Inspect the affected path and relevant callers before choosing a fix. Search for existing helpers, components, and established patterns.
- Look first for existing project behavior, configuration, code, platform capabilities, and suitable installed dependencies. Reuse them when they fit; improve the design when reuse would preserve a concrete architectural problem.
- Add a dependency only when it removes meaningful implementation or maintenance burden. Compare that benefit with its integration cost.
- Introduce an abstraction when it expresses a domain concept, gives a shared rule one owner, or separates concerns that change independently. Require a concrete need for options and extension points; avoid coupling unrelated behavior just to remove repetition.

## Make the complete change

- Fix a shared cause at the appropriate layer; avoid patching each symptom or changing unrelated code.
- Follow local architecture guidance and preserve public contracts unless the request requires changing them. Improve responsibilities and boundaries within the affected scope when the benefit justifies the migration. Update affected callers, types, configuration, and fixtures together.
- Minimize the complexity of the resulting system, not just the diff. Prefer readable, direct code over fewer lines. Remove code made obsolete by the change when its uses have been checked.
- Preserve input validation, meaningful error handling, security, accessibility, and required performance. State any material limitation; do not silently narrow the request.

## Verify

- Run the project's required checks and verification relevant to the affected behavior.
- For a bug fix or meaningful new logic, add or update a focused behavioral test when practical. Cover the failure or boundary that matters; avoid tests that merely mirror the implementation.
- Review the diff for unnecessary scope and incomplete integration. Stop once the request is satisfied and relevant checks pass; report any verification gap.

Inspired by [Ponytail](https://github.com/DietrichGebert/ponytail).
