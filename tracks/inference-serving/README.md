# Inference & Serving

Goal: Run and benchmark LLM inference with quantization, KV caching, batching, llama.cpp, and vLLM.

Prereqs: [Python for ML](../python-for-ml/) and [LLMs](../llms/), plus basic command-line use and HTTP requests.

Status: done

Start with a small model that fits your hardware. The llama.cpp server supports CPU inference; vLLM examples need a supported hardware setup. The readings are free, and local serving avoids paid API calls. Compare memory use, response quality, latency, and throughput on the same workload.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Prefill, decoding, and continuous batching | | [NVIDIA — Inference Optimization](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/) |
| 2 | Reuse attention keys and values | | [Hugging Face — How caching works](https://huggingface.co/docs/transformers/cache_explanation) |
| 3 | Quantize weights and assess quality loss | | [llama.cpp — GGUF conversion and quantization](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md) |
| 4 | Serve a local model over HTTP | | [llama.cpp — Server build, requests, and health checks](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) |
| 5 | PagedAttention and KV memory sharing | | [vLLM — Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html) |
| 6 | Serve requests with vLLM | | [vLLM — OpenAI-Compatible Server](https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/) |
| 7 | Reuse shared prompt prefixes | | [vLLM — Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) |
| 8 | Measure throughput and token latency | | [vLLM — Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/) |
