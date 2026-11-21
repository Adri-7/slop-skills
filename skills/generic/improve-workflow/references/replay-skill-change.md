# Replay a skill change

1. Start with a realistic user request and the smallest project context in which the original problem occurs. Before running it, define an observable difference such as which workflow loads, whether files are modified, or whether a required check runs.
2. If practical, run the old and new instructions in fresh, isolated sessions using the same request, project state, and available tools. Keep the expected outcome out of the request. If the old run comes from a previous chat, use its actual record and note any relevant differences.
3. Compare the files read, actions taken, and resulting artifact or check output. Include a nearby request that should still behave as before if a routing boundary changed. Report what you observed and what was only inspected.
