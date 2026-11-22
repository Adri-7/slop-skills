# slop-skills

Shared agent skills and templates for development workflows across projects.

## Getting started

Install with the [skills CLI](https://github.com/vercel-labs/skills) (requires Node.js and Git).

```sh
npx skills add Adri-7/slop-skills
```

Choose the skills and agents when prompted. Add `-g` for a global installation or `--agent codex` to target Codex. Run `npx skills update` to update installed skills.

1. Use [`$setup-project`](skills/generic/setup-project/SKILL.md) to adopt the framework in a repository. It builds on the project's existing instructions, commands, and checks and adds an `AGENTS.md` rule to use `azaaroth-mode` when available.
2. Start an engineering task in the configured project, or use [`$azaaroth-mode`](skills/generic/azaaroth-mode/SKILL.md) with a task to invoke it explicitly in Codex. It picks a workflow from the installed skills and reads the relevant project guidance. You can also invoke any skill directly from the [catalog](skills/README.md).

## Optional statechart support

For TLA+ state diagrams and counterexamples, install pstack's [statechart](https://github.com/cursor/plugins/tree/main/pstack/skills/statechart) skill.

```sh
npx skills add https://github.com/cursor/plugins/tree/main/pstack/skills/statechart --agent codex --skill statechart
```

Add `-g` for a global installation. Use `$statechart` directly or ask `$azaaroth-mode` to check a TLA+ model.

### Java and TLC

Install [mise](https://mise.jdx.dev/installing-mise.html) so statechart can provision its runtime:

- **Windows (PowerShell)** — `winget install --id jdx.mise --exact`
- **macOS (Homebrew)** — `brew install mise`
- **Linux (shell)** — `curl -fsSL https://mise.run | sh`. Add `$HOME/.local/bin` to the `PATH` of the environment that launches Codex.

Verify `mise --version` in a fresh terminal and relaunch Codex if its environment changed. Statechart downloads Java and TLC on its first run. If the agent cannot reach the network, preload Java and TLC from a terminal with network access. The command below matches the tested runner. Use the pins in your installed version if they differ. [Upstream runtime pins](https://github.com/cursor/plugins/blob/main/pstack/skills/statechart/scripts/run.ts)

```sh
mise install java@temurin-25 'http:tla2tools[url=https://github.com/tlaplus/tlaplus/releases/download/v1.7.4/tla2tools.jar,checksum=sha256:936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88]@1.7.4'
```

If Java and TLC are already installed, statechart also accepts the `JAVA` and `TLA2TOOLS` environment variables. See the [upstream runtime requirements](https://github.com/cursor/plugins/blob/main/pstack/skills/statechart/SKILL.md#run) for the supported Node versions and invocation.

## Shared workflows and local rules

- **slop-skills** provides reusable workflows for planning, development, review, and validation.
- **Each repository** keeps a short `AGENTS.md` that points to its architecture and validation guidance. Local references cover commands, prerequisites, and execution restrictions. Give each rule one maintained source.
- **Tests, scripts, and CI** enforce rules that can be checked reliably. [Project verification](skills/generic/project-verification/SKILL.md) helps add and maintain those checks. [Validate work](skills/generic/validate-work/SKILL.md) runs applicable checks and reports any gaps.

## References

Azaaroth mode draws on Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack) and its [poteto-mode](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md) for routing tasks to focused workflows and requiring observable evidence.

## License

[MIT](LICENSE).
