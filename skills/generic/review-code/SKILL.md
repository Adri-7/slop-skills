---
name: review-code
description: "Review a code diff, commit, or pull request for concrete defects, regressions, and missing coverage."
---

# Review code

Resolve the review scope and intended behavior from the request, diff, and available change description. Inspect affected callers and contracts outside the diff, including persisted data or error paths where relevant.

Test the assumption the change relies on when a focused check is practical. Keep findings supported by an observed failure or a traceable code path. Identify which inputs or conditions trigger each issue and what users or callers experience.

Report findings in severity order with a precise file and line, trigger, and impact. Combine findings with the same cause. If there are none, say so and identify any material coverage gap. Keep edits out of a review-only request.
