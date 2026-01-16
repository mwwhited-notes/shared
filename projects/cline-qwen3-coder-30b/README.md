# Cline CLI with Local LLM Models

**Status**: Planning | **Type**: AI / Development Tools | **Hardware**: RTX 4070 Ti (12GB VRAM)

---

## Overview

Local LLM-powered Cline CLI integration for code generation and assistance without cloud API dependencies. Testing Qwen3 Coder 30b 4-bit and Qwen2 7b/14b models served via Ollama REST API. Goal is to establish a private, low-latency coding assistant for embedded systems, hardware projects, and FPGA development.

**Advantages of Local Setup:**
- Code stays private (no cloud uploads) - critical for proprietary projects
- Zero API costs and token limits
- Instant availability without rate limiting
- Ability to fine-tune or customize models later

**Goals:**
- Set up Ollama with Qwen3 Coder 30b 4-bit (primary) and Qwen2 variants (fallback)
- Configure Cline CLI to use local Ollama API endpoint
- Benchmark memory/latency on 12GB RTX 4070 Ti
- Evaluate coding quality across project domains (embedded, FPGA, .NET, Python)
- Determine best model size/quantization for this VRAM constraint
- Document setup and Cline configuration

---

## Project Details

### Model Specifications

#### Primary Model: Qwen3 Coder 30b 4-bit
| Aspect | Details |
|--------|---------|
| **Parameters** | 30B (30 billion) |
| **Quantization** | 4-bit GGUF (memory-optimized) |
| **Estimated VRAM** | ~10-11GB (fits in 12GB RTX 4070 Ti) |
| **Context Window** | Up to 32K tokens |
| **Inference Speed** | Expected 10-20 tokens/sec on RTX 4070 Ti |
| **Strengths** | Code generation, embedded systems, FPGA-aware |
| **Tradeoffs** | Slower than unquantized; quality vs speed balance |

#### Fallback Models: Qwen2 7b/14b
| Model | VRAM Needed | Speed | Use Case |
|-------|------------|-------|----------|
| **Qwen2 7b** | ~4-5GB | ~30-40 tokens/sec | Quick iterations, fallback |
| **Qwen2 14b** | ~8-9GB | ~15-25 tokens/sec | Balance, if 30b too slow |

### Evaluation Criteria

