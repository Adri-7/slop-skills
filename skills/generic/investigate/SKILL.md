---
name: investigate
description: "Explain how or why existing software behaves, or diagnose a symptom when the user asks for findings without a code change."
---

# Investigate a project

Start with the question and the affected entry point. Follow the relevant data or control flow through callers, state, and configuration. When asked why it was designed that way, check available decisions or history and distinguish recorded rationale from inference.

For a symptom, test the leading explanation with a focused, non-mutating check when practical. Cite the code, tests, or documentation that support the conclusion and state what evidence would resolve any remaining uncertainty. Leave project files untouched.
