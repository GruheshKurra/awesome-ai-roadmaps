# Fine-Tuning

Goal: Adapt a pretrained model with LoRA/QLoRA, instruction tuning, DPO, and the data work behind good adapters.

Prereqs: [LLMs](../llms/) and [Deep Learning](../deep-learning/), plus Python and a working PyTorch training loop.

Status: done

Prepare the data before training an adapter. Compare the adapted model with its base model on held-out examples; [Eval Harnesses](../eval-harnesses/) covers repeatable evaluation. The practical lesson includes dataset formats, loss masking, and LoRA training; choose a model that fits your available hardware.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Full fine-tuning vs. parameter-efficient fine-tuning | **[LoRA & QLoRA Explained Simply — Full Fine-Tuning vs PEFT + Intuition + Practical](https://www.youtube.com/watch?v=cO6Ly7mIziQ)** | |
| 2 | LoRA | | [Hu et al. 2021 — LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) |
| 3 | QLoRA | | [Dettmers et al. 2023 — QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) |
| 4 | Configure and merge LoRA adapters | | [Hugging Face PEFT — LoRA conceptual guide](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora) |
| 5 | Data for fine-tuning | | [Meta AI — How to fine-tune: Focus on effective datasets](https://ai.meta.com/blog/how-to-fine-tune-llms-peft-dataset-curation/) |
| 6 | Supervised fine-tuning: dataset formats, loss masks, and LoRA | | [Hugging Face TRL — SFT Trainer](https://huggingface.co/docs/trl/en/sft_trainer) |
| 7 | Direct Preference Optimization | **[Direct Preference Optimization (DPO) — How to fine-tune LLMs directly without reinforcement learning](https://www.youtube.com/watch?v=k2pD3k1485A)** | [Rafailov et al. 2023 — DPO: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) |
