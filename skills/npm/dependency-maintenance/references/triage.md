# Triage npm dependencies

## Audit and advisories

- Use `npm outdated --json` for version inventory and `npm audit --json` for advisories when relevant to the scope. Read the JSON and exit status together to distinguish findings from tool errors.
- Use `npm explain <package>` to locate the introducing dependency. Prefer fixing that dependency. Use a scoped override when compatibility is verified and record the condition for removal. Review existing overrides when their underlying constraint changes.
- Keep remediation bounded to the requested scope. Check new install scripts against the project's approval policy. Avoid using `npm audit fix --force` or `--legacy-peer-deps` to suppress compatibility failures.

## Major updates

- Read official release notes and migrations, and check engines and peer requirements. Update coupled packages together when their supported versions require it. Verify migration-sensitive build and runtime behavior.
- For an unused dependency or size concern, check actual usage and build evidence before removal. Framework auto-imports, plugins, and package scripts can be callers.

[npm audit](https://docs.npmjs.com/cli/v11/commands/npm-audit/) · [npm explain](https://docs.npmjs.com/cli/v11/commands/npm-explain/) · [npm outdated](https://docs.npmjs.com/cli/v11/commands/npm-outdated/)
