# Coding Agents

Goal: Understand how coding agents navigate repositories, generate edits, use test feedback, and evaluate patches.

Prereqs: [Agents & Tooling](../agents-tooling/), Python, Git diffs, shell commands, and writing unit tests. [Eval Harnesses](../eval-harnesses/) helps with the final step.

Status: done

All readings and code examples are free to access; hosted model calls and cloud evaluation can cost money. The minimal agent executes shell commands, so use an isolated environment with a disposable repository when experimenting.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Design tools for repository navigation, editing, and execution | | [Yang et al. 2024 — SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) |
| 2 | Build a command/observation loop with error handling | | [Lieret et al. — Building a minimal AI agent from scratch](https://minimal-agent.com/) |
| 3 | Select repository context within a token budget | | [Aider — Repository map](https://aider.chat/docs/repomap.html) |
| 4 | Represent edits as whole files, search/replace blocks, or diffs | | [Aider — Edit formats](https://aider.chat/docs/more/edit-formats.html) |
| 5 | Feed lint and test failures back into the repair loop | | [Aider — Linting and testing](https://aider.chat/docs/usage/lint-test.html) |
| 6 | Compare an agent loop with localization, repair, and validation stages | | [Xia et al. 2024 — Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489) |
| 7 | Evaluate generated patches against repository tests in Docker | | [SWE-bench — Evaluation Guide](https://www.swebench.com/SWE-bench/guides/evaluation/) |
