# HuggingFace Models in .NET: Native Execution Research

## Overview

This research project explores options for running HuggingFace transformer models natively in .NET applications **without calling out-of-process to Python**. It covers ONNX conversion workflows, native .NET inference engines, tokenizer implementations, and code generation approaches.

## Problem Statement

HuggingFace provides powerful pre-trained models (BERT, GPT-2, T5, etc.) with easy-to-use AutoModel/AutoConfig/AutoTokenizer APIs in Python. However, .NET developers face challenges:

- **No direct .NET equivalent** of HuggingFace transformers library
- **Out-of-process Python calls** add complexity, latency, and deployment overhead
- **Need for native .NET solutions** that can run models entirely in-process

## Solution Approaches

This research documents several viable approaches for native .NET execution:

### 1. **ONNX Runtime + ML.NET** (Recommended for Production)
Export HuggingFace models to ONNX format, then run inference using Microsoft.ML.OnnxRuntime or ML.NET. This is the most mature and well-supported approach.

### 2. **TorchSharp** (Native PyTorch in .NET)
Use TorchSharp (official .NET bindings for LibTorch) to run PyTorch models directly or load converted weights. Supports both inference and training.

### 3. **Transformers.NET** (Community Library)
Built on TorchSharp, provides a more HuggingFace-like API for running and training transformer models with automatic model provisioning from HuggingFace Hub.

### 4. **Code Generation / Precompilation** (Experimental)
Transform model definitions into compiled C# code for maximum performance and no runtime reflection. Less mature but offers interesting possibilities.

### 5. **Semantic Kernel Integration** (AI Orchestration)
Microsoft's AI orchestration framework with built-in HuggingFace connectors for higher-level application development.

## Repository Structure

```
huggingface-dotnet-native-execution/
├── README.md                           # This file - project overview
├── TECHNOLOGY_COMPARISON.md            # Detailed comparison matrix of all approaches
├── ONNX_CONVERSION_WORKFLOW.md         # Step-by-step ONNX export and deployment guide
├── IMPLEMENTATION_GUIDES.md            # Practical implementation scenarios
├── RESEARCH_BIBLIOGRAPHY.md            # Comprehensive resource list (100+ links)
├── documents/                          # Downloaded PDFs, papers, standards
│   └── (standards, whitepapers, etc.)
└── examples/                           # Code examples for each approach
    ├── onnx-bert-sentiment/
    ├── torchsharp-gpt2/
    └── transformers-net-demo/
```

## Quick Start Scenarios

### Scenario 1: BERT Sentiment Analysis (ONNX)
1. Export BERT model to ONNX using HuggingFace Optimum
2. Install `Microsoft.ML.OnnxRuntime` and `Tokenizers.HuggingFace` NuGet packages
3. Load ONNX model and run inference in C#

**Best for:** Production deployments, CPU inference, maximum compatibility

### Scenario 2: GPT-2 Text Generation (TorchSharp)
1. Load GPT-2 weights using TorchSharp.PyBridge
2. Build model architecture in TorchSharp
3. Run generation loop in C#

**Best for:** Research, custom training, GPU acceleration

### Scenario 3: Auto-Loading Models (Transformers.NET)
1. Install Transformers.NET NuGet package
2. Use HuggingFace model IDs to auto-download and run models
3. No manual export needed

**Best for:** Rapid prototyping, HuggingFace Hub integration

See [IMPLEMENTATION_GUIDES.md](./IMPLEMENTATION_GUIDES.md) for detailed code examples.

## Technology Maturity Assessment

| Approach | Maturity | Community Support | Performance | Ease of Use |
|----------|----------|-------------------|-------------|-------------|
| ONNX Runtime + ML.NET | ⭐⭐⭐⭐⭐ Production | Microsoft + Community | Excellent (optimized) | Good |
| TorchSharp | ⭐⭐⭐⭐ Stable | Microsoft .NET Foundation | Excellent (GPU) | Moderate |
| Transformers.NET | ⭐⭐⭐ Community | Active development | Good | Excellent |
| Code Generation | ⭐ Experimental | Research-stage | Variable | Complex |
| Semantic Kernel | ⭐⭐⭐⭐ Stable | Microsoft | Good | Excellent (AI apps) |

## Key Findings

### ONNX is the Most Mature Path
- **130,000+ HuggingFace models** supported by ONNX Runtime
- **Official Microsoft support** via ML.NET integration
- **Cross-platform** (Windows, Linux, macOS)
- **Hardware acceleration** (CPU, GPU, DirectML, CoreML, etc.)
- **Production-ready** with extensive documentation

### Native Tokenizers Available
Three main options for tokenization in .NET:
1. **Tokenizers.HuggingFace** (NuGet) - Native bindings to Rust tokenizers library
2. **Tokenizers.DotNet** - Community wrapper with .NET 6.0+ support
3. **BERTTokenizers** - Specialized for BERT models with ML.NET

### TorchSharp Enables Full PyTorch Capabilities
- Direct access to PyTorch's LibTorch via C#/F# APIs
- Load pretrained weights from Python PyTorch
- Train and fine-tune models entirely in .NET
- Active development by .NET Foundation

### Conversion Tools Mature and Easy
- **HuggingFace Optimum** CLI: `optimum-cli export onnx --model <model-name> <output-dir>`
- **Programmatic export** via Optimum Python API
- **80+ model architectures** with ORT support out-of-box
- **Automated quantization** and optimization available

## Cross-References to Related Projects

From Matt's GitHub repositories:

### .NET Libraries & Frameworks
- [dotex](https://github.com/OutOfBandDevelopment/dotex) - .NET extensions framework
- [oobtainium](https://github.com/OutOfBandDevelopment/oobtainium) - Mocking framework
- [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders) - Encoding/decoding libraries

### Embedded & Hardware Projects
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - Multi-platform embedded work (potential edge deployment targets)

**Note:** This research focuses on cloud/desktop .NET deployment. Edge device deployment (embedded systems) would require additional consideration of model size, quantization, and hardware constraints.

## Next Steps

1. **Implement proof-of-concept examples** for each approach (ONNX, TorchSharp, Transformers.NET)
2. **Performance benchmarking** across different models and hardware
3. **Document deployment patterns** for ASP.NET Core, desktop apps, Azure Functions
4. **Explore quantization** for reduced model size and faster inference
5. **Investigate code generation** approaches for compile-time model embedding

## Contributing

This is a research repository documenting native .NET execution of HuggingFace models. For implementation questions:

- **ONNX Runtime:** [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime)
- **TorchSharp:** [dotnet/TorchSharp](https://github.com/dotnet/TorchSharp)
- **ML.NET:** [dotnet/machinelearning](https://github.com/dotnet/machinelearning)
- **Transformers.NET:** [tauerlund/Transformers.NET](https://github.com/tauerlund/Transformers.NET)

## License

Documentation and research findings are provided for educational purposes. Respect licenses of referenced libraries and models.

---

**Last Updated:** 2026-01-19
**Author:** Matt Whited ([mwwhited](https://github.com/mwwhited))
**Organization:** [mwwhited-notes](https://github.com/mwwhited-notes)
