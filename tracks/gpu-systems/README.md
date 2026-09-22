# GPU Systems

Goal: Explain GPU bottlenecks in neural networks, measure runtime and memory use, and optimize small kernels with mixed precision and fusion.

Prereqs: [Python for ML](../python-for-ml/), [Deep Learning](../deep-learning/), a PyTorch training loop, and basic C++ arrays and pointers for the CUDA examples.

Status: done

The lessons are free to read or watch. Running the CUDA examples requires a compatible NVIDIA GPU and CUDA Toolkit; the Triton exercises also need a supported GPU. Measure a baseline and check numerical correctness before comparing an optimization.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | GPU execution, memory hierarchy, and arithmetic intensity | **[Stanford CS336 2025 — Lecture 5: GPUs](https://www.youtube.com/watch?v=6OBtO9niT00)** | [NVIDIA — GPU Performance Background](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html) |
| 2 | CUDA kernels, threads, blocks, and host/device memory | | [Mark Harris — An Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) |
| 3 | Shared memory and synchronization within a block | | [Mark Harris — Using Shared Memory in CUDA C/C++](https://developer.nvidia.com/blog/using-shared-memory-cuda-cc/) |
| 4 | Reliable timing: warmup and CUDA synchronization | | [PyTorch — Benchmark](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html) |
| 5 | Find expensive operators and memory allocations | | [PyTorch — Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) |
| 6 | Mixed precision, autocast, and gradient scaling | | [PyTorch — Automatic Mixed Precision](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html) |
| 7 | Write and validate a Triton kernel | | [Triton — Vector Addition](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html) |
| 8 | Fuse softmax to reduce memory traffic | | [Triton — Fused Softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html) |
