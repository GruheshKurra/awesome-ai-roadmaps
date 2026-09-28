# ML Research Practice

Goal: Read ML papers critically, reproduce a small empirical result, and write a report whose claims match the evidence.

Prereqs: [ML Basics](../ml-basics/), [Deep Learning](../deep-learning/), probability from [Math for ML](../math-for-ml/), and a PyTorch training loop.

Status: done

Choose one published experiment with public data and a model that fits hardware you already have. State the claim you will test, then record the data splits, baseline, tuning budget, and any departures from the paper. Produce an experiment log, a comparison with the reported result, one ablation, and a short cited report. Include failed replications and inconclusive comparisons.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Read a paper in passes and trace its related work | | [S. Keshav — How to Read a Paper](https://cs.uwaterloo.ca/~brecht/courses/854-http-video-2012/readings/keshav-paper-reading.pdf) |
| 2 | Choose an ML research question and keep an experiment notebook | | [John Schulman — An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html) |
| 3 | Separate empirical gains from speculation with baselines and ablations | | [Lipton & Steinhardt 2018 — Troubling Trends in Machine Learning Scholarship](https://arxiv.org/abs/1807.03341) |
| 4 | Compare models under explicit hyperparameter search budgets | | [Dodge et al. 2019 — Show Your Work: Improved Reporting of Experimental Results](https://aclanthology.org/D19-1224.pdf) |
| 5 | Control random seeds and understand the limits of deterministic runs | | [PyTorch — Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html) |
| 6 | Measure variation across runs and quantify uncertainty in comparisons | | [Bouthillier et al. 2021 — Accounting for Variance in Machine Learning Benchmarks](https://arxiv.org/abs/2103.03098) |
| 7 | Document data, code, settings, and commands needed to reproduce results | | [Joelle Pineau — Machine Learning Reproducibility Checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist-v2.0.pdf) |
| 8 | Write a clear research argument with evidence and credit to prior work | **[Simon Peyton Jones — How to Write a Great Research Paper](https://www.youtube.com/watch?v=VK51E3gHENc)** | [Simon Peyton Jones — How to Write a Great Research Paper (slides)](https://www.microsoft.com/en-us/research/wp-content/uploads/2015/02/simon-peyton-jones_paper.pdf) |
