# From Scratch

Goal: Build tiny nets, tokenizers, and a GPT by hand, in code, instead of only watching the architecture explained.

Prereqs: [Deep Learning](../deep-learning/) and [Python for ML](../python-for-ml/). Review transformers in [LLMs](../llms/) before GPT-2; the final step also needs C/CUDA.

Status: done

Implement each model alongside the lesson. The tokenizer and GPT-2 videos link their code and exercises in the descriptions. The lessons are free; reproducing the full GPT-2 training run requires substantial GPU compute.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Autograd engine from scratch | **[Karpathy — The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0)** | |
| 2 | A net from raw NumPy, no autograd | **[Samson Zhang — Building a neural network FROM SCRATCH (no Tensorflow/Pytorch, just numpy & math)](https://www.youtube.com/watch?v=w8yWXqWQYmU)** | |
| 3 | MLP language model from scratch | **[Karpathy — Building makemore Part 2: MLP](https://www.youtube.com/watch?v=TCH_1BHY58I)** | |
| 4 | A deeper sequence model from scratch | **[Karpathy — Building makemore Part 5: Building a WaveNet](https://www.youtube.com/watch?v=t3YJ5hKiMQ0)** | |
| 5 | BPE tokenizer from scratch | **[Karpathy — Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)** | |
| 6 | Build, train, and evaluate GPT-2 (124M) | **[Karpathy — Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)** | |
| 7 | A GPT in raw C/CUDA | | [llm.c — training GPT-2 without PyTorch or Python](https://github.com/karpathy/llm.c) |
