# Awesome AI Roadmaps

**One good video or article for each AI concept.** Free, short, and picked because it explains the idea well, not because it is famous.

- **Quality over quantity.** About 80 concepts, one pick each. A new entry has to beat the current one, or fill a real gap.
- **Free to use.** No paywalls, no course homepages, no playlists. One specific video, paper or chapter per cell.
- **Why it's here.** Every row says in one line why this pick beats the obvious alternative.

## Start here

- **Never done ML:** [Math](#math-you-actually-need) → [Python](#python-for-ml) → [Classical ML](#classical-ml) → [Deep learning](#deep-learning)
- **Build with LLMs:** [Language models](#language-models) → [Agents, RAG and evals](#agents-rag-and-evals)
- **Understand how ChatGPT works:** [Deep learning](#deep-learning) → [Language models](#language-models) → [Fine-tuning and running models](#fine-tuning-and-running-models)

[Tips for learning faster](TIPS.md). Found a broken link or a better pick? [Open an issue](https://github.com/GruheshKurra/awesome-ai-roadmaps/issues/new/choose).

## Resources

### Math you actually need

Five videos and one reference cover what deep learning uses.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| Matrices as moving space | **[3Blue1Brown — Linear transformations and matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE)** | – | Linear algebra drawn as geometry before any formula. |
| Eigenvectors | **[3Blue1Brown — Eigenvectors and eigenvalues](https://www.youtube.com/watch?v=PFDu9oVAE-g)** | – | Shows what the idea means, not just how to compute it. |
| Chain rule | **[StatQuest — The Chain Rule](https://www.youtube.com/watch?v=wl1myxrtQHQ)** | – | Worked with plain numbers, which is what backprop needs. |
| Gradient descent | **[StatQuest — Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8)** | – | One update at a time, with real numbers. |
| Matrix calculus | – | [The Matrix Calculus You Need For Deep Learning](https://explained.ai/matrix-calculus/) | The reference to open when gradient shapes stop making sense. |
| Bayes' theorem | **[StatQuest — Bayes' Theorem](https://www.youtube.com/watch?v=9wCnvr7Xw4E)** | – | Probability updating explained without notation overload. |

### Python for ML

Skip if you already write NumPy and pandas.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| NumPy | **[Keith Galli — Complete Python NumPy Tutorial](https://www.youtube.com/watch?v=GB9ByFAIAH4)** | [NumPy — the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) | One sitting covers arrays, indexing and broadcasting. |
| Broadcasting | – | [NumPy — Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) | The rule behind most shape errors. |
| pandas | **[Keith Galli — Complete Python Pandas Tutorial (2025)](https://www.youtube.com/watch?v=2uvysYbKdjM)** | [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) | Enough data wrangling for real projects. |

### Classical ML

The ideas every later model reuses: fitting, overfitting, measuring.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| Linear regression | **[StatQuest — Linear Regression](https://www.youtube.com/watch?v=7ArmBVF2dCs)** | – | Fitting a line, explained step by step. |
| Logistic regression | **[StatQuest — Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8)** | – | Bridges regression to classification and neural nets. |
| Bias and variance | **[StatQuest — Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA)** | – | The overfitting intuition in a few minutes. |
| Cross-validation | **[StatQuest — Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw)** | [scikit-learn — Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) | How to test a model without fooling yourself. |
| Precision, recall, F1 | **[StatQuest — The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o)** | [Google — Calculate and choose classification metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) | Pick metrics that match the cost of mistakes. |
| Random forests | **[StatQuest — Random Forests Part 1](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)** | – | Why averaging many weak trees works. |
| PCA | **[StatQuest — Principal Component Analysis](https://www.youtube.com/watch?v=FgakZw6K1QQ)** | – | Dimensionality reduction with a picture of what it does. |

### Deep learning

From a single neuron to the training tricks that make deep nets work.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| What a neural network is | **[3Blue1Brown — But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk)** | – | The best first visual of layers and weights. |
| Backpropagation, by hand | **[Karpathy — The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0)** | [cs231n — Backprop in practice](https://cs231n.github.io/optimization-2/) | You build the autograd engine yourself, so nothing stays magic. |
| Activations and batch norm | **[Karpathy — Building makemore Part 3: Activations & Gradients, BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc)** | [Ioffe & Szegedy 2015 — Batch Normalization](https://arxiv.org/abs/1502.03167) | Teaches how to diagnose a net that will not train. |
| Adam optimizer | **[StatQuest — Adam Optimizer](https://www.youtube.com/watch?v=JXQT_vxqwIs)** | [Kingma & Ba 2014 — Adam](https://arxiv.org/abs/1412.6980) | Momentum and scaling, shown one piece at a time. |
| Convolution | **[3Blue1Brown — But what is a convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA)** | [cs231n — Convolutional neural networks](https://cs231n.github.io/convolutional-networks/) | Convolution as a sliding operation you can picture. |
| Residual connections | **[DeepLearning.AI — ResNets](https://www.youtube.com/watch?v=ZILIbUvp5lk)** | [He et al. 2015 — Deep Residual Learning](https://arxiv.org/abs/1512.03385) | Why skip connections let networks go deep. |
| Layer normalization | – | [Ba et al. 2016 — Layer Normalization](https://arxiv.org/abs/1607.06450) | The normalization transformers use. |

### Language models

Transformer to GPT to ChatGPT, in the order that makes sense.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| Transformers, the big picture | **[3Blue1Brown — Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M)** | [SLP3 ch. 7 Transformers and Pretraining](https://web.stanford.edu/~jurafsky/slp3/7.pdf) | Start here for the overall flow of tokens through the model. |
| Attention | **[3Blue1Brown — Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc)** | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Visual walk through queries, keys and values. |
| Tokenization (BPE) | **[Karpathy — Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)** | – | Builds a GPT tokenizer live; explains many odd LLM failures. |
| Build GPT from scratch | **[Karpathy — Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY)** | – | A small GPT in code, line by line. |
| Reproduce GPT-2 | **[Karpathy — Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)** | [Radford et al. 2019 — Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | Real training details: batch size, mixed precision, speed. |
| Decoding: temperature, top-k, top-p | – | [Hugging Face — How to generate text: temperature, top-k, and top-p](https://huggingface.co/blog/how-to-generate) | Short, practical, with runnable examples. |
| Scaling laws | – | [Hoffmann et al. 2022 — Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | The paper behind compute-optimal training. |
| RLHF and instruction tuning | **[AssemblyAI — How ChatGPT actually works](https://www.youtube.com/watch?v=x_bw_IHjCWU)** | [Ouyang et al. 2022 — InstructGPT](https://arxiv.org/abs/2203.02155) | Video for the idea, paper for the recipe. |
| Using LLMs well | **[Andrej Karpathy — How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw)** | – | A practitioner's tour of what to ask and how. |

### Fine-tuning and running models

Adapt a model, then make it fast and cheap to serve.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| LoRA and QLoRA | **[LoRA & QLoRA Explained Simply — Full Fine-Tuning vs PEFT + Intuition + Practical](https://www.youtube.com/watch?v=cO6Ly7mIziQ)** | [Hu et al. 2021 — LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | Intuition first, then the original paper. |
| DPO | **[Direct Preference Optimization (DPO) — How to fine-tune LLMs directly without reinforcement learning](https://www.youtube.com/watch?v=k2pD3k1485A)** | [Rafailov et al. 2023 — DPO: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) | Preference tuning without a separate reward model. |
| KV cache | – | [Hugging Face — How caching works](https://huggingface.co/docs/transformers/cache_explanation) | Why generation gets faster with caching, and what it costs in memory. |
| PagedAttention and vLLM | – | [vLLM — Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html) | How serving engines fit more requests on one GPU. |
| GPU basics for ML | **[Stanford CS336 2025 — Lecture 5: GPUs](https://www.youtube.com/watch?v=6OBtO9niT00)** | [NVIDIA — GPU Performance Background](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html) | A full lecture on memory, compute and why kernels are slow. |
| Mixed precision | – | [PyTorch — Automatic Mixed Precision](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html) | Train faster in half precision, safely. |

### Agents, RAG and evals

Build with LLMs, then check that it works.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| What an agent is | – | [Anthropic — Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) | Clear split between workflows and agents, from people who ship them. |
| ReAct agent without a framework | **[Python: Create a ReAct Agent from Scratch](https://www.youtube.com/watch?v=hKVhRA9kfeM)** | – | A working loop in plain Python. |
| MCP | **[Understanding MCP From Scratch](https://www.youtube.com/watch?v=CDjjaTALI68)** | [Model Context Protocol — Introduction](https://modelcontextprotocol.io/introduction) | How tools connect to assistants, built up from first principles. |
| Context engineering | – | [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | What to put in the model's context, and what to leave out. |
| RAG in one pass | **[IBM Technology — What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M)** | [Lewis et al. 2020 — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | Plain-language overview, then the original paper. |
| Chunking | – | [Weaviate — Chunking Strategies to Improve LLM RAG Pipeline Performance](https://weaviate.io/blog/chunking-strategies-for-rag) | Where many RAG systems quietly lose quality. |
| Evaluating RAG | – | [Es et al. 2023 — Ragas: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) | Scores retrieval and answers without hand-labelled data. |
| Evals that matter | **[Hamel Husain — AI Evaluations Clearly Explained in 50 Minutes](https://www.youtube.com/watch?v=uiza7wp1KrE)** | – | A 50-minute practical walkthrough of evaluating LLM apps. |
| LLM-as-judge | – | [Zheng et al. 2023 — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) | Measures where model judges agree with humans and where they do not. |
| Coding agents | – | [Aider — Repository map](https://aider.chat/docs/repomap.html) | How a repo map fits a codebase into limited context. |

### Vision, image generation and audio

Seeing, generating and hearing.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| Vision transformer | **[Yannic Kilcher — An Image is Worth 16x16 Words](https://www.youtube.com/watch?v=TrdevFK_am4)** | [Dosovitskiy et al. 2020 — Vision Transformer](https://arxiv.org/abs/2010.11929) | Walks through the paper. |
| CLIP | **[Yannic Kilcher — OpenAI CLIP: Connecting Text and Images](https://www.youtube.com/watch?v=T9XSU0pKX2E)** | [Radford et al. 2021 — Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | Connects text and images in one embedding space. |
| VAEs | **[Variational Autoencoder (VAE) from scratch](https://www.youtube.com/watch?v=VUwAGLM6K_8)** | [Kingma & Welling 2013 — Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) | Built from scratch in code, plus the original paper. |
| GANs | **[Yannic Kilcher — Generative Adversarial Networks (Classic)](https://www.youtube.com/watch?v=eyxmSmjmNS0)** | [Goodfellow et al. 2014 — Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) | Walks through the original paper. |
| Diffusion models | **[AI Coffee Break — Diffusion models explained](https://www.youtube.com/watch?v=344w5h24-h8)** | [Lilian Weng — What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) | Video overview plus a widely used long-form post. |
| Latent diffusion | **[How does Stable Diffusion work? — Latent Diffusion Models Explained](https://www.youtube.com/watch?v=J87hffSMB60)** | [Rombach et al. 2022 — High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) | What makes Stable Diffusion cheap enough to run. |
| Flow matching | – | [Lipman et al. 2023 — Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | The newer training objective behind recent image models. |
| Mel spectrograms | **[Valerio Velardo — Mel Spectrograms Explained Easily](https://www.youtube.com/watch?v=9GHCiiDLHQ4)** | [Ketan Doshi — Audio Deep Learning Made Simple: Why Mel Spectrograms perform better](https://ketanhdoshi.github.io/Audio-Mel/) | What audio models actually see. |
| Whisper | **[OpenAI's Whisper Model Explained](https://www.youtube.com/watch?v=uFOkMme19Zs)** | [Radford et al. 2022 — Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) | How large-scale weak supervision gives robust speech recognition. |

### Reinforcement learning

Agents that learn by trial and reward.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| The RL problem | **[David Silver — Introduction to Reinforcement Learning](https://www.youtube.com/watch?v=2pWv7GOvuf0)** | [Lilian Weng — A (Long) Peek into Reinforcement Learning](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) | Silver's lecture sets up every term used later. |
| Key concepts | – | [OpenAI Spinning Up — Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) | A compact reference for the vocabulary. |
| DQN | **[Yannic Kilcher — Playing Atari with Deep Reinforcement Learning](https://www.youtube.com/watch?v=rFwQDDbYTm4)** | [Mnih et al. 2013 — Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602) | The Atari paper explained. |
| Policy gradients | **[David Silver — Policy Gradient Methods](https://www.youtube.com/watch?v=KHZVXao4qXs)** | [Lilian Weng — Policy Gradient Algorithms](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/) | From the lecture to a readable derivation. |
| PPO implementation details | **[Costa Huang — PPO Implementation Details](https://www.youtube.com/watch?v=MEt6rrxH8W4)** | [Schulman et al. 2017 — Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) | Covers the tricks that decide whether PPO works. |

### Specialised topics

Pick what you need.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| Causal graphs | **[3.4 - Causal Graphs](https://www.youtube.com/watch?v=vjvP9oRgZyM)** | [Facure — Graphical Causal Models](https://matheusfacure.github.io/python-causality-handbook/04-Graphical-Causal-Models.html) | A free course lecture plus a practical free text. |
| Propensity scores | **[6.4 - Propensity Scores and Inverse Probability Weighting (IPW)](https://www.youtube.com/watch?v=YQDMlNIQSA8)** | [Facure — Propensity Score](https://matheusfacure.github.io/python-causality-handbook/11-Propensity-Score.html) | Estimating effects when you cannot run an experiment. |
| Two-tower retrieval | **[Building Scalable Retrieval System with Two-Tower Models](https://www.youtube.com/watch?v=o-pZk5R0TZg)** | – | The pattern behind many large recommender systems. |
| YouTube's recommender | **[Deep Neural Networks for YouTube Recommendations](https://www.youtube.com/watch?v=WK_Nr4tUtl8)** | [Covington, Adams & Sargin 2016 — Deep Neural Networks for YouTube Recommendations](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf) | A classic two-stage design explained. |
| Time-series stationarity | **[Time Series Talk — Stationarity](https://www.youtube.com/watch?v=oY-j2Wof51c)** | [Wikipedia — Stationary process](https://en.wikipedia.org/wiki/Stationary_process) | Prerequisite for most forecasting models. |
| Do transformers help forecasting? | **[LTSF-Linear: Are Transformers Effective for Time Series Forecasting](https://www.youtube.com/watch?v=Su2Bj37rAFs)** | [Zeng et al. 2022 — Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/abs/2205.13504) | A simple linear baseline that humbles complex models. |
| Why graphs for ML | **[Stanford CS224W — Why Graphs](https://www.youtube.com/watch?v=JAB_plj2rbA)** | [Distill — A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/) | Stanford CS224W opener plus an interactive Distill intro. |
| SHAP | **[The Fair Way to Attribute Feature Importance: Shapley Values](https://www.youtube.com/watch?v=M87HSyA51-8)** | [Lundberg & Lee 2017 — A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874) | Fair attribution of a prediction to its features. |
| Transformer circuits | **[A Walkthrough of A Mathematical Framework for Transformer Circuits](https://www.youtube.com/watch?v=KV5gbOmHbjU)** | [Distill — Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) | Entry point to mechanistic interpretability. |
| Specification gaming | **[Specification Gaming: How AI Can Turn Your Wishes Against You](https://www.youtube.com/watch?v=jQOBaGka7O0)** | [DeepMind — Specification gaming: the flip side of AI ingenuity](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) | Concrete examples of models satisfying the letter of a goal. |
| Label errors in datasets | **[Cleanlab: AI to Find and Fix Errors in ML Datasets](https://www.youtube.com/watch?v=BnOTv0f9Msk)** | [Northcutt, Jiang & Chuang 2021 — Confident Learning: Estimating Uncertainty in Dataset Labels](https://arxiv.org/abs/1911.00068) | Find and fix wrong labels before blaming the model. |
| Training-data filtering | **[How to Create an LLM Dataset: FineWeb Overview](https://www.youtube.com/watch?v=vB9pHTZKoGQ)** | [Penedo et al. 2024 — The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557) | How a public web-scale dataset is built. |

### Ship it and do research

Habits that separate working projects from demos.

| Concept | Watch | Read | Why this one |
| --- | --- | --- | --- |
| Rules of ML | – | [Google — Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) | Google's practical rules for production machine learning. |
| Avoid data leakage | – | [scikit-learn — Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) | The mistake that makes a bad model look great. |
| ML test score | – | [Breck et al. 2017 — The ML Test Score](https://research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf) | A checklist for whether your ML system is production-ready. |
| How to read a paper | – | [S. Keshav — How to Read a Paper](https://cs.uwaterloo.ca/~brecht/courses/854-http-video-2012/readings/keshav-paper-reading.pdf) | A three-pass method that saves hours. |
| How to do ML research | – | [John Schulman — An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html) | Advice on picking problems and running experiments. |
| Write a clear paper | **[Simon Peyton Jones — How to Write a Great Research Paper](https://www.youtube.com/watch?v=VK51E3gHENc)** | [Simon Peyton Jones — How to Write a Great Research Paper (slides)](https://www.microsoft.com/en-us/research/wp-content/uploads/2015/02/simon-peyton-jones_paper.pdf) | Talk and slides by an expert communicator. |

## Maintenance

An automated agent reviews this list daily: it checks links, replaces weak picks, and records each check in a ledger. Its notes live in [memory.md](https://github.com/GruheshKurra/awesome-ai-roadmaps/blob/main/memory.md) and its link ledger in [data/links.json](https://github.com/GruheshKurra/awesome-ai-roadmaps/blob/main/data/links.json). See [CONTRIBUTING.md](CONTRIBUTING.md) for how to suggest a resource.
