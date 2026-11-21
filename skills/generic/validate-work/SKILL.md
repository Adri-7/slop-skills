---
name: validate-work
description: "Validate a change or existing diff against its expected behavior and the target project's checks. Use to run checks and report evidence."
---

# Validate work

1. Identify the expected outcome and the changed behavior, callers, and boundaries. Read the project's validation guide or derive the applicable checks from existing scripts and CI. Select the required baseline, checks triggered by the diff, and the evidence needed for the task.
2. Reuse evidence from the current change when it covers the same check; run the remaining applicable checks. Prefer the normal user or caller entry point for behavioral evidence. Use the documented environment and data. For validation-only work, use non-mutating variants when available and report any required check that needs writes or a manual handoff.
3. When a check fails, distinguish a regression, a pre-existing failure, and an unavailable or broken environment using evidence. Keep the expected result intact. A check that did not run remains unverified.
4. Report the commands or paths exercised, outcomes, and any unmet requirement or remaining manual check. Give a concrete prerequisite for each gap that affects acceptance.
