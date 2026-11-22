---
name: validate-work
description: "Plan and run checks for a proposed change or existing diff. Use to capture a baseline, verify expected behavior, or report validation evidence."
---

# Validate work

1. Identify the expected outcome and the changed behavior, callers, and boundaries. Read the project's validation guide or derive the applicable checks from existing scripts and CI. Select the required baseline, checks triggered by the diff, and the evidence needed for the task. Use the [performance guide](references/performance.md) when measuring a regression, comparing performance across options, or claiming a performance gain.
2. Reuse matching evidence for the version being validated and run the remaining applicable checks. Prefer the normal user or caller entry point for behavioral evidence. Use the documented environment and data. For validation-only work, use non-mutating variants when available and report any required check that needs writes or a manual handoff.
3. When a check fails, distinguish a regression, a pre-existing failure, and an unavailable or broken environment using evidence. Keep the expected result intact. A check that did not run remains unverified.
4. Report the commands or paths exercised, outcomes, and any unmet requirement or remaining manual check. Give a concrete prerequisite for each gap that affects acceptance.
