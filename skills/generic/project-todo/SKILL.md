---
name: project-todo
description: Prepare or clarify a requested repository task, or close the task associated with completed work. Excludes automatic task creation for every edit and external issue trackers.
---

# Repository tasks

Read local task conventions and only the selected task and relevant references. Follow existing paths, language, and lifecycle rules.

Default todo directory: `.agents/todo/`.

## Prepare

- Create a task when requested or when agreed follow-up needs tracking, not for every edit. Check for duplicates.
- Capture the need, scope, observable acceptance criteria, and blocking questions. Add implementation references only when useful and grounded in the code.
- Omit empty sections, copied repository rules, speculative designs, and step-by-step work diaries. Clarify the existing file rather than append discussion.
- With no existing convention, use draft/ for unresolved tasks, backlog/ for ready tasks, and done/ for completed tasks. The folder alone records status; no status field or README inventory.
- Move to backlog/ when implementation needs no further product decisions. Routine technical choices belong to the agent. Preparing a task does not authorize implementation.

## Complete

- Check for overlapping work when visible. Keep the task in backlog/ while implementing.
- Move to done/ as soon as implementation, acceptance criteria, and required validation are complete; no commit, PR, or merge is required.
- Keep only useful handoff notes and concise validation evidence, distinguishing passed, failed, skipped, and unavailable checks. Preserve historical evidence.
- Repair relative links after moves. Do not generate documentation or ADRs merely because a task is closing.
