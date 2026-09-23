# Distributed Training

Goal: Scale a PyTorch training loop across GPUs and machines, recover from failures, and choose between replicated, sharded, tensor, and pipeline parallelism.

Prereqs: [Deep Learning](../deep-learning/), [GPU Systems](../gpu-systems/), and a working PyTorch training loop. Review transformers in [LLMs](../llms/) before the final three steps.

Status: done

The lessons are free to read or watch. Running the GPU examples requires compatible hardware and a matching PyTorch/CUDA installation; the multi-node lesson needs at least two networked GPU machines. Start with DDP, then study sharding when a full training replica exceeds one GPU's memory.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Data parallelism, input partitioning, and gradient all-reduce | **[PyTorch — What is Distributed Data Parallel?](https://www.youtube.com/watch?v=Cvdhwx-OBBo)** | [PyTorch — How DDP works](https://docs.pytorch.org/tutorials/beginner/ddp_series_theory.html) |
| 2 | Process groups, distributed sampling, and a multi-GPU training loop | **[PyTorch — Multi-GPU Training with DDP](https://www.youtube.com/watch?v=-LAtx9Q6DA8)** | [PyTorch — Multi GPU training with DDP](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html) |
| 3 | Launch with torchrun and resume from training snapshots | **[PyTorch — DDP Training with Torchrun](https://www.youtube.com/watch?v=9kIvQOiwYzg)** | [PyTorch — Fault-tolerant Distributed Training](https://docs.pytorch.org/tutorials/beginner/ddp_series_fault_tolerance.html) |
| 4 | Multi-node rendezvous, local/global ranks, and network troubleshooting | **[PyTorch — Multinode DDP Training](https://www.youtube.com/watch?v=KaAJtI1T2x4)** | [PyTorch — Multinode Training](https://docs.pytorch.org/tutorials/intermediate/ddp_series_multinode.html) |
| 5 | Shard parameters, gradients, and optimizer states with FSDP2 | | [PyTorch — Getting Started with FSDP2](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) |
| 6 | Tensor and sequence parallelism; combine TP with FSDP | | [PyTorch — Transformer Training with Tensor Parallel](https://docs.pytorch.org/tutorials/intermediate/TP_tutorial.html) |
| 7 | Pipeline stages, microbatches, and execution schedules | | [PyTorch — Introduction to Distributed Pipeline Parallelism](https://docs.pytorch.org/tutorials/intermediate/pipelining_tutorial.html) |
