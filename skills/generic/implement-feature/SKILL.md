---
name: implement-feature
description: "Implement a new capability or an intentional change to existing behavior. Use when the desired outcome differs from the existing contract."
---

# Implement a feature

1. State what the caller or user should observe. Trace the current entry point, relevant callers, and local conventions before selecting a design.
2. Reuse the existing path when it fits. For changes that cross boundaries or introduce state, settle who owns the state, the data contract, and the expected behavior on failure or retry before writing logic.
3. Build the smallest complete path through the affected layers. Preserve existing callers and data outside the requested change. If the work needs stages, make each stage usable and verifiable.
4. Exercise the new behavior from its normal entry point and check affected existing behavior. Run required project checks, using `validate-work` if available to coordinate them. Add focused behavioral coverage where existing tests cannot detect an important regression.
