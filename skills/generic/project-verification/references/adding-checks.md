# Add a validation check

- Match the tool to the property. Use a test for an observable behavior, a static rule for a source pattern, and a model checker for meaningful interleavings or state transitions.
- Keep rules, models, and their test cases with the project. Expose a stable command through the existing runner or CI conventions.
- Before adding a tool, try it on a representative case and confirm the platform, runtime, and CI support. When integration is in scope, use the project’s dependency or bootstrap mechanism, pin the version, and exercise the same entry point local users or CI will run. Record any prerequisite that prevents a run.
- Decide whether existing findings should block, be removed first, or be tracked through the project's existing mechanism. Distinguish findings from configuration and tool failures.
- For OpenGrep, use explicit, versioned rule configuration, test matches and non-matches with [opengrep test](https://www.opengrep.dev/docs/commands/test.html), and configure the [scan exit behavior](https://www.opengrep.dev/docs/commands/scan.html) to match the CI policy.

## TLA+ models

- Version the specification and TLC configuration. State the properties, assumptions, and bounds. Confirm a representative broken model yields a counterexample.
- Map modeled transitions to the files and functions that implement them. Recheck that mapping when a change affects state ownership, atomicity, or reachable transitions. Preserve implementation tests for behavior outside the model. [TLC documentation](https://github.com/tlaplus/tlaplus/blob/master/general/docs/current-tools.md)
