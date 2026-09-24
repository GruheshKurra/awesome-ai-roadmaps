# Model Compression

Goal: Reduce model size and inference cost with pruning, quantization, distillation, and compact architectures, then measure the accuracy and latency trade-offs.

Prereqs: [Deep Learning](../deep-learning/) and a working PyTorch training loop. Review CNNs in [Computer Vision](../computer-vision/) for MobileNetV2 and transformers in [LLMs](../llms/) for the BERT example.

Status: done

Compare each compressed model with its original on the same evaluation data and hardware. Record accuracy, stored model size, and latency separately; fewer weights or bits do not guarantee faster inference. All lessons are free to read or watch. Running the quantization and sparse-inference examples requires compatible hardware; the final tutorial uses an NVIDIA GPU with compute capability 8.0 or later.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Pruning criteria, granularity, and retraining | **[MIT 6.5940 — Pruning and Sparsity, Part I](https://www.youtube.com/watch?v=EjsB0WgIfUM)** | [Han et al. 2015 — Deep Compression](https://arxiv.org/abs/1510.00149) |
| 2 | Apply pruning masks and compare local with global pruning | | [PyTorch — Pruning Tutorial](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html) |
| 3 | Represent weights and activations with fewer bits | **[MIT 6.5940 — Quantization, Part I](https://www.youtube.com/watch?v=ymAzUz3qlIA)** | |
| 4 | Choose quantized inference formats for the target hardware | | [TorchAO — Quantized Inference](https://docs.pytorch.org/ao/stable/workflows/inference.html) |
| 5 | Design compact networks with depthwise convolutions and bottlenecks | | [Sandler et al. 2018 — MobileNetV2](https://arxiv.org/abs/1801.04381) |
| 6 | Transfer a teacher's predictions to a smaller student | **[MIT 6.5940 — Knowledge Distillation](https://www.youtube.com/watch?v=Ubj3QXv4rjw)** | [Hinton et al. 2015 — Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) |
| 7 | Train and evaluate a student with distillation losses | | [PyTorch — Knowledge Distillation Tutorial](https://docs.pytorch.org/tutorials/beginner/knowledge_distillation_tutorial.html) |
| 8 | Turn 2:4 sparsity into measured speedups and check accuracy | | [PyTorch — Accelerating BERT with Semi-Structured Sparsity](https://docs.pytorch.org/tutorials/advanced/semi_structured_sparse.html) |
