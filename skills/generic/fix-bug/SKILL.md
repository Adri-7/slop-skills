---
name: fix-bug
description: "Diagnose and fix behavior that differs from the intended or previously working behavior."
---

# Fix a bug

1. Establish the expected outcome and follow the failing path from its normal entry point. Reproduce the bug when accessible. If that path is unavailable, use the closest evidence you can obtain and record the gap.
2. Identify the first point where actual behavior diverges from the expected state. Test the leading hypothesis with a focused check or trace. If attempts keep failing under the same assumption, test that assumption before editing again.
3. Fix the cause where the responsible rule or state belongs. Add or update a focused behavioral regression test when practical, and confirm that it catches the failure before the fix when possible.
4. Replay the original scenario with equivalent conditions. Run required project checks, using `validate-work` if available to coordinate them. Report the cause, what changed, and which evidence verified the fix.
