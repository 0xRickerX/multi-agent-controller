# Architecture

Multi-Agent Controller separates orchestration from agent execution.

## Flow

1. Task Analyzer extracts the goal and required capabilities.
2. Planner decomposes the task into subtasks.
3. Matcher scores agents against the required capabilities.
4. Controller assembles the highest-scoring valid crew.
5. Subtasks are assigned.
6. Verifier checks completion and creates a final execution receipt.

The current implementation is deterministic and provider-agnostic.
