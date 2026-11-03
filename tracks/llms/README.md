# LLMs

Goal: Understand LLM architecture, pretraining, decoding, scaling, and instruction alignment.

Prereqs: [Deep Learning](../deep-learning/). [Learn NLP](../nlp/) through transformers helps.

Time: about 30 hours.

Status: done

In step 9, compare continuations of the same prompt while changing one decoding setting at a time. The lesson uses pretrained GPT-2 and includes a CPU option.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | The big picture: what an LLM is and how it is trained | **[Andrej Karpathy — Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)** | |
| 2 | Transformer overview | **[3Blue1Brown — Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M)** | [SLP3 ch. 7 Transformers and Pretraining](https://web.stanford.edu/~jurafsky/slp3/7.pdf) |
| 3 | Attention | **[3Blue1Brown — Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc)** | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) |
| 4 | The Transformer paper | **[StatQuest — Transformer Neural Networks](https://www.youtube.com/watch?v=zxQyTK8quyY)** | [Vaswani et al. 2017 — Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| 5 | Decoder-only transformers | **[StatQuest — Decoder-Only Transformers](https://www.youtube.com/watch?v=bQ5BoolX9Ag)** | |
| 6 | Tokens and BPE | **[Karpathy — Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)** | |
| 7 | Build a GPT | **[Karpathy — Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY)** | |
| 8 | GPT-2 | **[Karpathy — Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)** | [Radford et al. 2019 — Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) |
| 9 | Decoding: greedy, beam search, and sampling | | [Hugging Face — How to generate text: temperature, top-k, and top-p](https://huggingface.co/blog/how-to-generate) |
| 10 | GPT-3 and in-context learning | **[Yannic Kilcher — GPT-3: Language Models are Few-Shot Learners](https://www.youtube.com/watch?v=SY5PvZrJhLE)** | [Brown et al. 2020 — Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) |
| 11 | Scaling laws | | [Hoffmann et al. 2022 — Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) |
| 12 | Instruction following and RLHF | **[AssemblyAI — How ChatGPT actually works](https://www.youtube.com/watch?v=x_bw_IHjCWU)** | [Ouyang et al. 2022 — InstructGPT](https://arxiv.org/abs/2203.02155) |
| 13 | Post-training overview | | [SLP3 ch. 8 Post-training](https://web.stanford.edu/~jurafsky/slp3/8.pdf) |
| 14 | Open foundation models | | [Touvron et al. 2023 — LLaMA](https://arxiv.org/abs/2302.13971) |

## Build it

- **Decoding playground.** Generate from GPT-2 with greedy, beam, temperature, top-k, and top-p and write down where each fails.
- **nanoGPT on your own text.** Train a character-level GPT on a text you care about (song lyrics, your notes, a codebase).
- **Scaling mini-study.** Train 3 model sizes for the same token budget and plot loss against parameters.

Next: [Modern LLM Architectures](../modern-llm-architectures/) for what changed after GPT-2, and [Reasoning Models](../reasoning-models/) for post-training with RL.
