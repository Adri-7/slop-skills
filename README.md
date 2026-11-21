# slop-skills

Shared agent skills and templates for development workflows across projects.

## Getting started

Install with the [skills CLI](https://github.com/vercel-labs/skills) (requires Node.js and Git).

```sh
npx skills add Adri-7/slop-skills
```

Choose the skills and agents when prompted. Add `-g` for a global installation or `--agent codex` to target Codex. Run `npx skills update` to update installed skills.

1. Use [`$setup-project`](skills/generic/setup-project/SKILL.md) to adopt the framework in a repository. It builds on the project's existing instructions, commands, and checks.
2. In Codex, use [`$azaaroth-mode`](skills/generic/azaaroth-mode/SKILL.md) with a task. It picks a workflow from the installed skills and reads the relevant project guidance. You can also invoke any skill directly from the [catalog](skills/README.md).

## Shared workflows and local rules

- **slop-skills** provides reusable workflows for planning, development, review, and validation.
- **Each repository** keeps a short `AGENTS.md` that points to its architecture and validation guidance. Local references cover commands, prerequisites, and execution restrictions. Give each rule one maintained source.
- **Tests, scripts, and CI** enforce rules that can be checked reliably. [Project verification](skills/generic/project-verification/SKILL.md) helps add and maintain those checks. [Validate work](skills/generic/validate-work/SKILL.md) runs applicable checks and reports any gaps.

## References

Azaaroth mode draws on Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack) and its [poteto-mode](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md) for routing tasks to focused workflows and requiring observable evidence.

## License

[MIT](LICENSE).
