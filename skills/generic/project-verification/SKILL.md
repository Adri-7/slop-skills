---
name: project-verification
description: "Create or maintain project validation guidance, runnable checks, rules, and harnesses. Use to add a validation tool, enforce an invariant, or repair verification drift."
---

# Maintain project verification

Find the existing validation guide, runner, and CI. Use that guide or create a linked one when needed. Keep required baseline checks and conditional checks in one place, with the command, scope, prerequisites, and whether the result blocks acceptance. For a user journey, record the entry point, action, observable success, and any manual step or cleanup.

State the rule and a violation that should be caught. Prefer the smallest reliable deterministic check in the existing toolchain. For a concrete gap in that toolchain, use the [check integration guide](references/adding-checks.md) to evaluate and integrate a tool. When the rule requires judgment, put a short project-wide constraint in `AGENTS.md`, scoped detail in local guidance, or a repeatable procedure in a skill. Keep one source for the rule.

Prove each new or changed automated control catches a representative violation and accepts valid behavior. Exercise a representative journey when adding instructions for one. Compare with the existing repository before making a new control blocking. During upkeep, rerun the affected cases after changes. Fix stale checks and remove controls superseded by equivalent coverage. Report product regressions against the expected behavior and state which checks could not run.
