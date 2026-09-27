# Eval Harnesses

Goal: Choose LLM benchmarks, recognize contamination, and run repeatable evaluations with custom tasks and metrics.

Prereqs: [LLMs](../llms/) and [Python for ML](../python-for-ml/), plus basic command-line use.

Status: done

For the hands-on steps, use the harness's local Hugging Face backend with a model that fits your hardware. Save the model revision, task configuration, scores, and sample outputs so you can compare runs and inspect failures.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Why evals matter | **[Hamel Husain — AI Evaluations Clearly Explained in 50 Minutes](https://www.youtube.com/watch?v=uiza7wp1KrE)** | |
| 2 | What benchmarks measure and miss | **[AI Benchmarks Explained — MMLU, SWE-bench, and more](https://www.youtube.com/watch?v=fSWg4HAJjBo)** | [A Survey on Evaluation of Large Language Models](https://arxiv.org/abs/2307.03109) |
| 3 | Benchmark contamination | | [Benchmark Data Contamination of Large Language Models: A Survey](https://arxiv.org/abs/2406.04244) |
| 4 | Functional-correctness code evals | | [Chen et al. 2021 — Evaluating Large Language Models Trained on Code (HumanEval)](https://arxiv.org/abs/2107.03374) |
| 5 | Repo-level agent evals | **[How SWE-bench Changed the Way We Test AI Coders](https://www.youtube.com/watch?v=uamd4C7AFXo)** | [Jimenez et al. 2023 — SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) |
| 6 | LLM-as-judge for open-ended tasks | | [Zheng et al. 2023 — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) |
| 7 | Run benchmarks and save scores and sample outputs | | [EleutherAI — Evaluation harness user guide](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md) |
| 8 | Define custom datasets, prompts, and scoring rules | | [EleutherAI — New Task Guide](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/new_task_guide.md) |
