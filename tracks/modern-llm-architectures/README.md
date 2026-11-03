# Modern LLM Architectures

Goal: Go from GPT-2 to today's open models: RoPE, RMSNorm, SwiGLU, grouped-query attention, FlashAttention, mixture of experts, latent attention, multi-token prediction, and state-space models.

Prereqs: [LLMs](../llms/) and the matrix operations in [Math for ML](../math-for-ml/). KV caching from [Inference & Serving](../inference-serving/) helps with steps 3 and 9.

Time: about 25 hours.

Status: done

Step 1 maps every change since GPT-2. Steps 2–5 cover the dense Llama-style block; steps 6–12 cover mixture of experts and the DeepSeek-V3 design. Trace tensor shapes on paper as you read. Everything here runs on a laptop at toy scale.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | What changed since GPT-2 | | [Sebastian Raschka — The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) |
| 2 | Rotary position embeddings (RoPE) | **[Efficient NLP — Rotary Positional Embeddings: Combining Absolute and Relative](https://www.youtube.com/watch?v=o29P0Kpobz0)** | [Su et al. 2021 — RoFormer](https://arxiv.org/abs/2104.09864) |
| 3 | RMSNorm, GQA, and the KV cache in code | **[Umar Jamil — Coding LLaMA 2 from scratch in PyTorch](https://www.youtube.com/watch?v=oM4VmoabDAI)** | [Ainslie et al. 2023 — GQA: Training Generalized Multi-Query Transformer Models](https://arxiv.org/abs/2305.13245) |
| 4 | SwiGLU feed-forward layers | | [Shazeer 2020 — GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) |
| 5 | FlashAttention: IO-aware exact attention | **[Umar Jamil — Flash Attention derived and coded from first principles with Triton](https://www.youtube.com/watch?v=zy8ChVd_oTM)** | [Dao et al. 2022 — FlashAttention](https://arxiv.org/abs/2205.14135) |
| 6 | Mixture of experts and sliding-window attention | **[Umar Jamil — Mistral / Mixtral Explained](https://www.youtube.com/watch?v=UiX8K-xBUpE)** | [Jiang et al. 2024 — Mixtral of Experts](https://arxiv.org/abs/2401.04088) |
| 7 | Sparse routing, capacity, and balancing losses | | [Fedus et al. — Switch Transformers](https://arxiv.org/abs/2101.03961) |
| 8 | Fine-grained experts and shared experts | | [Dai et al. — DeepSeekMoE](https://arxiv.org/abs/2401.06066) |
| 9 | Multi-head latent attention (MLA) | **[Welch Labs — How DeepSeek Rewrote the Transformer](https://www.youtube.com/watch?v=0VLAoVGf_74)** | [DeepSeek-AI — DeepSeek-V2](https://arxiv.org/abs/2405.04434) |
| 10 | Balance experts without an auxiliary loss | | [Wang et al. — Auxiliary-Loss-Free Load Balancing](https://arxiv.org/abs/2408.15664) |
| 11 | Predict several tokens at once | | [Gloeckle et al. — Better & Faster Large Language Models via Multi-token Prediction](https://arxiv.org/abs/2404.19737) |
| 12 | Putting it together: FP8 training and communication overlap | | [DeepSeek-AI — DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) |
| 13 | A dense frontier recipe end to end | | [Llama Team 2024 — The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) |
| 14 | Beyond attention: selective state-space models | | [Gu & Dao 2023 — Mamba](https://arxiv.org/abs/2312.00752) |

## Build it

- **GPT-2 to Llama in one diff.** Take a nanoGPT-style model and swap in RoPE, RMSNorm, SwiGLU, and GQA one at a time. Train each variant on TinyStories for the same steps and compare loss.
- **Toy MoE layer.** Replace the MLP with 8 experts and top-2 routing. Log how many tokens each expert gets, with and without a balancing loss.
- **KV-cache calculator.** Write a function that returns KV-cache memory for MHA, GQA, and MLA given layers, heads, dims, and context length. Check it against a real model config.
