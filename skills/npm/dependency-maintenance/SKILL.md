---
name: dependency-maintenance
description: "Audit, review, or update npm dependencies. Use for npm advisories, overrides, version updates, and Dependabot changes."
---

# Maintain npm dependencies

1. Confirm the requested scope and the project's npm and Node versions. Read the manifest, lockfile, relevant registry settings, and dependency decisions, including `.agents/dependencies/` if present. Treat audits and reviews that ask only for findings as read-only.
2. Use [dependency triage](references/triage.md) for audits, advisories, overrides, major updates, or suspected unused dependencies. When updating, work in coherent batches within scope. Start a general maintenance pass with compatible patch and minor updates. Preserve version-range conventions and inspect the lockfile diff.
3. Run the checks that exercise affected dependency groups. For build or runtime changes, run the project build when available. Use a lockfile-based clean install when validating reproducibility. If a batch fails, isolate its cause before updating further.
4. Report updated versions, migrations, checks run, and unresolved findings. Record lasting overrides or deferrals using the project's existing decision process. If a new record is warranted and no template exists, adapt the [decision template](assets/dependency-decisions-template.md).
