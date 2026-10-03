# DeepSeek-V3 Architecture

Goal: Explain how DeepSeek-V3 combines sparse experts, latent attention, load balancing, multi-token prediction, and FP8 training.

Prereqs: [LLMs](../llms/) and the matrix operations in [Math for ML](../math-for-ml/). Review KV caching in [Inference & Serving](../inference-serving/); use [GPU Systems](../gpu-systems/) and [Distributed Training](../distributed-training/) for the final report's systems sections.

Status: done

Read the architecture sections and trace the routing and attention tensor shapes. Step 5 introduces independent prediction heads; compare them with V3's sequential prediction modules in step 6. All papers are free to read. This is a paper study path; full model pretraining requires large-scale infrastructure.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Sparse expert routing, capacity, and balancing losses | | [Fedus et al. — Switch Transformers](https://arxiv.org/abs/2101.03961) |
| 2 | Fine-grained experts and shared expert isolation | | [Dai et al. — DeepSeekMoE](https://arxiv.org/abs/2401.06066) |
| 3 | Multi-head Latent Attention: KV compression and decoupled RoPE | | [DeepSeek-AI — DeepSeek-V2](https://arxiv.org/abs/2405.04434) |
| 4 | Balance expert loads with routing biases | | [Wang et al. — Auxiliary-Loss-Free Load Balancing](https://arxiv.org/abs/2408.15664) |
| 5 | Predict multiple future tokens with independent heads | | [Gloeckle et al. — Better & Faster Large Language Models via Multi-token Prediction](https://arxiv.org/abs/2404.19737) |
| 6 | V3 integration: sequential prediction, FP8, and communication overlap | | [DeepSeek-AI — DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) |
