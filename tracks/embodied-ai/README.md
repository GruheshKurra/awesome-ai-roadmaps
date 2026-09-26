# Embodied AI

Goal: Connect observations to robot actions through simulation, imitation learning, sim-to-real transfer, and vision-language-action models.

Prereqs: [Deep Learning](../deep-learning/), [Computer Vision](../computer-vision/), and MDPs from [Reinforcement Learning](../reinforcement-learning/). [Generative Models](../generative-models/) and [Multimodal](../multimodal/) help with the later policy papers.

Status: done

This track focuses on robot manipulation. Start with simulated observations and actions, then train a behavior-cloning baseline before studying larger policies. The readings are free; the simulation exercises need local compute, and reproducing hardware experiments requires a robot. Follow step 3's robosuite version requirement when running its rollouts.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Simulated observations, actions, rewards, and policy rollouts | | [robosuite — Environments](https://robosuite.ai/docs/modules/environments.html) |
| 2 | Behavior cloning, compounding errors, and DAgger | | [Sergey Levine — Supervised Learning of Behaviors (lecture slides)](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-2.pdf) |
| 3 | Train a behavior-cloning policy and inspect rollout results | | [robomimic — Getting Started](https://robomimic.github.io/docs/introduction/getting_started.html) |
| 4 | Transfer visual perception from simulation with domain randomization | | [Tobin et al. 2017 — Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907) |
| 5 | Predict action chunks and combine overlapping predictions with ACT | | [Zhao et al. 2023 — Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705) |
| 6 | Generate action sequences with diffusion and receding-horizon control | | [Chi et al. 2023 — Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137) |
| 7 | Adapt a vision-language model to predict robot actions | | [Kim et al. 2024 — OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) |
| 8 | Evaluate task success, knowledge transfer, and forgetting | | [Liu et al. 2023 — LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) |
