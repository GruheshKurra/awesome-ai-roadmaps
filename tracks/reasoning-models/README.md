# Reasoning Models

Goal: Understand how models like o1 and DeepSeek-R1 learn to reason: post-training, reward models, RL from verifiable rewards, GRPO, and test-time compute.

Prereqs: [LLMs](../llms/) and [Fine-Tuning](../fine-tuning/) (which covers DPO). The policy-gradient steps in [Reinforcement Learning](../reinforcement-learning/) help with steps 3–4 and 9.

Time: about 25 hours.

Status: done

Read in order: the pipeline first, then rewards, then where the extra compute goes (training-time RL or inference-time search). Step 14 trains a small reasoning model with GRPO; a free Colab or Kaggle GPU is enough for a 0.5B–1.5B model on a math dataset.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | The full training pipeline: pretraining, SFT, RL | **[Andrej Karpathy — Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI)** | |
| 2 | Sample many chains of thought, then vote | | [Wang et al. 2022 — Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171) |
| 3 | RLHF: reward models and PPO | **[Umar Jamil — Reinforcement Learning from Human Feedback explained with math derivations](https://www.youtube.com/watch?v=qGyFrqc34yc)** | [Hugging Face — Illustrating RLHF](https://huggingface.co/blog/rlhf) |
| 4 | What actually makes PPO for LLMs work | | [Hugging Face — The N Implementation Details of RLHF with PPO](https://huggingface.co/blog/the_n_implementation_details_of_rlhf_with_ppo) |
| 5 | Post-training reference book | | [Nathan Lambert — Reinforcement Learning from Human Feedback (book)](https://rlhfbook.com/) |
| 6 | Process rewards vs. outcome rewards | | [Lightman et al. 2023 — Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) |
| 7 | Spend compute at inference instead of training | | [Snell et al. 2024 — Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314) |
| 8 | Best-of-N and search with verifiers, in code | | [Hugging Face — Scaling test-time compute with open models](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute) |
| 9 | GRPO: PPO without a value network | **[Yannic Kilcher — GRPO Explained: DeepSeekMath](https://www.youtube.com/watch?v=bAWV_yrqx4w)** | [Shao et al. 2024 — DeepSeekMath](https://arxiv.org/abs/2402.03300) |
| 10 | RL from verifiable rewards at scale | | [DeepSeek-AI 2025 — DeepSeek-R1](https://arxiv.org/abs/2501.12948) |
| 11 | Four ways to build a reasoning model | | [Sebastian Raschka — Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) |
| 12 | Cheap reasoning: 1,000 examples and budget forcing | | [Muennighoff et al. 2025 — s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) |
| 13 | Why thinking longer helps | | [Lilian Weng — Why We Think](https://lilianweng.github.io/posts/2025-05-01-thinking/) |
| 14 | Train a reasoning model with GRPO | | [Hugging Face TRL — GRPO Trainer](https://huggingface.co/docs/trl/main/en/grpo_trainer) |
| 15 | Reward hacking and how RL goes wrong | | [Lilian Weng — Reward Hacking in Reinforcement Learning](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) |

## Build it

- **Self-consistency on GSM8K.** Sample 1, 5, and 20 answers per question from a small open model and plot accuracy against samples. This is test-time compute in one chart.
- **GRPO on a free GPU.** Train Qwen2.5-0.5B-Instruct (or similar) with TRL's GRPO trainer on GSM8K using an exact-match reward. Track reward, response length, and held-out accuracy.
- **Catch a reward hack.** Add a reward for "uses the word 'therefore'" and watch the model exploit it. Write down what you saw.
