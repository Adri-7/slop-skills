# Measure performance

- Before editing, define the claim, metric and units, representative workload, and what result would count as improvement. Save a baseline and a command that can reproduce it. For a slowdown, use a trace or profile to locate the bottleneck before choosing a fix.
- Compare the same inputs, build settings, and runtime conditions. Check that both runs complete the intended work and produce equivalent results. Count failures separately. If the baseline is missing, recover it from the pre-change code where practical.
- For noisy metrics such as latency, repeat both variants and alternate them when practical. Report the sample count, a typical value, and the spread. Treat a difference within normal run-to-run variation as inconclusive.
- For client bundles, compare the same routes, interactions, production build settings, and compression. Measure JavaScript loaded on the initial visit separately from what loads after interaction. Exercise the affected feature to confirm it still works.
- Report before and after values, conditions, and the reproducing command or artifact. Limit the claim to the workload measured and state any gap that prevents a reliable comparison.

Inspired by pstack's [benchmark checklist](https://github.com/cursor/plugins/blob/main/pstack/skills/benchmark-checklist/SKILL.md) and [performance playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/perf-issue.md).
