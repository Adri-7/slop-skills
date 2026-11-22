# Independent review

1. Identify the base and the exact change to review, including relevant new files. Keep that scope stable during the review.
2. Start one fresh agent without inherited conversation and give it a read-only review task. Use read-only permissions when the host supports them. Give it the user request, material clarifications or acceptance criteria, the repository and exact diff or snapshot, and the applicable project guidance. Leave out the builder's rationale, conclusions, and claimed test results. Ask it to apply the normal review procedure and use permitted non-mutating checks.
3. Confirm findings against the reviewed change before acting. After fixes, recheck affected behavior and refresh independent coverage when a material change invalidates it. If a fresh reviewer is unavailable, run the normal checks and report the missing independent pass.

Sources for the verification pattern and its motivation. [Pstack Interrogate](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md) · [Intrinsic self-correction](https://arxiv.org/abs/2310.01798) · [Self-preference bias](https://arxiv.org/abs/2404.13076)
