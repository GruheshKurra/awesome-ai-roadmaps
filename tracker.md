# Tracker

Queue of unpublished tracks. In the git repo. Excluded from GitHub Pages (`_config.yml` `exclude`). Do not add these names to README Contents or the sidebar until the track is `done`.

One unit of work per automation run. The next work is the first unchecked box that is not already in README Contents.
Do not pre-create empty track folders. Copy `tracks/_template.md` into `tracks/<slug>/README.md` on that run.

Series headings are comments. They are not work items.
If a slug cannot be filled with 5–15 live free URLs, do not commit a stub. Leave the box unchecked and stop; report the blocker. Do not start another track.

Keep the operator prompt in `AGENTS.md` in the same slug order as Queue.

| | Count |
|---|---:|
| Done | 17 |
| Queue | 882 |
| At 5 runs/day | ~177 days |
| At 10 runs/day | ~89 days |
| At 15 runs/day | ~59 days |

## Done

- [x] LP — Learning platform. This repo is public as [awesome-ai-roadmaps](https://github.com/GruheshKurra/awesome-ai-roadmaps).
- [x] `nlp` — Learn NLP. Word vectors through BERT.
- [x] `python-for-ml` — NumPy, notebooks, data frames, plotting for ML.
- [x] `math-for-ml` — Linear algebra, calculus, probability, optimization.
- [x] `ml-basics` — Classical supervised and unsupervised ML.
- [x] `deep-learning` — MLPs, backprop, CNNs, training practice.
- [x] `computer-vision` — Images, detection, segmentation, vision backbones.
- [x] `llms` — Language models, scaling, decoding, post-training.
- [x] `from-scratch` — Build tiny nets, tokenizers, and a GPT by hand.
- [x] `eval-harnesses` — Unit tests for models, SWE-bench-style harnesses, regression evals.
- [x] `rag` — Retrieval, chunking, embeddings, citations.
- [x] `agents-tooling` — Tool use, ReAct, memory, browser/computer-use agents.
- [x] `ai-tools` — Cursor, Claude, local models, MCP, playgrounds. Try them, then point at free docs.
- [x] `prompt-context` — Prompts, context windows, context engineering.
- [x] `fine-tuning` — LoRA, instruction tuning, DPO, data for adapters.
- [x] `speech-audio` — ASR, TTS, audio representations.
- [x] `multimodal` — Vision-language, audio-language, any-to-any.
- [x] `generative-models` — VAEs, GANs, diffusion.

## Queue

### Remaining original

15. [ ] `reinforcement-learning` — MDPs, Q-learning, policy gradients, RLHF as a pointer only.
16. [ ] `graph-ml` — GNNs, graphs as data.
17. [ ] `recsys` — Ranking, two-tower, sequential recs.
18. [ ] `time-series` — Forecasting with ML.
19. [ ] `causal-ml` — Causal graphs, identification, treatment effects.
20. [ ] `interpretability` — Features, circuits, attribution.
21. [ ] `evals-safety` — Benchmarks, jailbreaks at a high level, alignment overviews.
22. [ ] `data-centric` — Datasets, labeling, synthetic data, filtering.
23. [ ] `mlops` — Training jobs, tracking, registries, deployment.
24. [ ] `inference-serving` — Quantization, vLLM, llama.cpp, batching.
25. [ ] `gpu-systems` — CUDA mental model, mixed precision, profiling.
26. [ ] `distributed-training` — Data parallel, FSDP, multi-node.
27. [ ] `compression` — Distillation, pruning, small models.
28. [ ] `coding-agents` — Repo agents, patches, test loops.
29. [ ] `embodied-ai` — Robotics, sim, vision-action.
30. [ ] `become-ml-engineer` — Job-shaped path: ship a model end to end.
31. [ ] `become-researcher` — Papers, reproduce a result, write a short argument.

### Build from scratch

32. [ ] `build-gpt2` — Reproduce GPT-2: BPE, transformer, train, sample. Karpathy nanoGPT path.
33. [ ] `build-nanogpt` — Read and modify nanoGPT until you can change the architecture and still train.
34. [ ] `build-llm-c` — GPT-2 training in C/CUDA with llm.c. No PyTorch.
35. [ ] `build-nanochat` — Karpathy nanochat: a small ChatGPT-style stack trained end to end.
36. [ ] `build-llm101n` — LLM101n: tokenizer through a tiny storyteller model in Python and C.
37. [ ] `build-deepseek-v3` — DeepSeek-V3 report: MLA, DeepSeekMoE, multi-token prediction, training setup.
38. [ ] `build-deepseek-v4` — DeepSeek V4 family: MoE scale, 1M context, Engram-style memory, Flash vs Pro.
39. [ ] `build-deepseek-r1` — R1 pipeline: cold-start SFT, GRPO, reasoning traces, distillation.
40. [ ] `build-moe` — Mixture of experts from equations: router, experts, load-balance, aux loss.
41. [ ] `build-mla` — Multi-head latent attention: compress KV, absorb projections, decode.
42. [ ] `build-mha` — Multi-head attention in NumPy: QKV, mask, softmax, concat.
43. [ ] `build-gqa-mqa` — Grouped-query and multi-query attention, memory vs quality.
44. [ ] `build-rope` — Rotary embeddings, complex view, NTK-aware and YaRN scaling.
45. [ ] `build-kv-cache` — Autoregressive KV cache, sliding window, prefix reuse.
46. [ ] `build-tokenizer` — BPE from bytes: minbpe, SentencePiece, tiktoken, special tokens.
47. [ ] `build-transformer-block` — Pre-norm block: RMSNorm, attention, SwiGLU, residuals.
48. [ ] `build-llama-arch` — Llama-style decoder: RMSNorm, SwiGLU, RoPE, GQA.
49. [ ] `build-bert` — BERT from scratch: MLM, encoder stack, WordPiece.
50. [ ] `build-t5` — T5 encoder-decoder, span corruption, relative bias.
51. [ ] `build-vit` — Vision Transformer: patches, encoder, classification head.
52. [ ] `build-whisper` — Whisper encoder-decoder for ASR, mel spectrograms, decoding.
53. [ ] `build-clip` — CLIP contrastive image-text, temperature, zero-shot.
54. [ ] `build-vae` — VAE: ELBO, reparameterization, latent walk.
55. [ ] `build-gan` — GAN minimax, DCGAN, failure modes.
56. [ ] `build-diffusion` — DDPM forward/reverse, epsilon prediction, sampling.
57. [ ] `build-flow-matching` — Flow matching and rectified flow, straight paths.
58. [ ] `build-unet` — U-Net skips for denoising and segmentation.
59. [ ] `build-mamba` — Selective SSM, discretize, parallel scan.
60. [ ] `build-rwkv` — RWKV time-mix and channel-mix, linear-time sequence model.
61. [ ] `build-autograd` — Reverse-mode AD: micrograd, topological backward.
62. [ ] `build-mlp-numpy` — MLP in NumPy only: forward, backward, train on a tiny task.
63. [ ] `build-cnn-numpy` — Conv and pool with explicit im2col, backprop through conv.
64. [ ] `build-rnn-lstm` — RNN, LSTM, GRU by hand, vanishing gradients.
65. [ ] `build-word2vec` — Skip-gram, negative sampling, embeddings you can inspect.
66. [ ] `build-optimizers` — SGD, momentum, Adam, AdamW, Muon from the update rules.
67. [ ] `build-layernorm` — LayerNorm, RMSNorm, QK-Norm, where they sit in the block.
68. [ ] `build-softmax` — Softmax numerics, online softmax, temperature, top-k/p.
69. [ ] `build-positional` — Sinusoidal, learned, ALiBi, RoPE, NoPE.
70. [ ] `build-flash-attn` — IO-aware attention: tiling, online softmax, kernel sketch.
71. [ ] `build-speculative-decoding` — Draft model, rejection sampling, lossless speedup.
72. [ ] `build-paged-attention` — vLLM PagedAttention: blocks, copy-on-write, fragmentation.
73. [ ] `build-bpe-merge` — Train a tokenizer on a small corpus and measure fertility.
74. [ ] `build-sampling` — Greedy, temperature, top-k, nucleus, typical, mirostat.
75. [ ] `build-chat-template` — Chat templates, special tokens, tool-call serialization.
76. [ ] `build-decision-transformer` — Offline RL as sequence modeling, returns-to-go.
77. [ ] `build-alphazero-tiny` — Policy/value net plus MCTS on a tiny board game.
78. [ ] `build-gnn-mpnn` — Message passing, GCN, GAT in a small graph library.
79. [ ] `build-neural-ode` — Continuous-depth nets, adjoint sensitivity, tiny ODE task.
80. [ ] `build-transformer-mt` — Attention Is All You Need replica on a small translation set.
81. [ ] `build-mae` — Masked autoencoder for images: mask, encoder, decoder.
82. [ ] `build-nerf-tiny` — Tiny NeRF: positional encoding, volume rendering.
83. [ ] `build-3dgs-tiny` — Gaussian splatting: 3D Gaussians, rasterize, optimize.
84. [ ] `build-wavenet` — Dilated causal conv language/audio model.
85. [ ] `build-pointer-net` — Pointer networks and copy mechanisms.
86. [ ] `build-memory-net` — End-to-end memory networks, hops.

### Self-host

87. [ ] `self-host-llms` — Run open weights on your machine: pick a runtime, quant, test a prompt.
88. [ ] `self-host-ollama` — Ollama models, Modelfile, OpenAI-compatible local API.
89. [ ] `self-host-llamacpp` — llama.cpp: GGUF, server, grammar, embeddings, GPU offload.
90. [ ] `self-host-vllm` — vLLM: PagedAttention, continuous batching, OpenAI server.
91. [ ] `self-host-sglang` — SGLang: RadixAttention, constrained decoding, structured gen.
92. [ ] `self-host-tgi` — Text Generation Inference: sharding, quantization backends.
93. [ ] `self-host-mlx` — Apple MLX: unified memory, convert, generate on Mac.
94. [ ] `self-host-exllamav2` — ExLlamaV2 / EXL2 quants on NVIDIA, cache, LoRA at runtime.
95. [ ] `self-host-koboldcpp` — KoboldCpp as a local server for GGUF and image backends.
96. [ ] `self-host-tabbyapi` — TabbyAPI / similar: local OpenAI-style API in front of a GPU.
97. [ ] `self-host-openwebui` — Open WebUI in front of Ollama or an OpenAI-compatible backend.
98. [ ] `self-host-continue` — Continue.dev with a local model, context providers, autocomplete.
99. [ ] `self-host-aider` — Aider against a local or self-hosted endpoint, git loop.
100. [ ] `self-host-open-interpreter` — Open Interpreter: local model, code execution sandbox.
101. [ ] `self-host-comfyui` — ComfyUI graphs for local image and video models.
102. [ ] `self-host-automatic1111` — Stable Diffusion WebUI: checkpoints, LoRAs, samplers.
103. [ ] `self-host-whisper` — Local Whisper / faster-whisper / whisper.cpp transcription.
104. [ ] `self-host-tts` — Local TTS: Piper, Kokoro, StyleTTS-class models, voice clone ethics.
105. [ ] `self-host-embeddings` — Local embedding server: TEI, llama.cpp embeddings, batch encode.
106. [ ] `self-host-rerankers` — Cross-encoder rerank locally, batch size, latency.
107. [ ] `self-host-rag` — Fully local RAG: embed, store, retrieve, generate, cite.
108. [ ] `self-host-vector-db` — FAISS, Chroma, Qdrant, LanceDB on one machine.
109. [ ] `self-host-agent` — A local agent loop with tools, no cloud API required.
110. [ ] `self-host-mcp` — MCP servers on localhost: filesystem, git, fetch, sandbox.
111. [ ] `self-host-gateway` — LiteLLM / similar: one local gateway to many backends.
112. [ ] `self-host-gpu-box` — Pick GPUs, VRAM math, tensor parallel vs quant vs smaller model.
113. [ ] `self-host-cpu-only` — CPU GGUF paths that actually finish a prompt.
114. [ ] `self-host-docker` — Containerize a model server: GPU passthrough, healthcheck, volumes.
115. [ ] `self-host-k8s` — Serve a model on Kubernetes: GPU operators, autoscaling caveats.
116. [ ] `self-host-auth` — Auth in front of a local LLM: API keys, network bind, no open 0.0.0.0.
117. [ ] `self-host-observability` — Traces, token counts, latency histograms on your own stack.
118. [ ] `self-host-offline` — Air-gapped models: download once, disable telemetry, pin hashes.
119. [ ] `self-host-multi-lora` — Serve many LoRAs on one base: Punica, S-LoRA, vLLM LoRA.
120. [ ] `self-host-speculative` — Draft + target on one box, measure tokens per second.
121. [ ] `self-host-vision` — Local VLM: LLaVA-class, Qwen-VL-class, image tokens, VRAM.
122. [ ] `self-host-browser-agent` — Browser-use or Playwright MCP against a local LLM.

### Build your own harness

123. [ ] `build-eval-harness` — Write a tiny harness: dataset in, model out, score, fail the build.
124. [ ] `lm-eval-harness` — EleutherAI lm-evaluation-harness: tasks, few-shot, loglikelihood.
125. [ ] `openai-evals` — OpenAI evals YAML/Python evals, completion vs chat.
126. [ ] `swe-bench` — SWE-bench: issues, fail-to-pass, gold tests, Verified split.
127. [ ] `swe-bench-harness` — Run SWE-bench locally: docker, patch apply, timeouts.
128. [ ] `swe-gym` — SWE-gym and training on software-engineering trajectories.
129. [ ] `terminal-bench` — Terminal-Bench: agents in a shell, scoring, terminal-bench 2.
130. [ ] `livecodebench` — LiveCodeBench: contamination-resistant code eval.
131. [ ] `humaneval-plus` — HumanEval, HumanEval+, EvalPlus, hidden tests.
132. [ ] `mbpp-eval` — MBPP and similar, execution-based scoring.
133. [ ] `osworld` — OSWorld: computer-use tasks on a real desktop.
134. [ ] `webarena` — WebArena and VisualWebArena: browser agents, sites, rewards.
135. [ ] `gaia-bench` — GAIA: general assistant tasks, levels, tool use.
136. [ ] `agentbench` — AgentBench-style tool-using agent evals.
137. [ ] `tau-bench` — tau-bench: tool-agent-user interaction, policy.
138. [ ] `bfcl` — Berkeley Function-Calling Leaderboard: parse, execute, nested.
139. [ ] `ifeval` — IFEval: verifiable instruction following.
140. [ ] `mt-bench` — MT-Bench and pairwise LLM-as-judge.
141. [ ] `arena-hard` — Arena-Hard and style of live pairwise ranking.
142. [ ] `simpleqa` — SimpleQA and short-form factuality.
143. [ ] `gpqa` — GPQA Diamond: graduate-level questions, contamination.
144. [ ] `mmlu-pro` — MMLU-Pro: harder MMLU, 10-way, reasoning.
145. [ ] `hle-eval` — Humanity's Last Exam-style hard closed evals.
146. [ ] `math-eval` — MATH, MATH-500, AIME-style contest evals.
147. [ ] `code-eval-sandbox` — Sandbox: namespaces, timeouts, no network, resource limits.
148. [ ] `llm-as-judge` — Judge prompts, position bias, pairwise vs pointwise, rubrics.
149. [ ] `reward-model-eval` — Evaluate reward models: accuracy, length bias, hacking.
150. [ ] `rag-eval` — RAGAS-class metrics: faithfulness, recall, citation.
151. [ ] `agent-eval` — Trajectory eval: tool calls, recovery, cost, side effects.
152. [ ] `eval-ci` — Put evals in CI: golden set, gates, flake, cost caps.
153. [ ] `eval-contamination` — Detect and reduce benchmark contamination.
154. [ ] `eval-dynamic` — Live / rolling evals that refresh items.
155. [ ] `eval-human` — Human protocol: raters, IAA, guidelines, sample size.
156. [ ] `build-unit-tests-for-prompts` — Prompt unit tests: fixtures, snapshots, schema asserts.
157. [ ] `build-regression-evals` — Pin a model version, fail on metric drop, bisect prompts.

### Agents 2026

158. [ ] `agent-loop` — The loop: observe, think, tool, observe. Failure and stop conditions.
159. [ ] `react-agents` — ReAct: interleaved reasoning and acting, traces.
160. [ ] `tool-calling` — Function calling: JSON schemas, parallel calls, errors.
161. [ ] `mcp-protocol` — Model Context Protocol: hosts, servers, tools, resources, prompts.
162. [ ] `mcp-build-server` — Write an MCP server: one tool, one resource, stdio.
163. [ ] `mcp-security` — MCP threat model: confused deputy, secrets, sandbox, allowlists.
164. [ ] `agent-skills` — SKILL.md / agent skills: packaged procedures agents load on demand.
165. [ ] `computer-use` — Screenshot or a11y-tree agents that click, type, scroll.
166. [ ] `browser-agents` — DOM + CDP browser agents, Playwright MCP, self-healing harnesses.
167. [ ] `browser-harness` — browser-harness-class: CDP, live capability patching, recovery.
168. [ ] `desktop-agents` — OS-level agents: AXUIElement, UI Automation, AT-SPI.
169. [ ] `coding-agent-loop` — Read repo, edit, run tests, read fail, patch. Tight loop.
170. [ ] `multi-agent` — Swarms: roles, handoff, shared memory, when one agent is enough.
171. [ ] `agent-memory` — Working memory, episodic logs, vector memory, MemGPT-class.
172. [ ] `agent-planning` — Plan then act: LLM planners, HTN-lite, replanning on fail.
173. [ ] `agent-reflection` — Reflexion, self-critique, retry with traces.
174. [ ] `agent-routing` — Routers, cascades, specialist tools, cost vs quality.
175. [ ] `agent-handoff` — Handoff protocols, schemas, who owns the transcript.
176. [ ] `agent-sandbox` — OS, FS, net, subprocess isolation for tool-using agents.
177. [ ] `agent-secrets` — No secrets in prompts. Vault, env, redaction, tool-side creds.
178. [ ] `agent-observability` — Traces, spans, tool I/O, Langfuse / Phoenix-class open tools.
179. [ ] `agent-cost` — Tokens, tool latency, retries, budget interrupts.
180. [ ] `agent-eval-loop` — Offline trajectories plus online shadow mode.
181. [ ] `a2a-protocol` — Agent-to-agent protocols and task passing.
182. [ ] `openai-agents-sdk` — Open Agents SDK-class: tools, handoffs, tracing. Free docs only.
183. [ ] `claude-agent-sdk` — Claude Agent SDK / computer-use docs. Free pages only.
184. [ ] `langgraph-agents` — LangGraph: state machines, checkpoints, cycles. Free docs.
185. [ ] `crewai-agents` — CrewAI-style role crews. Free docs, not a sales page.
186. [ ] `autogen-agents` — AutoGen / AG2 multi-agent conversations.
187. [ ] `smolagents` — Hugging Face smolagents: code-as-action agents.
188. [ ] `pydanticai-agents` — PydanticAI structured agents, tools, validation.
189. [ ] `goose-agents` — Block goose and similar local coding agents.
190. [ ] `opencode-agents` — OpenCode-class CLI coding agents on open models.
191. [ ] `aider-deep` — Aider internals: repo map, diffs, test commands.
192. [ ] `continue-deep` — Continue: context providers, autocomplete vs agent, local.
193. [ ] `cursor-agent-internals` — How repo agents index, apply diffs, run terminals. Public docs only.
194. [ ] `swe-agent` — SWE-agent: agent-computer interface for GitHub issues.
195. [ ] `openhands` — OpenHands / OpenDevin: sandboxed coding agent.
196. [ ] `devin-style-agents` — Long-running software agents: memory, tickets, PRs. Open writeups.
197. [ ] `ui-tars` — UI-TARS and purpose-built computer-use vision models.
198. [ ] `browser-use` — Browser Use: DOM-aware web agents.
199. [ ] `skyvern` — Skyvern: workflow-style web agents.
200. [ ] `playwright-mcp` — Playwright MCP: accessibility tree as tools.
201. [ ] `agent-browser` — agent-browser-class CLIs: refs, sessions, local/cloud browsers.
202. [ ] `computer-use-local` — Fully local computer-use with a VLM and a11y APIs.

### Open model families

203. [ ] `llama-family` — Llama 2/3/4: architecture, licenses, Scout-class long context.
204. [ ] `qwen-family` — Qwen3.x dense and MoE, hybrid thinking, coder variants.
205. [ ] `deepseek-family` — V3, R1, V4 Flash/Pro: MLA, MoE, 1M context, MIT weights.
206. [ ] `kimi-family` — Kimi K2/K2.5/K2.6/K3: long context, coding, Moonshot reports.
207. [ ] `glm-family` — GLM-4/5/5.1: MIT MoE, SWE-bench numbers, vision variants.
208. [ ] `gemma-family` — Gemma 2/3/4: on-device sizes, Apache shift, recitation.
209. [ ] `mistral-family` — Mistral, Mixtral, Magistral: dense, MoE, Apache.
210. [ ] `phi-family` — Phi textbook-quality data, small SLMs, limits.
211. [ ] `olmo-family` — OLMo: fully open data, code, weights, Dolma.
212. [ ] `map-neo-family` — MAP-NEO and fully open stacks.
213. [ ] `yi-family` — Yi / Llama-like bilingual models.
214. [ ] `internlm-family` — InternLM and InternVL.
215. [ ] `minimax-family` — MiniMax M2.x: multimodal, agent CLI. Weights vs API.
216. [ ] `cohere-aya` — Aya / Command open multilingual checkpoints.
217. [ ] `falcon-family` — Falcon TII models, RefinedWeb.
218. [ ] `stablelm-family` — Stable LM and related small decoders.
219. [ ] `rwkv-family` — RWKV checkpoints and linear-time inference.
220. [ ] `mamba-family` — Mamba, Jamba, hybrid SSM-transformers.
221. [ ] `dbrx-family` — DBRX MoE, open weights, Databricks report.
222. [ ] `grok-open-weights` — xAI open-weight drops when they exist. Architecture only.
223. [ ] `trinity-arcee` — Arcee Trinity-class open weights, 2026 small-lab releases.
224. [ ] `ring-ling` — Ant Group Ring/Ling 1T-class MoE reports.
225. [ ] `stepfun-models` — StepFun Step 3.x Flash-class open reports.
226. [ ] `nanbeige-models` — Nanbeige small dense open models.
227. [ ] `muse-glimmer` — 30B-class tool-calling open models (Muse Glimmer-class).

### LLM internals

228. [ ] `attention-variants` — Full, sliding, dilated, sparse, linear attention.
229. [ ] `normalization-llm` — Pre vs post-norm, sandwich, DeepNorm, QK-Norm.
230. [ ] `activations-llm` — GELU, SwiGLU, GEGLU, squared ReLU.
231. [ ] `embeddings-tokens` — Tied embeddings, input/output, scale.
232. [ ] `context-length` — Train length vs inference length, interpolation.
233. [ ] `yarn-ntk` — YaRN, NTK-aware RoPE scaling, PI.
234. [ ] `alibi` — ALiBi bias, length extrapolation.
235. [ ] `infini-attention` — Compressive / Infini-attention, memory + local.
236. [ ] `ring-attention` — Sequence parallel attention across devices.
237. [ ] `hybrid-architectures` — Attention + SSM hybrids, Qwen-Coder-Next-class.
238. [ ] `multi-token-prediction` — MTP heads, DeepSeek-style, speculative cousins.
239. [ ] `mixture-of-depths` — Skip layers dynamically, compute routing.
240. [ ] `early-exit` — Confident early exit at inference.
241. [ ] `matryoshka-reps` — Matryoshka embeddings and nested dimensions.
242. [ ] `qk-clip` — QK clipping, z-loss, attention sinks.
243. [ ] `attention-sinks` — StreamingLLMs, sink tokens, rolling KV.
244. [ ] `softcapping` — Gemma-style logit softcapping.
245. [ ] `width-depth` — Kaplan vs Chinchilla, overtraining, data-constrained scaling.
246. [ ] `scaling-laws` — Kaplan, Chinchilla, Hoffmann, emergent-abilities debate.
247. [ ] `grokking` — Grokking, delayed generalization, regularization.
248. [ ] `double-descent` — Model-wise and epoch-wise double descent.
249. [ ] `lottery-ticket` — Lottery ticket hypothesis, sparse subnets.
250. [ ] `ntk-lazy` — NTK / lazy vs feature-learning regimes.
251. [ ] `feature-learning` — Maximal update parametrization, muP, hyperparam transfer.
252. [ ] `loss-spikes` — Spike causes: data, LR, precision, routing.
253. [ ] `training-stability` — Gradient clip, loss spike skip, skip QK, init.
254. [ ] `init-llm` — μP, scaled init, residual scales.
255. [ ] `precision-training` — fp16, bf16, fp8, mixed, loss scaling.
256. [ ] `sequence-packing` — Document packing, masking, cross-doc leakage.
257. [ ] `data-parallel-llm` — DDP, grad sync, bucket, overlap.
258. [ ] `tensor-parallel-llm` — Megatron TP: column/row split, sequence parallel.
259. [ ] `pipeline-parallel-llm` — GPipe, PipeDream, 1F1B, bubbles.
260. [ ] `expert-parallel` — EP for MoE, all-to-all, capacity factor.
261. [ ] `context-parallel` — CP / Ulysses / Ring for long sequences.
262. [ ] `fsdp2` — FSDP2, HSDP, wrapping, prefetch.
263. [ ] `zero-stages` — ZeRO 1/2/3, offload CPU/NVMe.
264. [ ] `activation-checkpoint` — Recompute vs store, selective AC.
265. [ ] `compiler-pytorch` — torch.compile, Dynamo, Inductor, graph breaks.
266. [ ] `xla-jax` — JAX pjit, SPMD, XLA, named sharding.
267. [ ] `numerics-softmax` — Underflow, inf, NaN in attention, flash variants.

### Post-training and reasoning

268. [ ] `sft` — Supervised fine-tune: packing, loss on assistant tokens.
269. [ ] `instruction-tuning` — Instruction mixes, Self-Instruct, Magpie, UltraChat-class.
270. [ ] `chat-sft-data` — ShareGPT-style, role tags, refusal, tool traces.
271. [ ] `dpo` — Direct Preference Optimization, implicit reward.
272. [ ] `orpo` — ORPO: odds-ratio preference, no ref model.
273. [ ] `kto` — Kahneman-Tversky Optimization, binary feedback.
274. [ ] `ipo-simpo` — IPO, SimPO, length-normalized preferences.
275. [ ] `ppo-llm` — PPO for LLMs: policy, value, KL, advantage.
276. [ ] `grpo` — Group Relative Policy Optimization as in DeepSeek-R1.
277. [ ] `dapo` — DAPO: clip-higher, dynamic sampling, token-level loss.
278. [ ] `gspo` — Sequence-level policy optimization variants on GRPO.
279. [ ] `rlaif` — RLAIF and constitutional-style AI feedback.
280. [ ] `rlhf` — Classic RLHF stack: SFT, RM, PPO.
281. [ ] `reward-models` — Bradley-Terry RM, length bias, ensemble.
282. [ ] `process-reward` — PRMs, step-level rewards, search.
283. [ ] `outcome-reward` — Verifiable rewards: math, code, unit tests.
284. [ ] `rejection-sampling` — Best-of-N, RFT, STaR.
285. [ ] `constitutional-ai` — Principles, critique, revision.
286. [ ] `online-dpo` — Iterative DPO, on-policy preference collection.
287. [ ] `test-time-compute` — Search, extra tokens, majority, verifiers vs bigger models.
288. [ ] `chain-of-thought` — CoT, zero-shot CoT, when it helps.
289. [ ] `tree-of-thoughts` — ToT search, branches, evaluators.
290. [ ] `self-consistency` — Sample many, vote, cost.
291. [ ] `mcts-llm` — MCTS over thoughts or code, AlphaCode-class.
292. [ ] `verifiers` — Separate verifier models, process vs outcome.
293. [ ] `best-of-n` — BoN with RM, diminishing returns.
294. [ ] `reasoning-models` — o1/R1-class: long CoT, hidden vs shown traces.
295. [ ] `hybrid-thinking` — Think/non-think switch, budget tokens, Qwen-class.
296. [ ] `tool-integrated-reason` — ToRA, PAL, code interpreter in the loop.
297. [ ] `search-augmented-reason` — Search during think, citations, stop.

### RAG and retrieval

298. [ ] `embeddings-models` — E5, GTE, BGE, GTE-modern, MTEB reading.
299. [ ] `dense-retrieval` — Dual encoders, in-batch negatives, InfoNCE.
300. [ ] `sparse-retrieval` — BM25, SPLADE, learned sparse.
301. [ ] `hybrid-search` — RRF, weighted fusion, filters.
302. [ ] `colbert` — Late interaction, token-level MaxSim.
303. [ ] `cross-encoders` — Rerankers, listwise vs pointwise.
304. [ ] `chunking` — Fixed, recursive, semantic, late chunking.
305. [ ] `parent-document` — Small retrieve, big generate.
306. [ ] `contextual-retrieval` — Anthropic-style contextual chunks, BM25+embed.
307. [ ] `hyde` — Hypothetical document embeddings.
308. [ ] `query-rewrite` — Multi-query, step-back, HyDE, decomposition.
309. [ ] `raptor` — Tree summarization retrieval.
310. [ ] `graphrag` — GraphRAG: entities, communities, summaries.
311. [ ] `agentic-rag` — Retrieve as a tool, multi-hop, stop.
312. [ ] `code-rag` — Repo index, AST chunks, symbol search.
313. [ ] `multimodal-rag` — ColPali, image pages, PDF as images.
314. [ ] `long-context-vs-rag` — When to stuff the window vs retrieve.
315. [ ] `citation-grounding` — Quote, span, refuse if missing.
316. [ ] `hallucination-detect` — NLI, self-check, retrieval overlap.
317. [ ] `vector-indexes` — HNSW, IVF, PQ, DiskANN.
318. [ ] `faiss-deep` — FAISS indexes, GPU, training IVF.
319. [ ] `ann-theory` — Recall vs QPS, why exact kNN dies.
320. [ ] `embedding-finetune` — Sentence-transformers contrastive, Matryoshka.
321. [ ] `instruction-retrieval` — Instructor/E5-instruct query prefixes.
322. [ ] `multilingual-rag` — Cross-lingual retrieval, translate vs multilingual encoders.

### GPU, CUDA, kernels

323. [ ] `cuda-mental-model` — Threads, blocks, warps, SM, occupancy.
324. [ ] `gpu-memory-hierarchy` — Registers, SMEM, L2, HBM, coalescing.
325. [ ] `tensor-cores` — MMA, tf32, fp16, fp8, layouts.
326. [ ] `mixed-precision` — AMP, GradScaler, bf16 default.
327. [ ] `profiling-gpu` — Nsight, PyTorch profiler, roofline.
328. [ ] `kernel-fusion` — Why fusion wins, compiler vs hand.
329. [ ] `triton-kernels` — OpenAI Triton: write a fused kernel.
330. [ ] `cutlass` — CUTLASS GEMM hierarchy, epilogues.
331. [ ] `cuda-graphs` — Capture, replay, dynamic vs static.
332. [ ] `streams-events` — Overlap copy and compute.
333. [ ] `nccl` — AllReduce, AllToAll, rings, trees.
334. [ ] `nvlink-infiniband` — Intra-node vs inter-node fabric.
335. [ ] `rocm` — AMD ROCm, HIP, MI Open, portability.
336. [ ] `metal-mps` — Apple GPU: MPS, MLX, limits.
337. [ ] `webgpu-inference` — WONNX / WebGPU LLM demos, WASM.
338. [ ] `flashdecoding` — FlashDecoding, split-k, long-prefix.
339. [ ] `fused-moe-kernel` — Grouped GEMM for routed experts.
340. [ ] `attention-kernel-zoo` — Flash2/3, SDPA backends, xformers.
341. [ ] `quant-kernels` — INT4 GEMM, AWQ kernels, marlin.
342. [ ] `pytorch-memory` — allocator, cache, fragmentation, empty_cache myths.
343. [ ] `activation-memory` — Who uses VRAM: params, grads, adam, acts.
344. [ ] `batch-size-tuning` — Microbatch, accum, tokens/sec vs quality.
345. [ ] `compile-inductor` — Triton from inductor, autotune.
346. [ ] `ptx-sass` — When you read SASS, bank conflicts.
347. [ ] `multi-gpu-one-node` — DDP vs TP vs FSDP on 8 GPUs.

### Distributed training

348. [ ] `data-parallel` — DDP algorithm, bucketing, overlap.
349. [ ] `fsdp` — Fully sharded, wrapping policy, prefetch.
350. [ ] `tensor-parallel` — Megatron-LM TP walkthrough.
351. [ ] `pipeline-parallel` — Interleaved 1F1B, microbatches.
352. [ ] `3d-parallel` — Combine DP, TP, PP, EP.
353. [ ] `deepspeed` — DeepSpeed ZeRO, engine, config.
354. [ ] `megatron-core` — Megatron-Core layers and parallel state.
355. [ ] `fairscale` — FairScale FSDP history, fairseq.
356. [ ] `colossal-ai` — Colossal-AI heterogeneous, Gemini.
357. [ ] `composer-mosaic` — Mosaic Composer streaming, speed recipes.
358. [ ] `torchtitan` — PyTorch torchtitan LLM recipes.
359. [ ] `nemo` — NVIDIA NeMo: recipes, parallelism.
360. [ ] `axolotl` — Axolotl configs for SFT/DPO/LoRA.
361. [ ] `unsloth` — Unsloth kernels, QLoRA speed, limits.
362. [ ] `trl-train` — TRL SFT/DPO/GRPO trainers.
363. [ ] `ray-train` — Ray Train multi-node jobs.
364. [ ] `slurm-ml` — Slurm: gpus, exclusive, checkpoints.
365. [ ] `checkpointing` — Async ckpt, sharding, resume, rng.
366. [ ] `multi-node-debug` — NCCL timeouts, hanging ranks, stragglers.
367. [ ] `elastic-train` — Elastic, fault tolerance, snapshot.

### Inference internals

368. [ ] `continuous-batching` — Iteration-level scheduling vs static batch.
369. [ ] `prefix-caching` — Automatic prefix cache, hash, hit rate.
370. [ ] `chunked-prefill` — Split prefill, stall decode less.
371. [ ] `scheduler-vllm` — vLLM scheduler: waiting, running, swapped.
372. [ ] `sglang-radix` — Radix tree cache of prefixes.
373. [ ] `constrained-decoding` — GBNF, outlines, xgrammar, JSON.
374. [ ] `structured-output` — JSON schema, tool-call parsers, fail closed.
375. [ ] `grammar-sampling` — CFG-guided generation, stack FSM.
376. [ ] `speculation-eagle` — EAGLE, Medusa, lookahead, PLD.
377. [ ] `medusa-heads` — Multiple decoding heads on one backbone.
378. [ ] `draft-models` — How to pick a draft, acceptance rate.
379. [ ] `kv-quant` — KV cache int8/fp8, KIVI, SnapKV.
380. [ ] `cache-eviction` — H2O, Scissorhands, SnapKV eviction.
381. [ ] `long-prefill` — Chunked, parallel, disaggregated prefill.
382. [ ] `disagg-prefill-decode` — Split prefill and decode pools.
383. [ ] `lora-serving` — Multi-LoRA batching, S-LoRA.
384. [ ] `routing-inference` — Model cascade, MoE at serving, routers.
385. [ ] `load-balancing-llm` — Sticky prefix, cache-aware routing.
386. [ ] `streaming-tokens` — SSE, first-token latency, backpressure.
387. [ ] `batching-metrics` — TTFT, ITL, TPS, goodput.
388. [ ] `openai-compat-server` — ChatCompletions vs Responses, tools, errors.
389. [ ] `tokenizer-fast-path` — Rust tokenizers, pretok, special ids.

### Quantization and compression

390. [ ] `quantization` — Absmax, zeropoint, per-channel, calibration.
391. [ ] `gptq` — GPTQ second-order weight quant.
392. [ ] `awq` — AWQ activation-aware weight quant.
393. [ ] `gguf-quants` — Q4_K_M, IQ, imatrix, llama.cpp types.
394. [ ] `smoothquant` — SmoothQuant migrate difficulty to weights.
395. [ ] `quarot-spinquant` — QuaRot, SpinQuant, rotate then quant.
396. [ ] `bitnet` — 1.58-bit / ternary BitNet.
397. [ ] `fp8-inference` — FP8 formats, scaling, tensor cores.
398. [ ] `mxfp` — Microscaling MX formats.
399. [ ] `kv-cache-quant` — Quantize K and V separately.
400. [ ] `pruning-llm` — Wanda, SparseGPT, 2:4 structured.
401. [ ] `structured-sparsity` — N:M, speed only with kernels.
402. [ ] `distillation-llm` — MiniLLM, DistiLLM, on-policy distill.
403. [ ] `speculative-distill` — Train a draft, not just a student.
404. [ ] `small-models` — When 1–8B is the product.
405. [ ] `matryoshka-quant` — Nested dims plus quant.
406. [ ] `ggml-backend` — ggml/gguf compute graphs, backends.
407. [ ] `safetensors` — Safetensors vs pickle, mmap, fast load.

### Data and pretraining

408. [ ] `pretraining-data` — Web, books, code mix, Common Crawl.
409. [ ] `fineweb` — FineWeb, FineWeb-Edu, quality filters.
410. [ ] `dclm` — DataComp-LM, filtering competitions.
411. [ ] `dolma` — OLMo Dolma mix, docs, reproduction.
412. [ ] `the-pile` — The Pile, piles of piles, licenses.
413. [ ] `redpajama` — RedPajama recipes, SlimPajama.
414. [ ] `star-coder-data` — The Stack, StarCoder data, licenses, PII.
415. [ ] `dedup` — MinHash, suffix array, exact, near.
416. [ ] `quality-classifier` — Edu classifiers, FastText, LLM-as-filter.
417. [ ] `pii-filter` — PII, secrets, personal data, regex + models.
418. [ ] `toxicity-filter` — Hate/porn filters, false positives, eval.
419. [ ] `synthetic-pretrain` — Phi-style textbooks, Cosmopedia, collapse.
420. [ ] `annealing-data` — Mid-train on HQ data, WSD schedule.
421. [ ] `data-mix` — Domain weights, code %, multilingual.
422. [ ] `tokenization-data` — Train tokenizer on the mix, fertility, unk.
423. [ ] `packing-docs` — BOS/EOS, masking, shuffle.
424. [ ] `continual-pretrain` — Domain CPT, replay, LR.
425. [ ] `unlearning-data` — Who to forget, eval of unlearning.
426. [ ] `dataset-cards` — Datasheets, cards, consent, license.
427. [ ] `synthetic-sft` — Magpie, Evol-Instruct, persona, filters.

### Vision advanced

428. [ ] `convnets-modern` — ResNet, ConvNeXt, efficient convs.
429. [ ] `detection` — Faster R-CNN, YOLO, FCOS, labels.
430. [ ] `detr` — DETR, Hungarian matching, queries.
431. [ ] `segmentation` — Mask R-CNN, Mask2Former, SAM.
432. [ ] `sam` — Segment Anything, prompts, SAM 2 video.
433. [ ] `grounding-dino` — Open-vocab detection, text prompts.
434. [ ] `yolo-family` — YOLO from v3 through latest open forks.
435. [ ] `ocr` — OCR: CRAFT, PARSeq, TrOCR, errors.
436. [ ] `document-ai` — LayoutLM, Donut, Nougat, PDFs.
437. [ ] `depth` — Monocular depth, MiDaS, Depth Anything.
438. [ ] `optical-flow` — RAFT, flow as correspondence.
439. [ ] `tracking` — CUTIE, SAM 2 tracking, IDs.
440. [ ] `self-supervised-vision` — SimCLR, BYOL, DINO, MAE.
441. [ ] `dino-dinov2` — DINO, DINOv2, registers, PCA vis.
442. [ ] `mae-vit` — MAE ablations, mask ratio.
443. [ ] `clip-siglip` — CLIP, SigLIP, contrastive vs sigmoid.
444. [ ] `open-vocab` — OWL-ViT, Grounding DINO, CLIP detect.
445. [ ] `video-understanding` — TimeSformer, VideoMAE, action.
446. [ ] `action-recognition` — Kinetics, SlowFast, X3D.
447. [ ] `nerf` — NeRF, Instant-NGP, mip-NeRF.
448. [ ] `gaussian-splatting` — 3DGS, 2DGS, dynamic Gaussians.
449. [ ] `point-clouds` — PointNet++, sparse conv, LiDAR.
450. [ ] `equivariant-vision` — e3nn, steerable CNNs.
451. [ ] `medical-vision` — U-Net, nnU-Net, public datasets only.
452. [ ] `efficient-vision` — MobileNet, EfficientNet, ViT-tiny.

### Video, 3D, world models

453. [ ] `video-generation` — Open video models: CogVideo, HunyuanVideo, Wan.
454. [ ] `hunyuan-video` — Hunyuan Video architecture and local run.
455. [ ] `wan-video` — Wan 2.x open video, Comfy graphs.
456. [ ] `cogvideox` — CogVideoX DiT video.
457. [ ] `ltx-video` — LTX-Video and real-time-ish open video.
458. [ ] `svd` — Stable Video Diffusion, image-to-video.
459. [ ] `dit-video` — DiT for video, spatiotemporal attention.
460. [ ] `world-models` — Dreamer, IRIS, Genie, latent dynamics.
461. [ ] `dreamer` — DreamerV3: RSSM, imagine, actor-critic.
462. [ ] `jepa` — I-JEPA, V-JEPA, predict in latent space.
463. [ ] `lecun-path` — LeCun world-model talks and position papers.
464. [ ] `genie` — Genie: interactive generative environments.
465. [ ] `oasis-world` — Open world-model game agents.
466. [ ] `video-tokenizer` — MagViT, Cosmos tokenizer, latents.
467. [ ] `temporal-consistency` — Flicker, optical-flow guidance, cache.
468. [ ] `control-video` — ControlNet-for-video, pose, depth.
469. [ ] `4d-generation` — Dynamic scenes, 4D Gaussians.
470. [ ] `scene-reconstruction` — COLMAP, DUSt3R, MASt3R, VGGT.
471. [ ] `slam-learning` — DROID-SLAM, neural implicit SLAM.
472. [ ] `occupancy` — Occupancy networks, driving occupancy.
473. [ ] `openvla` — OpenVLA and vision-language-action.
474. [ ] `diffusion-policy` — Diffusion Policy for robot action.
475. [ ] `act-policy` — Action Chunking Transformers.
476. [ ] `pi0-vla` — π0 / PaliGemma-class VLAs, open reports.

### Speech and audio deep

477. [ ] `asr-deep` — CTC, transducer, Whisper, Conformer.
478. [ ] `wav2vec` — wav2vec 2.0, quantized latents, CTC.
479. [ ] `hubert` — HuBERT iterative clustering SSL.
480. [ ] `whisper-deep` — Whisper training, multilingual, timestamps.
481. [ ] `speecht5` — SpeechT5 encoder-decoder speech-text.
482. [ ] `tts-deep` — Tacotron, FastSpeech, VITS, flow TTS.
483. [ ] `neural-codecs` — SoundStream, EnCodec, DAC, residual VQ.
484. [ ] `audioldm` — AudioLDM, Tango, text-to-audio diffusion.
485. [ ] `musicgen` — MusicGen, MusicLM-class, tokens.
486. [ ] `voice-conversion` — Open VC papers, consent, anti-spoof.
487. [ ] `diarization` — pyannote diarization, embeddings, clustering.
488. [ ] `speaker-id` — x-vectors, ECAPA-TDNN, verification.
489. [ ] `kws` — Keyword spotting, tiny models on device.
490. [ ] `audio-ssl` — BEATs, AudioMAE, CLAP.
491. [ ] `speech-translation` — Seamless, Whisper translate, AST.
492. [ ] `streaming-asr` — Chunked, transducers, latency.
493. [ ] `enhancement` — Denoise, DEMUCS, spectral masking.
494. [ ] `codec-lm` — Audio LM on discrete units, VALL-E-class papers.

### Multimodal deep

495. [ ] `flamingo` — Flamingo: perceiver, gated xattn, few-shot.
496. [ ] `blip` — BLIP, BLIP-2, Q-Former.
497. [ ] `llava` — LLaVA: visual instruction tuning.
498. [ ] `qwen-vl` — Qwen-VL / 2-VL / 2.5-VL open reports.
499. [ ] `internvl` — InternVL progressive scaling.
500. [ ] `molmo` — Molmo open VLM, PixMo data.
501. [ ] `paligemma` — PaliGemma, prefix-LM image tokens.
502. [ ] `florence` — Florence-2 task tokens, unified vision.
503. [ ] `any-to-any` — Chameleon, Janus, Show-o, unified tokens.
504. [ ] `image-tokenization` — VQGAN, FSQ, MAGVIT, TITok.
505. [ ] `mm-rope` — M-RoPE, packing images and video.
506. [ ] `grounded-vlm` — Referring, boxes, traces on images.
507. [ ] `video-llm` — LLaVA-Video, Qwen-VL-video, time.
508. [ ] `audio-llm` — Qwen2-Audio, Ultravox, speech-in.
509. [ ] `document-vlm` — Donut, ColPali, pages as images.
510. [ ] `mm-eval` — MMMU, MME, RealWorldQA, hallucination.
511. [ ] `mm-rag` — Retrieve images and text, late fusion.
512. [ ] `mm-agents` — See, click, read screens, UI-TARS.

### Reinforcement learning deep

513. [ ] `mdp-bellman` — MDPs, Bellman, optimality, DP.
514. [ ] `mc-td` — MC vs TD, bias-variance, n-step.
515. [ ] `q-learning-deep` — Q-learning, Double, Dueling, Rainbow.
516. [ ] `policy-gradient` — REINFORCE, baseline, causality.
517. [ ] `actor-critic` — A2C, A3C, GAE.
518. [ ] `ppo` — PPO clip, value clip, entropy.
519. [ ] `sac` — SAC entropy, twin Q, reparam.
520. [ ] `td3` — TD3 delayed policy, target noise.
521. [ ] `trpo-acktr` — TRPO natural gradient, ACKTR.
522. [ ] `dqn-rainbow` — Rainbow components, Atari.
523. [ ] `offline-rl` — CQL, IQL, conservative, OOD.
524. [ ] `offline-to-online` — Cal-QL, jump-start.
525. [ ] `model-based-rl` — Dyna, PETS, Dreamer pointer.
526. [ ] `mu-zero` — MuZero, value-equivalent models.
527. [ ] `alpha-zero` — Self-play, MCTS, AlphaZero.
528. [ ] `mcts` — UCT, PUCT, backups.
529. [ ] `bandits` — UCB, Thompson, contextual.
530. [ ] `imitation` — BC, DAgger, inverse RL intro.
531. [ ] `hierarchical-rl` — Options, feudal, HIRO.
532. [ ] `multi-agent-rl` — Independent Q, MADDPG, self-play.
533. [ ] `rl-engineering` — VecEnv, frameskip, reward scale.
534. [ ] `gflownets` — GFlowNets: sample proportional to reward.
535. [ ] `decision-transformer-rl` — DT, TrajGPT, limitations.

### Graphs, recsys, time series, causal

536. [ ] `gcn` — Kipf GCN, renormalization, limits.
537. [ ] `graphsage` — SAGE sampling, inductive.
538. [ ] `gat` — GAT attention, GAT v2.
539. [ ] `gin` — GIN, WL test, expressivity.
540. [ ] `graph-transformers` — Graphormer, SAN, GPS.
541. [ ] `hetero-graphs` — RGCN, HGT, relation types.
542. [ ] `temporal-graphs` — TGN, TGNNs, events.
543. [ ] `kg-completion` — TransE, RotatE, ComplEx.
544. [ ] `two-tower` — Two-tower retrieval, in-batch negs.
545. [ ] `dlrm` — DLRM embeddings, bottoms, tops.
546. [ ] `sasrec` — SASRec sequential recs.
547. [ ] `bert4rec` — BERT4Rec cloze recs.
548. [ ] `ranking-losses` — BPR, pairwise, listwise, softmax.
549. [ ] `rec-metrics` — Recall@k, NDCG, coverage, popularity.
550. [ ] `patchtst` — PatchTST, iTransformer, channel.
551. [ ] `tft` — Temporal Fusion Transformer.
552. [ ] `nbeats` — N-BEATS, N-HiTS, interpretable stacks.
553. [ ] `deepar` — DeepAR, probabilistic forecast.
554. [ ] `conformal` — Split conformal, coverage, time series.
555. [ ] `causal-graphs` — DAGs, d-separation, do-calculus intro.
556. [ ] `ate-cate` — ATE, CATE, meta-learners.
557. [ ] `iv-dml` — Instruments, DML, orthogonal ML.
558. [ ] `uplift` — Uplift, TARNet, S-learner traps.
559. [ ] `synthetic-control` — Synthetic control, matrix completion.

### Science ML

560. [ ] `alphafold` — AlphaFold 2/3 overview, Evoformer, open reproductions.
561. [ ] `esm` — ESM protein LMs, embeddings, inverse fold.
562. [ ] `boltz` — Boltz and open structure prediction.
563. [ ] `docking` — DiffDock, EquiBind, pose eval.
564. [ ] `mol-gen` — Molecular generation, SELFIES, diffusion mols.
565. [ ] `materials` — CHGNet, MACE, interatomic potentials.
566. [ ] `graphcast` — GraphCast, Pangu, weather ML.
567. [ ] `neural-operators` — FNO, DeepONet, PDE surrogates.
568. [ ] `pinns` — PINNs, collocation, failure modes.
569. [ ] `geometric-dl` — Bronstein geometric DL, gauges.
570. [ ] `e3nn` — e3nn, irreps, SE(3).
571. [ ] `neural-ode-sci` — Latent ODEs, irregular time.
572. [ ] `tabular-dl` — FT-Transformer, TabNet, TabPFN.
573. [ ] `tabpfn` — TabPFN prior-fitted networks.
574. [ ] `gbdt-vs-nets` — XGBoost/LightGBM vs nets on tabular.
575. [ ] `anomaly` — Isolation forest, autoencoders, Deep SVDD.
576. [ ] `umap-tsne` — t-SNE, UMAP, neighbor graphs, lies.
577. [ ] `clustering-deep` — Deep clustering, SCAN, DEC.
578. [ ] `active-learning` — Uncertainty, BALD, batch AL.
579. [ ] `weak-supervision` — Snorkel, labeling functions.
580. [ ] `semi-supervised` — FixMatch, Mean Teacher, MixMatch.
581. [ ] `domain-adaptation` — DANN, CORAL, test-time adapt.
582. [ ] `meta-learning` — MAML, ProtoNets, metric vs opt.
583. [ ] `neural-process` — Neural processes, uncertainty.
584. [ ] `gaussian-processes` — GPs, kernels, sparse GPs.
585. [ ] `bayesian-dl` — VI, MC dropout, deep ensembles.
586. [ ] `calibration` — ECE, temperature scale, Dirichlet.
587. [ ] `uncertainty` — Aleatoric vs epistemic, when to abstain.

### Interpretability and safety

588. [ ] `circuits` — Induction heads, circuits, toy models.
589. [ ] `sae` — Sparse autoencoders, dictionary learning.
590. [ ] `activation-patching` — Path patching, causal mediation.
591. [ ] `logit-lens` — Logit lens, tuned lens, early decoding.
592. [ ] `probing` — Linear probes, control tasks, amnesia.
593. [ ] `attribution` — Integrated grads, attention is not explanation.
594. [ ] `shap-lime` — SHAP, LIME, tabular and text limits.
595. [ ] `influence` — Influence functions, TracIn, data attribution.
596. [ ] `model-editing` — ROME, MEMIT, locate then edit.
597. [ ] `knowledge-conflicts` — Parametric vs contextual knowledge.
598. [ ] `sycophancy` — Sycophancy evals and mitigations.
599. [ ] `deception-evals` — Sandbagging, scheming evals at a high level.
600. [ ] `jailbreaks` — Jailbreak taxonomy, defenses, not a cookbook.
601. [ ] `prompt-injection` — Indirect injection, untrusted tools, delimiters.
602. [ ] `guardrails` — Classifiers, canaries, output filters.
603. [ ] `watermarking` — Kirchenbauer et al., detectability, robustness.
604. [ ] `ai-text-detect` — Detectors, ROC, paraphrasing, limits.
605. [ ] `membership-inference` — MIA overview, what it shows.
606. [ ] `extraction` — Training-data extraction papers, mitigations.
607. [ ] `unlearning` — TOFU, WMDP, forget quality vs utility.
608. [ ] `fairness` — Group metrics, equalized odds, limits.
609. [ ] `privacy-ml` — DP-SGD, epsilon, utility.
610. [ ] `federated` — FedAvg, non-IID, secure agg overview.
611. [ ] `scalable-oversight` — Debate, IDA, weak-to-strong.
612. [ ] `weak-to-strong` — W2S generalization, Burns et al.
613. [ ] `model-spec` — Specs, instruction hierarchy, system vs user.
614. [ ] `red-team` — Structured red team, severity, coverage.
615. [ ] `eval-alignment` — TruthfulQA, HarmBench, XSTest. High level.
616. [ ] `mech-interp-toolkit` — TransformerLens, SAELens, nnsight.
617. [ ] `toy-models-superpos` — Toy models of superposition, features.

### MLOps and production

618. [ ] `experiment-tracking` — MLflow, W&B-free alternatives, Aim, tracking.
619. [ ] `model-registry` — Versions, stages, aliases, rollback.
620. [ ] `data-versioning` — DVC, lakeFS, snapshots.
621. [ ] `feature-store` — Offline/online features, point-in-time.
622. [ ] `training-jobs` — Job specs, retries, GPU queue.
623. [ ] `ci-for-ml` — Lint data, unit-test models, eval gates.
624. [ ] `drift` — Covariate, label, embedding drift.
625. [ ] `monitoring-llm` — Quality, cost, toxicity, tool-error rates.
626. [ ] `ab-test-models` — Online experiments, CUPED, SRM.
627. [ ] `canary-models` — Shadow, canary, interleaved.
628. [ ] `fastapi-ml` — FastAPI + batching + timeouts.
629. [ ] `bentoml` — BentoML build, runner, deploy.
630. [ ] `ray-serve` — Ray Serve deployments, autoscaling.
631. [ ] `kserve` — KServe / inference graphs.
632. [ ] `batch-inference` — Map jobs, parquet, retries.
633. [ ] `online-inference` — p99, backpressure, load shed.
634. [ ] `prompt-versioning` — Pin prompts, reviews, eval on change.
635. [ ] `golden-datasets` — Versioned goldens, owners, drift.
636. [ ] `llm-observability` — OpenTelemetry for LLM spans.
637. [ ] `langfuse` — Langfuse self-host traces and scores.
638. [ ] `phoenix-arize` — Phoenix tracing and eval locally.
639. [ ] `cost-control` — Caps, caches, smaller models first.
640. [ ] `slo-ml` — SLOs for latency and quality.
641. [ ] `incident-ml` — Bad model rollback, runbooks.
642. [ ] `repro-seeds` — Seeds, nondeterminism, CUDA, dropout.

### Math and optimization deeper

643. [ ] `linalg-ml` — SVD, eig, QR, why they show up in ML.
644. [ ] `matrix-calc` — Jacobians, Hessians, autodiff shapes.
645. [ ] `probability-ml` — Cond, Bayes, conjugacy used in ML.
646. [ ] `info-theory` — Entropy, KL, cross-entropy, MI.
647. [ ] `stats-est` — MLE, MAP, bias-variance.
648. [ ] `pac-bayes` — PAC-Bayes bounds, what they give.
649. [ ] `opt-convex` — GD, rates, condition number.
650. [ ] `opt-nonconvex` — Saddle, landscape, SGD noise.
651. [ ] `adamw-deep` — AdamW decouple, epsilon, warmup.
652. [ ] `muon-optimizer` — Muon, SOAP, Shampoo-class second order.
653. [ ] `shampoo-soap` — Shampoo, SOAP, Kronecker factors.
654. [ ] `lion-sophia` — Lion, Sophia, Hessian diagonal.
655. [ ] `schedules` — Cosine, WSD, warmup, cooldown.
656. [ ] `sam-optimizer` — Sharpness-aware minimization.
657. [ ] `regularization` — Weight decay, dropout, stochastic depth.
658. [ ] `normalization-math` — Why BN/LN change the landscape.
659. [ ] `kernel-methods` — RKHS, NTK, when kernels win.
660. [ ] `spectral` — Graph Laplacian, Fourier on graphs.
661. [ ] `optimal-transport` — Sinkhorn, Wasserstein, WGAN link.
662. [ ] `score-matching` — Score, denoising score, Tweedie.

### NLP remaining

663. [ ] `tokenization-nlp` — Unicode, NFC, byte fallback, multilingual.
664. [ ] `pos-ner` — Sequence labeling, BIO, CRF, modern NER.
665. [ ] `parsing` — Dep parse, constituency, use in tools.
666. [ ] `coref` — Coreference, mention ranking.
667. [ ] `summarization` — Abstractive vs extractive, faithfulness.
668. [ ] `mt` — NMT, backtranslation, COMET.
669. [ ] `multilingual-llm` — Token tax, data mix, scripts.
670. [ ] `low-resource-nlp` — Adapters, translate-train, dictionaries.
671. [ ] `ie-re` — Relation extraction, OpenIE, graphs.
672. [ ] `topic-models` — LDA vs embeddings vs BERTopic.
673. [ ] `sentiment` — Polarity, aspect, social-data traps.
674. [ ] `style-transfer` — Formality, authorship, eval.
675. [ ] `dialogue-state` — DST, TOD, MultiWOZ, LLM TOD.
676. [ ] `factual-probing` — LAMA, T-REx, closed-book QA.

### Code models

677. [ ] `codex-history` — Codex, Copilot-era papers, HumanEval.
678. [ ] `starcoder` — StarCoder, The Stack, fill-in-middle.
679. [ ] `codellama` — Code Llama infill, long context, Python.
680. [ ] `deepseek-coder` — DeepSeek-Coder, V2/V3 coder reports.
681. [ ] `qwen-coder` — Qwen2.5/3 Coder, Qwen3-Coder-Next hybrid.
682. [ ] `codestral` — Codestral / Devstral-class open coder weights.
683. [ ] `fim` — Fill-in-the-middle objective, PSMs.
684. [ ] `repo-level-code` — RepoPedia, CrossCodeEval, repo context.
685. [ ] `code-repair` — APR, SWE-bench as repair, tests as spec.
686. [ ] `test-gen` — Generate tests, mutation, flaky tests.
687. [ ] `code-rag-index` — ctags, LSP, tree-sitter chunks.
688. [ ] `formal-llm` — Lean, Coq, AlphaProof-class overviews.
689. [ ] `diff-apply` — Search-replace, unified diff, fuzzy apply.
690. [ ] `program-analysis-llm` — Types, CFG, call graph as tools.
691. [ ] `code-eval-beyond` — BigCodeBench, LiveCodeBench, ClassEval.
692. [ ] `terminal-agents` — Shell agents, allowlists, PTY.

### Memory and long context

693. [ ] `context-engineering` — What goes in the window, order, compression.
694. [ ] `needle-haystack` — NIAH, multiple needles, haystack structure.
695. [ ] `long-context-arch` — Longformer, BigBird, LongNet, Hyena.
696. [ ] `recurrent-memory` — Transformer-XL, Compressive, Infini.
697. [ ] `memgpt` — OS-like memory tiers, paging.
698. [ ] `graph-memory` — Episode graphs, Zep-class, entity memory.
699. [ ] `summarize-memory` — Recursive summaries, lossy, eval.
700. [ ] `kv-offload` — CPU/NVMe KV, prefetch, paged.
701. [ ] `engram-memory` — DeepSeek Engram conditional memory, 1M context.
702. [ ] `yarn-long` — Extend a short model, eval beyond train len.
703. [ ] `packing-long` — Documents vs turns, loss masks.
704. [ ] `lost-in-middle` — Position bias in long context.
705. [ ] `infinite-context-eval` — RULER, ∞Bench, what they measure.

### Structured generation and tools

706. [ ] `json-mode` — JSON mode vs schema, trailing commas.
707. [ ] `outlines` — Outlines FSM, regex, JSON schema.
708. [ ] `xgrammar` — xgrammar fast constrained decoding.
709. [ ] `guidance` — Guidance / Guidance-AI programs.
710. [ ] `instructor` — Instructor / Pydantic extraction.
711. [ ] `tool-parsers` — Parse tool XML/JSON, repair, reject.
712. [ ] `parallel-tools` — Parallel calls, dependencies, join.
713. [ ] `sql-tools` — Text-to-SQL, schema, execute, guard.
714. [ ] `browser-tools` — Fetch, extract, robots, rate limits.
715. [ ] `code-interpreter` — Sandboxed Python, plots, files.
716. [ ] `retrieval-as-tool` — When RAG is a tool not a pipeline.
717. [ ] `human-in-loop` — Approvals, interrupts, HITL graphs.
718. [ ] `output-repair` — JSON repair, retry, fallbacks.

### Edge, mobile, privacy

719. [ ] `on-device-llm` — 1–8B on phone/laptop, ram, thermal.
720. [ ] `llama-cpp-mobile` — llama.cpp on iOS/Android, GPU backends.
721. [ ] `execu-torch` — ExecuTorch / TFLite LLM paths.
722. [ ] `mlc-llm` — MLC-LLM compile to native.
723. [ ] `web-llm` — WebLLM in the browser, WASM/WebGPU.
724. [ ] `tiny-ml` — MCU, TFLite Micro, keyword, sensors.
725. [ ] `distill-on-device` — Distill to the device budget.
726. [ ] `federated-llm` — On-device adapters, not full pretrain.
727. [ ] `dp-finetune` — DP-SGD LoRA, privacy budget.
728. [ ] `secure-inference` — TEE overview, split inference.
729. [ ] `local-first-ai` — Product design: local default, cloud optional.
730. [ ] `license-weights` — MIT vs Apache vs Llama vs Qwen terms.

### Research craft

731. [ ] `read-a-paper` — Pass 1/2/3, figures first, reproduce table 1.
732. [ ] `reproduce-result` — Match a number, log gaps, ablate.
733. [ ] `ablations` — One change at a time, error bars.
734. [ ] `error-analysis` — Slice, confusion, qualitative fails.
735. [ ] `write-a-paper` — Claim, evidence, related work hygiene.
736. [ ] `review-a-paper` — Reviewer checklist, reproducibility.
737. [ ] `open-release` — Weights, data, recipes, issues.
738. [ ] `model-cards` — Model cards, limits, evals.
739. [ ] `benchmark-hygiene` — No test peek, contamination, version pins.
740. [ ] `negative-results` — What did not work, still write it down.
741. [ ] `compute-budget` — Chinchilla math for your GPU hours.
742. [ ] `lit-review` — Related work without dumping 80 cites.

### Paper walkthroughs

743. [ ] `paper-attention` — Vaswani 2017 line by line.
744. [ ] `paper-gpt2` — GPT-2 report and the 124M reproduce.
745. [ ] `paper-gpt3` — GPT-3 few-shot paper.
746. [ ] `paper-chinchilla` — Hoffmann 2022 compute-optimal.
747. [ ] `paper-instructgpt` — Ouyang InstructGPT.
748. [ ] `paper-llama` — LLaMA 1/2/3 reports.
749. [ ] `paper-moe` — Switch Transformers, GShard, ST-MoE.
750. [ ] `paper-mla` — DeepSeek-V2/V3 MLA sections.
751. [ ] `paper-r1` — DeepSeek-R1 technical report.
752. [ ] `paper-v4` — DeepSeek-V4 / Engram reports when public.
753. [ ] `paper-dit` — Peebles DiT, Scalable Diffusion.
754. [ ] `paper-ldm` — Rombach latent diffusion.
755. [ ] `paper-whisper` — Radford Whisper.
756. [ ] `paper-clip` — Radford CLIP.
757. [ ] `paper-sam` — Kirillov SAM.
758. [ ] `paper-alphafold` — Jumper AlphaFold2.
759. [ ] `paper-muzero` — Schrittwieser MuZero.
760. [ ] `paper-ppo` — Schulman PPO.
761. [ ] `paper-dpo` — Rafailov DPO.
762. [ ] `paper-lora` — Hu LoRA.
763. [ ] `paper-flashattn` — Dao FlashAttention.
764. [ ] `paper-vllm` — Kwon vLLM PagedAttention.
765. [ ] `paper-mamba` — Gu Mamba.
766. [ ] `paper-jepa` — Assran I-JEPA.

### Training dynamics and tricks

767. [ ] `warmup-decay` — Why warmup, cosine vs WSD.
768. [ ] `grad-clip` — Global vs per-param, when spikes.
769. [ ] `loss-functions-llm` — CE, z-loss, aux MoE, MTP.
770. [ ] `label-smoothing` — When it helps, when it hurts LLMs.
771. [ ] `dropout-llm` — Attention dropout, residual dropout, 0.0 at scale.
772. [ ] `weight-tying` — Tie embed, vocab size effects.
773. [ ] `seq-len-curriculum` — Start short, grow length.
774. [ ] `overtrain` — Tokens >> Chinchilla, inference-optimal.
775. [ ] `distill-on-policy` — On-policy vs off-policy distill.
776. [ ] `ema` — Polyak average, eval with EMA.
777. [ ] `stochastic-depth` — Drop path in deep ViTs.
778. [ ] `mixup-cutmix` — Vision mixup, when for LM.
779. [ ] `gradient-accum` — Effective batch, LN stats, BN traps.
780. [ ] `microbatch` — Memory vs sync, token budget.
781. [ ] `data-order` — Shuffle, epochs, replay, annealing.
782. [ ] `eval-during-train` — How often, which tasks, cost.
783. [ ] `hyperparam-transfer` — muP, width scaling rules.
784. [ ] `spikiness` — Skip batches, rollback, dump dumps.

### Architectures beyond vanilla GPT

785. [ ] `encoder-decoder` — T5, BART, when enc-dec still wins.
786. [ ] `prefix-lm` — UniLM, GLM, prefix attention masks.
787. [ ] `retnet` — RetNet, retention, parallel vs recurrent.
788. [ ] `hyena` — Hyena, long conv, FFT.
789. [ ] `s4-ssm` — S4, DSS, Hippo, history of SSMs.
790. [ ] `griffin-hawk` — Griffin, Hawk, recurrent gated.
791. [ ] `jamba` — Jamba hybrid MoE + Mamba.
792. [ ] `recurrent-gemma` — Griffin-based small recurrent.
793. [ ] `linear-attention` — Performer, Linear Transformer, Lightning.
794. [ ] `state-space-llm` — When SSMs beat attention on long seq.
795. [ ] `mixture-of-recursions` — Recursive depth sharing papers.
796. [ ] `universal-transformer` — ACT, ponder, adaptive compute.
797. [ ] `hourglass` — Hierarchical pooling transformers.
798. [ ] `perceiver` — Perceiver, IO, latent bottleneck.
799. [ ] `gmlp-mlp-mixer` — All-MLP, Mixer, when they work.
800. [ ] `kan` — KAN vs MLP, hype vs evidence.

### Prompting and context advanced

801. [ ] `prompt-structure` — Role, task, constraints, format, examples.
802. [ ] `few-shot-design` — Example order, label space, diversity.
803. [ ] `cot-prompting` — Let's think, answer format, math.
804. [ ] `decomp-prompting` — Least-to-most, decomposed prompting.
805. [ ] `self-ask` — Self-Ask, follow-ups, search.
806. [ ] `generated-knowledge` — Generate then answer.
807. [ ] `prompt-caching` — System prefix cache, Anthropic/OpenAI docs.
808. [ ] `context-distill` — Compress history, keep decisions.
809. [ ] `system-prompt` — Stability, injection, instruction hierarchy.
810. [ ] `eval-prompts` — Same eval, different wrapper, noise.

### Diffusion and generative image deep

811. [ ] `score-diffusion` — Song SDE/ODE, probability flow.
812. [ ] `ddim` — DDIM, DPM-Solver, consistency.
813. [ ] `consistency-models` — Consistency distillation, one-step.
814. [ ] `latent-diffusion` — VAE latent, SD 1.x/2/XL.
815. [ ] `sd3-flux` — SD3 MMDiT, Flux, rectified flow.
816. [ ] `controlnet` — ControlNet, T2I-Adapter, ControlNet++.
817. [ ] `ip-adapter` — IP-Adapter, image prompt.
818. [ ] `lora-diffusion` — LoRA/DreamBooth/Textual Inversion.
819. [ ] `cfg` — Classifier-free guidance, rescale.
820. [ ] `samplers-image` — Euler, Heun, DPM++, ancestral.
821. [ ] `vae-sd` — SD VAE artifacts, TAESD, tiny VAE.
822. [ ] `upscalers` — Latent vs pixel upscale, SUPIR-class.

### Robotics and embodied extra

823. [ ] `simulators` — MuJoCo, Isaac, Habitat, limits of sim.
824. [ ] `sim2real` — Domain rand, real-world fine-tune.
825. [ ] `imitation-robots` — BC, ACT, Diffusion Policy recap.
826. [ ] `reward-from-video` — RFCL, video rewards, VIP.
827. [ ] `rt-models` — RT-1, RT-2, RT-X, Open X-Embodiment.
828. [ ] `vla-models` — OpenVLA, π0, Paligemma-robot.
829. [ ] `manipulation` — Grasp, IK vs learned, contact.
830. [ ] `navigation` — VLN, maps, frontier, LM planners.
831. [ ] `humanoids` — Open humanoid stacks, limits.
832. [ ] `dataset-robots` — OXE, DROID, what is in the mix.

### Classic ML extras

833. [ ] `glm-stats` — GLMs, logistic, Poisson, links.
834. [ ] `trees-deep` — CART, pruning, heterogeneity.
835. [ ] `boosting` — AdaBoost, GBM, XGBoost internals.
836. [ ] `svm-kernels` — SVM, kernel trick, dual.
837. [ ] `gmms` — EM, GMM, responsibilities.
838. [ ] `pca-ica` — PCA, ICA, whitening.
839. [ ] `factorization` — MF, ALS, implicit feedback.
840. [ ] `imbalanced` — Weights, sampling, PR curves.
841. [ ] `metrics-class` — ROC vs PR, calibration, cost.
842. [ ] `feature-eng` — Target encode, hashes, leaks.
843. [ ] `time-split` — Leakage, rolling origin, embargo.
844. [ ] `experiment-design` — Power, A/A, peeking.

### JAX, compilers, export

845. [ ] `jax-basics` — JIT, grad, vmap, pmap, pytrees.
846. [ ] `flax-linen` — Flax modules, state, scans.
847. [ ] `equinox` — Equinox, Module as pytree.
848. [ ] `optax` — Optax chains, schedules.
849. [ ] `orbax` — Checkpoints in JAX.
850. [ ] `export-onnx` — ONNX export, dynamo, opset traps.
851. [ ] `torch-export` — torch.export, AOT, executorch.
852. [ ] `tensorrt` — TensorRT engines, profiles.
853. [ ] `openvino` — OpenVINO CPU/iGPU paths.
854. [ ] `coreml` — Core ML convert, ANE.

### Datasets, eval culture, community

855. [ ] `hf-datasets-lib` — datasets lib: map, fingerprint, streaming. Not the HF course.
856. [ ] `hf-transformers-lib` — transformers internals: generate, cache, configs. Not the course.
857. [ ] `hf-peft` — PEFT: LoRA, QLoRA, IA3, config.
858. [ ] `hf-accelerate` — Accelerate: multi-GPU without a trainer.
859. [ ] `eleuther-stack` — GPT-NeoX, lm-eval, Pythia.
860. [ ] `pythia` — Pythia suite: intermediate ckpts, influence.
861. [ ] `olmo-stack` — OLMo, paloma eval, fully open.
862. [ ] `bigcode` — BigCode, StarCoder, The Stack.
863. [ ] `laion` — LAION, aesthetic, safety, legal.
864. [ ] `common-crawl` — WARC, WAT, WET, warc2text.
865. [ ] `arena` — Chatbot Arena methodology, style, limits.
866. [ ] `artificial-analysis` — Independent inference/quality indexes. Read methods.

### 2026 frontier topics

867. [ ] `test-time-training` — TTT, inner loop at inference, caches.
868. [ ] `continual-agents` — Agents that keep memory across days.
869. [ ] `self-improving-harness` — Agent patches its own tools under tests.
870. [ ] `computer-use-eval` — OSWorld, AndroidWorld, WindowsAgentArena.
871. [ ] `cli-agents` — Codex/Claude-Code-class CLIs on open models.
872. [ ] `skill-files` — SKILL.md packs: when to load, trust, version.
873. [ ] `mcp-apps` — MCP beyond files: browsers, DBs, CI, Colab.
874. [ ] `long-running-agents` — Hours-long jobs, checkpoints, watchdog.
875. [ ] `agent-teams` — Parallel agents on one repo, merge conflicts.
876. [ ] `open-weight-reasoners` — Open R1-class distillations, s1, OpenThinker.
877. [ ] `s1-budget-forcing` — s1: budget forcing, short extra compute.
878. [ ] `simple-rl-zero` — Tiny-zero / SimpleRL-Zoo: RL from base models.
879. [ ] `openr1` — Open-R1 reproduction stacks.
880. [ ] `deepseek-v4-serve` — Serve V4-Flash/Pro: VRAM, TP, quant, 1M context.
881. [ ] `qwen3-serve` — Serve Qwen3.x MoE and dense coder.
882. [ ] `kimi-serve` — Serve Kimi K2/K3-class MoE.
883. [ ] `glm5-serve` — Serve GLM-5.x MIT MoE.
884. [ ] `llama4-serve` — Serve Llama 4 Scout/Maverick-class.
885. [ ] `hybrid-ssm-attn-2026` — 2026 hybrids: Qwen-Coder-Next, CSA/HCA reports.
886. [ ] `million-context` — 1M–10M windows: memory, RoPE, Engram, Scout.
887. [ ] `video-world-2026` — Open video + world models as of 2026.
888. [ ] `local-cua-2026` — Local computer-use: UI-TARS, a11y, small VLMs.
889. [ ] `eval-agents-2026` — SWE-bench Pro, Terminal-Bench 2, tau2, BFCL.
890. [ ] `moe-routing-2026` — Aux-loss-free, expert choice, shared experts.
891. [ ] `fp4-fp8-2026` — NVFP4 / FP8 training and serve in 2026 stacks.
892. [ ] `disaggregated-serve` — Prefill/decode split, KV transfer, 2026 serve papers.
893. [ ] `spec-decode-2026` — EAGLE-3, MTP drafts, acceptance on reasoners.
894. [ ] `on-policy-distill-2026` — Distill long CoT on-policy into small models.
895. [ ] `open-data-2026` — FineWeb2, DCLM-2026, fully open mixes.
896. [ ] `safety-agents-2026` — Computer-use + MCP security, 2026 incidents as case studies.

## Operator slug list

Same order as Queue. Paste into the cloud automation prompt if that prompt still uses a SLUGS list.

```
speech-audio, multimodal, generative-models, reinforcement-learning, graph-ml, recsys, time-series, causal-ml, interpretability, evals-safety, data-centric, mlops, inference-serving, gpu-systems, distributed-training, compression, coding-agents, embodied-ai, become-ml-engineer, become-researcher, build-gpt2, build-nanogpt, build-llm-c, build-nanochat, build-llm101n, build-deepseek-v3, build-deepseek-v4, build-deepseek-r1, build-moe, build-mla, build-mha, build-gqa-mqa, build-rope, build-kv-cache, build-tokenizer, build-transformer-block, build-llama-arch, build-bert, build-t5, build-vit, build-whisper, build-clip, build-vae, build-gan, build-diffusion, build-flow-matching, build-unet, build-mamba, build-rwkv, build-autograd, build-mlp-numpy, build-cnn-numpy, build-rnn-lstm, build-word2vec, build-optimizers, build-layernorm, build-softmax, build-positional, build-flash-attn, build-speculative-decoding, build-paged-attention, build-bpe-merge, build-sampling, build-chat-template, build-decision-transformer, build-alphazero-tiny, build-gnn-mpnn, build-neural-ode, build-transformer-mt, build-mae, build-nerf-tiny, build-3dgs-tiny, build-wavenet, build-pointer-net, build-memory-net, self-host-llms, self-host-ollama, self-host-llamacpp, self-host-vllm, self-host-sglang, self-host-tgi, self-host-mlx, self-host-exllamav2, self-host-koboldcpp, self-host-tabbyapi, self-host-openwebui, self-host-continue, self-host-aider, self-host-open-interpreter, self-host-comfyui, self-host-automatic1111, self-host-whisper, self-host-tts, self-host-embeddings, self-host-rerankers, self-host-rag, self-host-vector-db, self-host-agent, self-host-mcp, self-host-gateway, self-host-gpu-box, self-host-cpu-only, self-host-docker, self-host-k8s, self-host-auth, self-host-observability, self-host-offline, self-host-multi-lora, self-host-speculative, self-host-vision, self-host-browser-agent, build-eval-harness, lm-eval-harness, openai-evals, swe-bench, swe-bench-harness, swe-gym, terminal-bench, livecodebench, humaneval-plus, mbpp-eval, osworld, webarena, gaia-bench, agentbench, tau-bench, bfcl, ifeval, mt-bench, arena-hard, simpleqa, gpqa, mmlu-pro, hle-eval, math-eval, code-eval-sandbox, llm-as-judge, reward-model-eval, rag-eval, agent-eval, eval-ci, eval-contamination, eval-dynamic, eval-human, build-unit-tests-for-prompts, build-regression-evals, agent-loop, react-agents, tool-calling, mcp-protocol, mcp-build-server, mcp-security, agent-skills, computer-use, browser-agents, browser-harness, desktop-agents, coding-agent-loop, multi-agent, agent-memory, agent-planning, agent-reflection, agent-routing, agent-handoff, agent-sandbox, agent-secrets, agent-observability, agent-cost, agent-eval-loop, a2a-protocol, openai-agents-sdk, claude-agent-sdk, langgraph-agents, crewai-agents, autogen-agents, smolagents, pydanticai-agents, goose-agents, opencode-agents, aider-deep, continue-deep, cursor-agent-internals, swe-agent, openhands, devin-style-agents, ui-tars, browser-use, skyvern, playwright-mcp, agent-browser, computer-use-local, llama-family, qwen-family, deepseek-family, kimi-family, glm-family, gemma-family, mistral-family, phi-family, olmo-family, map-neo-family, yi-family, internlm-family, minimax-family, cohere-aya, falcon-family, stablelm-family, rwkv-family, mamba-family, dbrx-family, grok-open-weights, trinity-arcee, ring-ling, stepfun-models, nanbeige-models, muse-glimmer, attention-variants, normalization-llm, activations-llm, embeddings-tokens, context-length, yarn-ntk, alibi, infini-attention, ring-attention, hybrid-architectures, multi-token-prediction, mixture-of-depths, early-exit, matryoshka-reps, qk-clip, attention-sinks, softcapping, width-depth, scaling-laws, grokking, double-descent, lottery-ticket, ntk-lazy, feature-learning, loss-spikes, training-stability, init-llm, precision-training, sequence-packing, data-parallel-llm, tensor-parallel-llm, pipeline-parallel-llm, expert-parallel, context-parallel, fsdp2, zero-stages, activation-checkpoint, compiler-pytorch, xla-jax, numerics-softmax, sft, instruction-tuning, chat-sft-data, dpo, orpo, kto, ipo-simpo, ppo-llm, grpo, dapo, gspo, rlaif, rlhf, reward-models, process-reward, outcome-reward, rejection-sampling, constitutional-ai, online-dpo, test-time-compute, chain-of-thought, tree-of-thoughts, self-consistency, mcts-llm, verifiers, best-of-n, reasoning-models, hybrid-thinking, tool-integrated-reason, search-augmented-reason, embeddings-models, dense-retrieval, sparse-retrieval, hybrid-search, colbert, cross-encoders, chunking, parent-document, contextual-retrieval, hyde, query-rewrite, raptor, graphrag, agentic-rag, code-rag, multimodal-rag, long-context-vs-rag, citation-grounding, hallucination-detect, vector-indexes, faiss-deep, ann-theory, embedding-finetune, instruction-retrieval, multilingual-rag, cuda-mental-model, gpu-memory-hierarchy, tensor-cores, mixed-precision, profiling-gpu, kernel-fusion, triton-kernels, cutlass, cuda-graphs, streams-events, nccl, nvlink-infiniband, rocm, metal-mps, webgpu-inference, flashdecoding, fused-moe-kernel, attention-kernel-zoo, quant-kernels, pytorch-memory, activation-memory, batch-size-tuning, compile-inductor, ptx-sass, multi-gpu-one-node, data-parallel, fsdp, tensor-parallel, pipeline-parallel, 3d-parallel, deepspeed, megatron-core, fairscale, colossal-ai, composer-mosaic, torchtitan, nemo, axolotl, unsloth, trl-train, ray-train, slurm-ml, checkpointing, multi-node-debug, elastic-train, continuous-batching, prefix-caching, chunked-prefill, scheduler-vllm, sglang-radix, constrained-decoding, structured-output, grammar-sampling, speculation-eagle, medusa-heads, draft-models, kv-quant, cache-eviction, long-prefill, disagg-prefill-decode, lora-serving, routing-inference, load-balancing-llm, streaming-tokens, batching-metrics, openai-compat-server, tokenizer-fast-path, quantization, gptq, awq, gguf-quants, smoothquant, quarot-spinquant, bitnet, fp8-inference, mxfp, kv-cache-quant, pruning-llm, structured-sparsity, distillation-llm, speculative-distill, small-models, matryoshka-quant, ggml-backend, safetensors, pretraining-data, fineweb, dclm, dolma, the-pile, redpajama, star-coder-data, dedup, quality-classifier, pii-filter, toxicity-filter, synthetic-pretrain, annealing-data, data-mix, tokenization-data, packing-docs, continual-pretrain, unlearning-data, dataset-cards, synthetic-sft, convnets-modern, detection, detr, segmentation, sam, grounding-dino, yolo-family, ocr, document-ai, depth, optical-flow, tracking, self-supervised-vision, dino-dinov2, mae-vit, clip-siglip, open-vocab, video-understanding, action-recognition, nerf, gaussian-splatting, point-clouds, equivariant-vision, medical-vision, efficient-vision, video-generation, hunyuan-video, wan-video, cogvideox, ltx-video, svd, dit-video, world-models, dreamer, jepa, lecun-path, genie, oasis-world, video-tokenizer, temporal-consistency, control-video, 4d-generation, scene-reconstruction, slam-learning, occupancy, openvla, diffusion-policy, act-policy, pi0-vla, asr-deep, wav2vec, hubert, whisper-deep, speecht5, tts-deep, neural-codecs, audioldm, musicgen, voice-conversion, diarization, speaker-id, kws, audio-ssl, speech-translation, streaming-asr, enhancement, codec-lm, flamingo, blip, llava, qwen-vl, internvl, molmo, paligemma, florence, any-to-any, image-tokenization, mm-rope, grounded-vlm, video-llm, audio-llm, document-vlm, mm-eval, mm-rag, mm-agents, mdp-bellman, mc-td, q-learning-deep, policy-gradient, actor-critic, ppo, sac, td3, trpo-acktr, dqn-rainbow, offline-rl, offline-to-online, model-based-rl, mu-zero, alpha-zero, mcts, bandits, imitation, hierarchical-rl, multi-agent-rl, rl-engineering, gflownets, decision-transformer-rl, gcn, graphsage, gat, gin, graph-transformers, hetero-graphs, temporal-graphs, kg-completion, two-tower, dlrm, sasrec, bert4rec, ranking-losses, rec-metrics, patchtst, tft, nbeats, deepar, conformal, causal-graphs, ate-cate, iv-dml, uplift, synthetic-control, alphafold, esm, boltz, docking, mol-gen, materials, graphcast, neural-operators, pinns, geometric-dl, e3nn, neural-ode-sci, tabular-dl, tabpfn, gbdt-vs-nets, anomaly, umap-tsne, clustering-deep, active-learning, weak-supervision, semi-supervised, domain-adaptation, meta-learning, neural-process, gaussian-processes, bayesian-dl, calibration, uncertainty, circuits, sae, activation-patching, logit-lens, probing, attribution, shap-lime, influence, model-editing, knowledge-conflicts, sycophancy, deception-evals, jailbreaks, prompt-injection, guardrails, watermarking, ai-text-detect, membership-inference, extraction, unlearning, fairness, privacy-ml, federated, scalable-oversight, weak-to-strong, model-spec, red-team, eval-alignment, mech-interp-toolkit, toy-models-superpos, experiment-tracking, model-registry, data-versioning, feature-store, training-jobs, ci-for-ml, drift, monitoring-llm, ab-test-models, canary-models, fastapi-ml, bentoml, ray-serve, kserve, batch-inference, online-inference, prompt-versioning, golden-datasets, llm-observability, langfuse, phoenix-arize, cost-control, slo-ml, incident-ml, repro-seeds, linalg-ml, matrix-calc, probability-ml, info-theory, stats-est, pac-bayes, opt-convex, opt-nonconvex, adamw-deep, muon-optimizer, shampoo-soap, lion-sophia, schedules, sam-optimizer, regularization, normalization-math, kernel-methods, spectral, optimal-transport, score-matching, tokenization-nlp, pos-ner, parsing, coref, summarization, mt, multilingual-llm, low-resource-nlp, ie-re, topic-models, sentiment, style-transfer, dialogue-state, factual-probing, codex-history, starcoder, codellama, deepseek-coder, qwen-coder, codestral, fim, repo-level-code, code-repair, test-gen, code-rag-index, formal-llm, diff-apply, program-analysis-llm, code-eval-beyond, terminal-agents, context-engineering, needle-haystack, long-context-arch, recurrent-memory, memgpt, graph-memory, summarize-memory, kv-offload, engram-memory, yarn-long, packing-long, lost-in-middle, infinite-context-eval, json-mode, outlines, xgrammar, guidance, instructor, tool-parsers, parallel-tools, sql-tools, browser-tools, code-interpreter, retrieval-as-tool, human-in-loop, output-repair, on-device-llm, llama-cpp-mobile, execu-torch, mlc-llm, web-llm, tiny-ml, distill-on-device, federated-llm, dp-finetune, secure-inference, local-first-ai, license-weights, read-a-paper, reproduce-result, ablations, error-analysis, write-a-paper, review-a-paper, open-release, model-cards, benchmark-hygiene, negative-results, compute-budget, lit-review, paper-attention, paper-gpt2, paper-gpt3, paper-chinchilla, paper-instructgpt, paper-llama, paper-moe, paper-mla, paper-r1, paper-v4, paper-dit, paper-ldm, paper-whisper, paper-clip, paper-sam, paper-alphafold, paper-muzero, paper-ppo, paper-dpo, paper-lora, paper-flashattn, paper-vllm, paper-mamba, paper-jepa, warmup-decay, grad-clip, loss-functions-llm, label-smoothing, dropout-llm, weight-tying, seq-len-curriculum, overtrain, distill-on-policy, ema, stochastic-depth, mixup-cutmix, gradient-accum, microbatch, data-order, eval-during-train, hyperparam-transfer, spikiness, encoder-decoder, prefix-lm, retnet, hyena, s4-ssm, griffin-hawk, jamba, recurrent-gemma, linear-attention, state-space-llm, mixture-of-recursions, universal-transformer, hourglass, perceiver, gmlp-mlp-mixer, kan, prompt-structure, few-shot-design, cot-prompting, decomp-prompting, self-ask, generated-knowledge, prompt-caching, context-distill, system-prompt, eval-prompts, score-diffusion, ddim, consistency-models, latent-diffusion, sd3-flux, controlnet, ip-adapter, lora-diffusion, cfg, samplers-image, vae-sd, upscalers, simulators, sim2real, imitation-robots, reward-from-video, rt-models, vla-models, manipulation, navigation, humanoids, dataset-robots, glm-stats, trees-deep, boosting, svm-kernels, gmms, pca-ica, factorization, imbalanced, metrics-class, feature-eng, time-split, experiment-design, jax-basics, flax-linen, equinox, optax, orbax, export-onnx, torch-export, tensorrt, openvino, coreml, hf-datasets-lib, hf-transformers-lib, hf-peft, hf-accelerate, eleuther-stack, pythia, olmo-stack, bigcode, laion, common-crawl, arena, artificial-analysis, test-time-training, continual-agents, self-improving-harness, computer-use-eval, cli-agents, skill-files, mcp-apps, long-running-agents, agent-teams, open-weight-reasoners, s1-budget-forcing, simple-rl-zero, openr1, deepseek-v4-serve, qwen3-serve, kimi-serve, glm5-serve, llama4-serve, hybrid-ssm-attn-2026, million-context, video-world-2026, local-cua-2026, eval-agents-2026, moe-routing-2026, fp4-fp8-2026, disaggregated-serve, spec-decode-2026, on-policy-distill-2026, open-data-2026, safety-agents-2026
```
