# Prompting & Context

Goal: Compare prompt designs, select context, and test retrieval across context lengths.

Prereqs: [LLMs](../llms/). [Eval Harnesses](../eval-harnesses/) helps with comparing prompt variants.

Status: done

Define success criteria before changing a prompt, then compare variants on the same examples. The final step probes retrieval within context; also evaluate the tasks you intend to use. Readings are free; running examples against hosted APIs can cost money.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Define success criteria and a prompt baseline | | [Anthropic — Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) |
| 2 | Clear instructions, examples, and output structure | | [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| 3 | Chain-of-thought reasoning | | [Wei et al. 2022 — Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) |
| 4 | Prompting and tool use in practice | **[Andrej Karpathy — How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw)** | |
| 5 | Context engineering: beyond the prompt | | [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |
| 6 | Probe retrieval across context lengths and insertion depths | | [gkamradt — LLMTest_NeedleInAHaystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) |
