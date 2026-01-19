# Research Bibliography

## Overview

Comprehensive resource list for running HuggingFace transformer models natively in .NET, organized by topic.

---

## Official Documentation

### ONNX Runtime

1. [ONNX Runtime | Home](https://onnxruntime.ai/)
   - Official ONNX Runtime website with documentation and tutorials

2. [ONNX Runtime | Huggingface](https://onnxruntime.ai/huggingface)
   - Dedicated page for HuggingFace model support

3. [Accelerate Hugging Face models](https://onnxruntime.ai/docs/tutorials/huggingface.html)
   - Tutorial on using ONNX Runtime with HuggingFace models

4. [Inference BERT NLP with C#](https://onnxruntime.ai/docs/tutorials/csharp/bert-nlp-csharp-console-app.html)
   - Official C# tutorial for BERT inference

5. [Inference Stable Diffusion with C# and ONNX Runtime](https://onnxruntime.ai/docs/tutorials/csharp/stable-diffusion-csharp.html)
   - Advanced tutorial for vision models in C#

6. [Install ONNX Runtime](https://onnxruntime.ai/docs/install/)
   - Installation guide for all platforms and languages

### HuggingFace Optimum

7. [Optimum Inference with ONNX Runtime](https://huggingface.co/docs/optimum-onnx/onnxruntime/usage_guides/models)
   - Official HuggingFace guide for ONNX model export

8. [ONNX Runtime Models - Package Reference](https://huggingface.co/docs/optimum-onnx/en/onnxruntime/package_reference/modeling)
   - API reference for Optimum ONNX Runtime classes

9. [Exporting 🤗 Transformers models to ONNX](https://huggingface.co/docs/transformers/main_classes/onnx)
   - Official transformers library ONNX export documentation

10. [Convert Transformers to ONNX with Hugging Face Optimum](https://huggingface.co/blog/convert-transformers-to-onnx)
    - Blog post with detailed export examples

11. [Export to ONNX](https://huggingface.co/docs/transformers/serialization)
    - Transformers serialization documentation

12. [ONNX](https://huggingface.co/docs/transformers/v4.44.2/en/serialization)
    - Version-specific ONNX export guide

### Microsoft ML.NET

13. [Introduction to Semantic Kernel | Microsoft Learn](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
    - Official Semantic Kernel documentation

14. [OnnxTransformer Class | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/microsoft.ml.transforms.onnx.onnxtransformer?view=ml-dotnet)
    - API reference for ML.NET ONNX transformer

15. [TextClassificationTrainer Class | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/microsoft.ml.torchsharp.nasbert.textclassificationtrainer?view=ml-dotnet-preview)
    - ML.NET TorchSharp-based text classification API

16. [Windows ML APIs | Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/api-reference)
    - Windows ML (ONNX Runtime integration) documentation

17. [ONNX Runtime versions shipped in Windows ML | Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/onnx-versions)
    - Version compatibility information

---

## GitHub Repositories

### Microsoft Official

18. [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime)
    - ONNX Runtime: cross-platform, high performance ML inferencing and training accelerator

19. [dotnet/machinelearning](https://github.com/dotnet/machinelearning)
    - ML.NET main repository

20. [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)
    - Semantic Kernel: Integrate cutting-edge LLM technology quickly and easily into your apps

21. [microsoft/AzureML-BERT](https://github.com/microsoft/AzureML-BERT)
    - End-to-End recipes for pre-training and fine-tuning BERT using Azure Machine Learning Service

22. [microsoft/onnxruntime-training-examples](https://github.com/microsoft/onnxruntime-training-examples)
    - Examples for ONNX Runtime training (includes GPT-2 discussions)

### TorchSharp

23. [dotnet/TorchSharp](https://github.com/dotnet/TorchSharp)
    - A .NET library that provides access to the library that powers PyTorch

24. [TorchSharp: Sharing Model Data between PyTorch and TorchSharp](https://github.com/dotnet/TorchSharp/wiki/Sharing-Model-Data-between-PyTorch-and-TorchSharp)
    - Wiki page on model interoperability

25. [TorchSharp/docfx/articles/saveload.md](https://github.com/dotnet/TorchSharp/blob/main/docfx/articles/saveload.md)
    - Documentation on saving and loading models

26. [TorchSharp: Creating Your Own TorchSharp Modules](https://github.com/dotnet/TorchSharp/wiki/Creating-Your-Own-TorchSharp-Modules)
    - Guide for building custom neural network modules

27. [shaltielshmid/TorchSharp.PyBridge](https://github.com/shaltielshmid/TorchSharp.PyBridge)
    - A library enabling easy transfer and handling of PyTorch models between .NET and Python

### Community Projects

28. [tauerlund/Transformers.NET](https://github.com/tauerlund/Transformers.NET)
    - Run and train Transformer based Large Language Models (LLMS) natively in .NET using TorchSharp

29. [sappho192/Tokenizers.DotNet](https://github.com/sappho192/Tokenizers.DotNet)
    - [Unofficial] Simple .NET wrapper of HuggingFace Tokenizers library

30. [NMZivkovic/BertTokenizers](https://github.com/NMZivkovic/BertTokenizers)
    - Open source project for BERT Tokenizers in C#

31. [Gigabyte0x1337/BERT-ML.NET](https://github.com/Gigabyte0x1337/BERT-ML.NET)
    - BERT Model for dotnet ML

32. [ksanman/AllMiniLML6v2Sharp](https://github.com/ksanman/AllMiniLML6v2Sharp)
    - .NET Standard 2.1 Library for running Sentence Transformers All-MiniLM-L6-v2 from C#

### HuggingFace Official

33. [huggingface/transformers](https://github.com/huggingface/transformers)
    - 🤗 Transformers: state-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX

34. [huggingface/tokenizers](https://github.com/huggingface/tokenizers)
    - 💥 Fast State-of-the-Art Tokenizers optimized for Research and Production

35. [huggingface/optimum-onnx](https://github.com/huggingface/optimum-onnx)
    - 🤗 Optimum ONNX: Export your model to ONNX and run inference with ONNX Runtime

36. [huggingface/notebooks](https://github.com/huggingface/notebooks)
    - HuggingFace example notebooks (includes ONNX export examples)

37. [onnx/models](https://github.com/onnx/models)
    - A collection of pre-trained, state-of-the-art models in the ONNX format

---

## NuGet Packages

### ONNX Runtime

38. [Microsoft.ML.OnnxRuntime 1.23.2](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime)
    - Main ONNX Runtime package for .NET

39. [Microsoft.ML.OnnxRuntime.Managed 1.23.2](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.Managed/)
    - Managed bindings for ONNX Runtime

40. [Microsoft.ML.OnnxRuntime.Gpu 1.23.2](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.gpu)
    - GPU-accelerated ONNX Runtime (CUDA)

41. [Microsoft.ML.OnnxRuntimeGenAI 0.2.0](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntimeGenAI/0.2.0)
    - ONNX Runtime for Generative AI (LLMs)

42. [Microsoft.ML.OnnxTransformer 5.0.0](https://www.nuget.org/packages/Microsoft.ML.OnnxTransformer/)
    - ML.NET integration for ONNX models

### Tokenizers

43. [Tokenizers.HuggingFace 2.21.4](https://www.nuget.org/packages/Tokenizers.HuggingFace/2.21.4)
    - .NET bindings for HuggingFace tokenizers (Rust-based)

44. [Tokenizers.DotNet 1.3.0](https://www.nuget.org/packages/Tokenizers.DotNet/)
    - Community wrapper for HuggingFace tokenizers

45. [Tokenizers.HuggingFace on Libraries.io](https://libraries.io/nuget/Tokenizers.HuggingFace)
    - Security & maintenance data for Tokenizers.HuggingFace

### TorchSharp

46. [TorchSharp (check latest on NuGet)](https://www.nuget.org/packages/TorchSharp)
    - Official TorchSharp package

47. [TorchSharp.PyBridge 1.2.0](https://www.nuget.org/packages/TorchSharp.PyBridge/1.2.0)
    - PyTorch model interop for TorchSharp

### Semantic Kernel

48. [Microsoft.SemanticKernel.Connectors.HuggingFace 1.6.1-preview](https://www.nuget.org/packages/Microsoft.SemanticKernel.Connectors.HuggingFace/1.6.1-preview)
    - HuggingFace connector for Semantic Kernel

---

## Blog Posts and Tutorials

### Microsoft

49. [Accelerating over 130,000 Hugging Face models with ONNX Runtime - Microsoft Open Source Blog](https://cloudblogs.microsoft.com/opensource/2023/10/04/accelerating-over-130000-hugging-face-models-with-onnx-runtime/)
    - Announcement of broad HuggingFace support in ONNX Runtime

50. [Journey to optimize large scale transformer model inference with ONNX Runtime - Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2021/06/30/journey-to-optimize-large-scale-transformer-model-inference-with-onnx-runtime)
    - Case study on optimizing transformer inference

51. [Introducing the ML.NET Text Classification API (preview) - .NET Blog](https://devblogs.microsoft.com/dotnet/introducing-the-ml-dotnet-text-classification-api-preview/)
    - Introduction to ML.NET's BERT-based text classification

52. [How to use Hugging Face Models with Semantic Kernel | Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/how-to-use-hugging-face-models-with-semantic-kernel/)
    - Tutorial for integrating HuggingFace with Semantic Kernel

53. [Image to Text with Semantic Kernel and HuggingFace | Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/image-to-text-with-semantic-kernel-and-huggingface/)
    - Multimodal AI with Semantic Kernel

### Community Blogs

54. [Using Huggingface Transformers with ML.NET | Rubix Code](https://rubikscode.net/2021/10/25/using-huggingface-transformers-with-ml-net/)
    - Detailed tutorial on ONNX + ML.NET workflow

55. [Machine Learning with ML.NET - NLP with BERT | Rubix Code](https://rubikscode.net/2021/04/19/machine-learning-with-ml-net-nlp-with-bert/)
    - BERT NLP implementation guide

56. [BERT Tokenizers NuGet Package for C# | Rubix Code](https://rubikscode.net/2022/09/13/bert-tokenizers-for-ml-net/)
    - Guide to using BERT tokenizers in .NET

57. [Text Classification in C# with ML.NET 2.0 - Matt on ML.NET](https://accessibleai.dev/post/ml_net_2_0_text_classification/)
    - ML.NET 2.0 text classification tutorial

58. [Run PyTorch in .NET with TorchSharp - CPI Consulting](https://cloudproinc.azurewebsites.net/index.php/2025/09/21/run-pytorch-in-net-with-torchsharp/)
    - Recent (2025) TorchSharp tutorial

59. [Build Your Own GPT from Scratch with C# and TorchSharp (CPU-Only!) - DEV Community](https://dev.to/auyeungdavid_2847435260/build-your-own-gpt-from-scratch-with-c-and-torchsharp-cpu-only-3ch5)
    - GPT implementation in TorchSharp

60. [State-Of-The-Art Natural Language Processing in .NET on the Edge - Ian Bebbington](https://ian.bebbs.co.uk/posts/Unoonnx)
    - Edge deployment with Uno Platform

61. [Using ONNX BERT Model for Text-based Q&A in your Mobile .NET Apps - Uno Platform](https://platform.uno/blog/context-recognition-bert-qna/)
    - Mobile BERT deployment tutorial

62. [Cross-Language Embedding Generation: Bringing Hugging Face Models to C# and Java with ONNX - Yuniko Software](https://yuniko.software/hugging-face-tokenizer-to-onnx-model/)
    - Comprehensive guide on embedding generation

63. [Building AI-Powered .NET Applications with Semantic Kernel - Andreas Schultz | Medium](https://medium.com/@aschultzme/building-ai-powered-net-applications-with-semantic-kernel-0cacd0c43877)
    - Semantic Kernel application development

64. [Accelerate your NLP pipelines using Hugging Face Transformers and ONNX Runtime - Tianlei Wu | Microsoft Azure | Medium](https://medium.com/microsoftazure/accelerate-your-nlp-pipelines-using-hugging-face-transformers-and-onnx-runtime-2443578f4333)
    - Performance optimization guide

### Source Generators and Code Generation

65. [Source Generators in C#: Compile-Time Code Generation | Learn C# Mastery](https://learncsharpmastery.com/blog/source-generators-compile-time-code-generation/)
    - C# source generators tutorial

66. [IntelliCode Compose: Code Generation Using Transformer - Microsoft Research](https://www.microsoft.com/en-us/research/publication/intellicode-compose-code-generation-using-transformer/)
    - Research paper on transformer-based code generation

---

## Academic Papers and Research

67. [IntelliCode compose: code generation using transformer | ACM ESEC/FSE 2020](https://dl.acm.org/doi/abs/10.1145/3368089.3417058)
    - Academic paper on transformer code generation

68. [A Comparative Study on Code Generation with Transformers - arXiv](https://arxiv.org/html/2412.05749v1)
    - Recent research on code generation

69. [MarianCG: a code generation transformer model inspired by machine translation - Journal of Engineering and Applied Science](https://jeas.springeropen.com/articles/10.1186/s44147-022-00159-4)
    - Code generation model research

70. [StructCoder: Structure-Aware Transformer for Code Generation - arXiv](https://arxiv.org/html/2206.05239)
    - Advanced transformer architecture for code

71. [Transformers in source code generation: A comprehensive survey - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1383762124001309)
    - Comprehensive survey of transformers for code

72. [TRANSFORMER-BASED MODEL FOR COMPUTER CODE GENERATION TO ASSIST PROGRAMMERS - ResearchGate](https://www.researchgate.net/publication/380357500_TRANSFORMER-BASED_MODEL_FOR_COMPUTER_CODE_GENERATION_TO_ASSIST_PROGRAMMERS)
    - Research on AI-assisted programming

---

## GitHub Issues and Discussions

73. [.NET bindings · Issue #1615 · huggingface/tokenizers](https://github.com/huggingface/tokenizers/issues/1615)
    - Discussion on official .NET bindings for HuggingFace tokenizers

74. [[Tokenizers] Add support for HuggingFace BPE Tokenizer format · Issue #6901 · dotnet/machinelearning](https://github.com/dotnet/machinelearning/issues/6901)
    - Request for HuggingFace tokenizer support in ML.NET

75. [Incompatability in C# with NuGet packages OnnxRuntime.GPU and OnnxTransformer · Issue #2013 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/2013)
    - GPU package compatibility discussion

76. [Using ONNX Runtime Training with GPT2 Text Generation · Issue #53 · microsoft/onnxruntime-training-examples](https://github.com/microsoft/onnxruntime-training-examples/issues/53)
    - GPT-2 training discussion

77. [Use pre-trained BERT weights with TorchSharp-defined BERT for NLP tasks · Discussion #457 · dotnet/TorchSharp](https://github.com/dotnet/TorchSharp/discussions/457)
    - Community discussion on loading pretrained BERT

78. [How to use Hugging Face Models with Semantic Kernel w/ C# · Discussion #6652 · microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel/discussions/6652)
    - Semantic Kernel + HuggingFace integration discussion

79. [How can I export a transformers model into onnx that not supported with optimum yet - #8 by nielsr - 🤗Optimum - Hugging Face Forums](https://discuss.huggingface.co/t/how-can-i-export-a-transformers-model-into-onnx-that-not-supported-with-optimum-yet/104590/8)
    - Advanced ONNX export techniques

---

## Related Technologies and Ecosystems

### PyTorch and Transformers

80. [PyTorch-Transformers – PyTorch](https://pytorch.org/hub/huggingface_pytorch-transformers/)
    - PyTorch Hub integration for transformers

81. [BERT - HuggingFace Docs](https://huggingface.co/docs/transformers/model_doc/bert)
    - Official BERT documentation

82. [Generation - HuggingFace Docs](https://huggingface.co/docs/transformers/main_classes/text_generation)
    - Text generation API documentation

### ONNX Ecosystem

83. [onnx-runtime · GitHub Topics](https://github.com/topics/onnx-runtime)
    - Browse ONNX Runtime projects on GitHub

84. [transformers · GitHub Topics](https://github.com/topics/transformers)
    - Browse transformer projects on GitHub

85. [sentence bert model in onnx format - Lightrun](https://lightrun.com/answers/ukplab-sentence-transformers-sentence-bert-model-in-onnx-format)
    - Discussion on sentence transformer ONNX export

86. [Adding example using ONNX model to get sentence embeddings · PR #386 · huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers/pull/386/files)
    - Example code for sentence embeddings

### Notebooks and Examples

87. [notebooks/examples/onnx-export.ipynb - huggingface/notebooks](https://github.com/huggingface/notebooks/blob/main/examples/onnx-export.ipynb)
    - Jupyter notebook with ONNX export examples

88. [Inference PyTorch Bert Model with ONNX Runtime on CPU - microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/python/tools/transformers/notebooks/PyTorch_Bert-Squad_OnnxRuntime_CPU.ipynb)
    - Official BERT inference notebook

---

## Additional Resources

### Documentation Archives

89. [Exporting transformers models — transformers 4.7.0 documentation](https://huggingface.co/transformers/v4.9.2/serialization.html)
    - Historical documentation for reference

90. [Exporting transformers models — transformers 3.3.0 documentation](https://huggingface.co/transformers/v3.3.1/serialization.html)
    - Earlier version documentation

91. [onnxruntime/docs/tutorials/huggingface.md at gh-pages · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/blob/gh-pages/docs/tutorials/huggingface.md)
    - Tutorial in markdown format

92. [Accelerate Hugging Face - onnxruntime (alternate URL)](https://tomwildenhain-microsoft.github.io/onnxruntime/docs/tutorials/huggingface.html)
    - Mirror of HuggingFace tutorial

### News and Updates

93. [Microsoft previews text classification API for ML.NET | InfoWorld](https://www.arnnet.com.au/article/699070/microsoft-previews-text-classification-api-ml-net/)
    - News coverage of ML.NET updates

94. [ML.NET Release Notes 2.0](https://github.com/dotnet/machinelearning/blob/main/docs/release-notes/2.0/release-2.0.0.md)
    - ML.NET 2.0 release notes with TorchSharp integration

### Community Projects and Examples

95. [Michieal/TorchSharpExamples - Codeberg](https://codeberg.org/Michieal/TorchSharpExamples)
    - TorchSharp implementation examples

96. [Michieal/TorchSharp - Codeberg](https://codeberg.org/Michieal/TorchSharp)
    - Mirror of TorchSharp repository

97. [NielsRogge/Transformers-Tutorials](https://github.com/NielsRogge/Transformers-Tutorials)
    - Community tutorials for transformers

98. [ThilinaRajapakse/simpletransformers](https://github.com/ThilinaRajapakse/simpletransformers)
    - Simplified transformers for various tasks

99. [extnet/Transformer.NET](https://github.com/extnet/Transformer.NET)
    - .NET template parsing library (different use case)

100. [chriskhanhtran/bert-for-sentiment-analysis](https://github.com/chriskhanhtran/bert-for-sentiment-analysis)
     - BERT sentiment analysis example

101. [huggingface/trl](https://github.com/huggingface/trl)
     - Train transformer language models with reinforcement learning

### Semantic Kernel Resources

102. [Semantic Kernel | Activate GenAI with Azure](https://azure.github.io/activate-genai/docs/concepts/semantic-kernel/)
     - Azure-focused Semantic Kernel guide

103. [Foundations of Semantic Kernel - Cookbook](https://github.com/microsoft/SemanticKernelCookBook/blob/main/docs/en/02.IntroduceSemanticKernel.md)
     - Semantic Kernel cookbook

104. [semantic-kernel/README.md](https://github.com/microsoft/semantic-kernel/blob/main/README.md)
     - Main README with quick start

---

## Summary by Category

### Essential Starting Points (Top 10)

1. [ONNX Runtime | Huggingface](https://onnxruntime.ai/huggingface) - Official overview
2. [Convert Transformers to ONNX with Hugging Face Optimum](https://huggingface.co/blog/convert-transformers-to-onnx) - Export guide
3. [Inference BERT NLP with C#](https://onnxruntime.ai/docs/tutorials/csharp/bert-nlp-csharp-console-app.html) - C# tutorial
4. [Using Huggingface Transformers with ML.NET](https://rubikscode.net/2021/10/25/using-huggingface-transformers-with-ml-net/) - Complete workflow
5. [dotnet/TorchSharp](https://github.com/dotnet/TorchSharp) - PyTorch in .NET
6. [tauerlund/Transformers.NET](https://github.com/tauerlund/Transformers.NET) - Easy HF integration
7. [Tokenizers.HuggingFace NuGet](https://www.nuget.org/packages/Tokenizers.HuggingFace/2.21.4) - Tokenizer package
8. [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) - AI orchestration
9. [Accelerating 130,000+ HF models](https://cloudblogs.microsoft.com/opensource/2023/10/04/accelerating-over-130000-hugging-face-models-with-onnx-runtime/) - Microsoft announcement
10. [huggingface/optimum-onnx](https://github.com/huggingface/optimum-onnx) - Export tool

### For Production Deployment

- ONNX Runtime documentation (#1-6, #38-42)
- Performance optimization guides (#49, #50, #64)
- ASP.NET Core integration (#54, #63)
- Mobile deployment (#60, #61)

### For Research and Experimentation

- TorchSharp resources (#23-27, #46-47, #58-59)
- Academic papers (#67-72)
- Community discussions (#73-79)

### For Tokenization

- Tokenizers documentation (#43-45, #34)
- BERTTokenizers (#30, #56)
- Integration examples (#54, #62)

---

**Last Updated:** 2026-01-19
**Total Resources:** 104 links