**Functional:**
- Code generation accuracy across different languages (Python, SystemVerilog, C#, ANTLR, Verilog)
- Embedded systems knowledge (Arduino, ARM, FPGA-related)
- Protocol implementation quality (SCPI, Modbus, custom protocols)
- Test case generation

**Performance:**
- Inference latency (first token, subsequent tokens)
- Memory consumption (VRAM, system RAM)
- Throughput (tokens/second)
- Quantization impact on quality vs baseline models

**Integration:**
- Cline compatibility and setup process
- VS Code / IDE integration smoothness
- Error handling and fallback behavior
- Session management and context handling

### Project Domains to Test

1. **Embedded Systems** - Arduino sketches, ATtiny/STM32 C code
2. **FPGA/HDL** - SystemVerilog, Verilog for SAP-1, CPU design projects
3. **Protocol Engineering** - SCPI, Modbus, custom serial protocols
4. **.NET Development** - C# code generation, dotex framework extensions
5. **Python** - Data analysis, ML model code, utilities
6. **Hardware Documentation** - README generation, pinout tables, schematic analysis

---

## Setup & Prerequisites

### Hardware Configuration

**Available:**
- **GPU:** Nvidia RTX 4070 Ti 12GB VRAM ⭐ Primary constraint
- **System RAM:** Assume 32GB+ (typical workstation)
- **Storage:** SSD with 50GB+ free space (models ~15-20GB total)

**VRAM Allocation Strategy for 12GB RTX 4070 Ti:**
```
Total VRAM: 12,288 MB

Usage breakdown:
- Qwen3 30b 4-bit: ~10,000 MB (KV cache, weights)
- OS/Driver overhead: ~500 MB
- Ollama/inference overhead: ~300 MB
- Headroom/safety margin: ~488 MB
────────────────────────────
Total: ~11,288 MB (tight but viable)
```

**Risk:** Memory is tight; may need to carefully manage batch sizes and context lengths.

### Software Stack

- **Inference Server:** Ollama (REST API, handles model management)
- **CLI Tool:** Cline (configured to use Ollama API endpoint)
- **Model Source:** Hugging Face/ollama.ai (quantized GGUF format)
- **Host OS:** Windows, WSL2, or Linux
- **Evaluation Scripts:** Python, Bash (for benchmarking)

---

## Implementation Plan

### Phase 1: Ollama + Model Setup
- [ ] Install Ollama (Windows/WSL2 or Linux)
- [ ] Pull Qwen3 Coder 30b 4-bit model (`ollama pull qwen3-coder`)
- [ ] Verify model loads and VRAM usage is acceptable (<12GB)
- [ ] Test Ollama API endpoint (port 11434 by default)
- [ ] Create baseline performance test script (first token, throughput)

### Phase 2: Cline CLI Integration
- [ ] Install Cline CLI (`npm install -g @cline/cli`)
- [ ] Configure Cline to use local Ollama endpoint instead of cloud API
- [ ] Edit Cline config/env to point to `http://localhost:11434`
- [ ] Test basic code generation prompt
- [ ] Document configuration steps

### Phase 3: Functional Testing (Multiple Models)
**Primary: Qwen3 30b 4-bit**
- [ ] Embedded systems: Arduino/ATtiny C code generation
- [ ] FPGA: Verilog for SAP-1 components
- [ ] Protocol: SCPI command parser implementation
- [ ] .NET: C# utility function generation
- [ ] Record latency and memory usage per test

**Fallback: Qwen2 7b/14b**
- [ ] Run same tests to compare quality/speed
- [ ] Determine if smaller models acceptable for iteration speed

### Phase 4: Performance Benchmarking
- [ ] Measure first-token latency (goal: <2s)
- [ ] Measure generation speed (tokens/sec)
- [ ] Profile VRAM usage over long sessions
- [ ] Test context window limits (max useful context)
- [ ] Create benchmark results table

### Phase 5: Documentation & Handoff
- [ ] Record working setup instructions
- [ ] Create Cline config template for future use
- [ ] Document known limitations on 12GB VRAM
- [ ] Store best-performing model recommendation
- [ ] Add project to future development workflow

---

## Key Questions to Answer

1. **Coding Quality:** Does Qwen3 30b match Claude/GPT-4 quality for embedded/FPGA domains?
2. **Embedded Competency:** How well does it understand Arduino, AVR, ARM assembly patterns?
3. **HDL Support:** Can it generate correct SystemVerilog/Verilog for logic synthesis?
4. **Context Handling:** How effectively does it maintain context across multi-file projects?
5. **Performance Trade-off:** Is 4-bit quantization acceptable for code generation tasks?
6. **Integration Friction:** How smooth is local model integration vs cloud APIs?
7. **Cost/Benefit:** Does local inference justify latency vs cloud convenience?

---

## Evaluation Metrics

### Code Quality Metrics
- Syntax correctness (compilation/linting passes)
- Functional correctness (logic matches specification)
- Performance (algorithmic efficiency)
- Readability (follows project conventions)
- Completeness (includes error handling, edge cases)

### Performance Metrics
```
- First token latency: <2s (acceptable interactive use)
- Generation speed: >5 tokens/sec (streaming acceptable)
- Memory peak usage: <20GB VRAM
- Session stability: Zero crashes over 24-hour usage
```

### Integration Metrics
- Setup time (minutes to working Cline + model)
- Error recovery time
- Context switch overhead

---

## Expected Outcomes

**Deliverables:**
1. Evaluation report with findings by code domain
2. Performance benchmark results
3. Cline configuration templates
4. Recommended use cases and limitations
5. Cost-benefit analysis (GPU compute vs cloud API costs)

**Knowledge Gain:**
- Local LLM inference patterns
- Qwen3 architectural understanding
- Cline integration best practices
- Quantization impact on code generation

---

## References & Resources

### Inference & Model Tools
- **[Ollama](https://ollama.ai/)** - Model management and REST API server (primary)
  - Install: Supports Windows, macOS, Linux
  - Model library: `ollama pull <model-name>`
  - API: Runs on `http://localhost:11434` by default
  - GGUF format with quantization support

- **[Cline CLI](https://github.com/cline/cline)** - AI code assistant for CLI
  - Install: `npm install -g @cline/cli`
  - Supports local model API endpoints
  - Can be integrated with project CI/CD

### Model Sources
- **Qwen3 Coder:** [Alibaba Qwen GitHub](https://github.com/QwenLM/Qwen)
- **Hugging Face:** [Qwen models](https://huggingface.co/Qwen)
- **Ollama Model Library:** Search for `qwen3-coder`, `qwen2` variants
- **TheBloke:** Common quantized GGUF versions of popular models

### Performance & Monitoring
- NVIDIA GPU utilities: `nvidia-smi` (monitor VRAM usage)
- Ollama debug mode: `OLLAMA_DEBUG=1 ollama serve`
- Benchmark tools: Python `time` module, Bash `time` command

### Relevant Projects
- [ai-ml-research/](../ai-ml-research/) - AI/ML research notes
- [vector-search-sqlserver/](../vector-search-sqlserver/) - Prior ML integration
- [devops-playground-cluster/](../devops-playground-cluster/) - GPU-capable hardware

---

## Implementation Notes

### VRAM Management (Critical for 12GB)
- **Monitor during startup:** Use `nvidia-smi` to watch VRAM during model load
- **If OOM errors occur:** Try Qwen2 14b or smaller model
- **Batch size:** May need to reduce for inference to fit in 12GB
- **Context length:** Longer contexts consume more VRAM for KV cache; test limits empirically

### Cline CLI Configuration

**Host Installation:**
```bash
# Set Ollama endpoint (check Cline docs for exact config location)
export OLLAMA_API_URL=http://localhost:11434
# or set in ~/.cline/config.json or equivalent
```

**Docker Container Setup (Recommended):**

Run Cline in a Docker container with working directory mapped (like Claude Code), keeping host clean:

```bash
# Start Ollama server on host (or in separate container)
ollama serve

# In another terminal, run Cline in Docker with current directory mapped
docker run -it --rm \
  -v "%CD%":/workspace \
  -e OLLAMA_API_URL=http://host.docker.internal:11434 \
  node:20-slim bash -c "npm install -g @cline/cli && cd /workspace && cline"
```

**For persistent Cline container with alias:**

Windows (PowerShell):
```powershell
# Add to profile or create alias
function cline-docker {
    docker run -it --rm `
      -v "$pwd":/workspace `
      -e OLLAMA_API_URL=http://host.docker.internal:11434 `
      node:20-slim bash -c "npm install -g @cline/cli && cd /workspace && cline"
}
```

Windows (cmd.bat):
```batch
@echo off
docker run -it --rm ^
  -v "%CD%":/workspace ^
  -e OLLAMA_API_URL=http://host.docker.internal:11434 ^
  node:20-slim bash -c "npm install -g @cline/cli && cd /workspace && cline"
```

Linux/macOS:
```bash
docker run -it --rm \
  -v "$PWD":/workspace \
  -e OLLAMA_API_URL=http://host.docker.internal:11434 \
  node:20-slim bash -c "npm install -g @cline/cli && cd /workspace && cline"
```

**Key Points:**
- `host.docker.internal` = host machine from inside Docker container
- `-v` mounts working directory into `/workspace` in container
- `-e` sets Ollama API endpoint for Cline to discover local model
- `--rm` deletes container after exit (clean workspace)
- Pre-installs npm/node so Cline CLI available immediately

### Performance Expectations
| Metric | Target | Notes |
|--------|--------|-------|
| First token | <2s | Acceptable for interactive use |
| Throughput | 10-20 tok/s | Qwen3 30b at 12GB is slower than cloud |
| Memory peak | <11.5GB | Leave headroom to prevent crashes |
| Session duration | 24+ hours | Should be stable long-term |

### Development Workflow Integration
- Use local Qwen for rapid iteration (no API costs, instant startup)
- Compare critical outputs with cloud models as needed
- Cache good prompts for future reference
- Consider using smaller Qwen2 model for initial brainstorming

### Troubleshooting Checklist
- [ ] `nvidia-smi` shows RTX 4070 Ti with 12GB
- [ ] Ollama running: `curl http://localhost:11434/api/tags`
- [ ] Model loaded: Check Ollama output logs
- [ ] Cline can connect: Test with simple prompt
- [ ] VRAM stays <12GB: Monitor with `nvidia-smi -l 1`

---

## Progress Tracking

| Phase | Status | Notes |
|-------|--------|-------|
| Setup | Not started | Awaiting first session |
| Integration | Not started | |
| Testing | Not started | |
| Benchmarking | Not started | |
| Documentation | In progress | Project README created |

---

**Project Created:** 2026-01-16
**Last Updated:** 2026-01-16
**Status:** Ready for setup and testing
