# Agents

Goal: Build LLM agents that call tools, connect to MCP servers, edit code, use a computer, and get evaluated on whether they actually finish the task.

Prereqs: [LLMs](../llms/) and [Prompting & Context](../prompt-context/). Python for the build steps.

Time: about 20 hours.

Status: done

Start with the difference between a fixed workflow and an agent, because most production systems should be the former. Build one loop by hand before you touch a framework. Agents that run shell commands or browse the web should run in a container or a throwaway VM. The readings are free; hosted model calls can cost money.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Workflows vs. agents, and when to use neither | | [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) |
| 2 | The parts of an agent: planning, memory, tools | | [Lilian Weng — LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) |
| 3 | ReAct: interleave reasoning and acting | | [Yao et al. 2022 — ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) |
| 4 | Build a ReAct agent with no framework | **[Alejandro AO — Python: Create a ReAct Agent from Scratch](https://www.youtube.com/watch?v=hKVhRA9kfeM)** | |
| 5 | Tool use and function calling | **[James Briggs — Building Chatbot Agents from Scratch with OpenAI Functions](https://www.youtube.com/watch?v=dgV4WFisK5Y)** | [Schick et al. 2023 — Toolformer](https://arxiv.org/abs/2302.04761) |
| 6 | Design tools a model can use well | | [Anthropic — Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) |
| 7 | Model Context Protocol (MCP) | **[LangChain — Understanding MCP From Scratch](https://www.youtube.com/watch?v=CDjjaTALI68)** | [Model Context Protocol — Introduction](https://modelcontextprotocol.io/docs/getting-started/intro) |
| 8 | Build your own MCP server | | [Model Context Protocol — Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) |
| 9 | Long-term memory | | [Packer et al. 2023 — MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) |
| 10 | Multi-agent orchestration | | [Anthropic — How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) |
| 11 | Coding agents: interfaces for reading, editing, and running code | | [Yang et al. 2024 — SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) |
| 12 | A coding agent in about 100 lines | | [Lieret et al. — Building a minimal AI agent from scratch](https://minimal-agent.com/) |
| 13 | Work alongside a coding agent | | [Claude Code — Best practices](https://code.claude.com/docs/en/best-practices) |
| 14 | Computer-use agents | **[Claude — Computer use for coding](https://www.youtube.com/watch?v=vH2f7cjXjKI)** | [Claude Docs — Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) |
| 15 | Evaluate agents on real tasks with real users | | [Yao et al. 2024 — τ-bench: Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) |

## Build it

- **No-framework agent.** Write a 150-line Python loop that calls a model, parses a tool call, runs one of three tools (search, calculator, file read), and stops on a final answer. Log every step.
- **Your own MCP server.** Expose something you actually use (your notes folder, a SQLite database, a GitHub repo) as an MCP server and connect it to a desktop client.
- **Tiny eval.** Write 20 tasks with checkable answers, then measure how often your agent succeeds over 3 runs each. Change one thing (a tool description, the system prompt) and measure again.
