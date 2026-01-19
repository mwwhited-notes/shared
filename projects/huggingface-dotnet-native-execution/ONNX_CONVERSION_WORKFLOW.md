# ONNX Conversion Workflow

## Overview

This document provides step-by-step instructions for converting HuggingFace transformer models to ONNX format and deploying them in .NET applications.

## Prerequisites

### Python Environment
```bash
# Install Python 3.8+ (if not already installed)
python --version

# Create virtual environment
python -m venv hf-onnx-env
source hf-onnx-env/bin/activate  # Linux/Mac
# OR
hf-onnx-env\Scripts\activate  # Windows
```

### Install HuggingFace Optimum
```bash
# Install Optimum with ONNX Runtime
pip install optimum[exporters,onnxruntime]

# Verify installation
optimum-cli --help
```

### .NET Environment
```bash
# Ensure .NET 6.0+ is installed
dotnet --version
```

---

## Method 1: CLI Export (Recommended)

### Basic Export

```bash
# Export a model to ONNX
optimum-cli export onnx \
  --model bert-base-uncased \
  bert-base-uncased-onnx/

# This creates:
# - model.onnx (the ONNX model file)
# - tokenizer_config.json
# - tokenizer.json
# - config.json
```

### Export with Task Specification

```bash
# For sequence classification (sentiment analysis)
optimum-cli export onnx \
  --model distilbert-base-uncased-finetuned-sst-2-english \
  --task text-classification \
  distilbert-sentiment-onnx/

# For question answering
optimum-cli export onnx \
  --model distilbert-base-uncased-distilled-squad \
  --task question-answering \
  distilbert-qa-onnx/

# For token classification (NER)
optimum-cli export onnx \
  --model dslim/bert-base-NER \
  --task token-classification \
  bert-ner-onnx/

# For text generation
optimum-cli export onnx \
  --model gpt2 \
  --task text-generation \
  gpt2-onnx/
```

### Export with Optimization

```bash
# Export with O2 optimization level
optimum-cli export onnx \
  --model bert-base-uncased \
  --optimize O2 \
  bert-optimized-onnx/

# Export with quantization (INT8)
optimum-cli export onnx \
  --model bert-base-uncased \
  --optimize O2 \
  --quantize \
  bert-quantized-onnx/
```

### Export from Local Model

```bash
# If you have a local fine-tuned model
optimum-cli export onnx \
  --model ./my-finetuned-model/ \
  --task text-classification \
  my-model-onnx/
```

---

## Method 2: Programmatic Export (Python)

### Basic Python Export

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer

# Load and export model
model = ORTModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english",
    export=True
)

# Save to disk
model.save_pretrained("./distilbert-sentiment-onnx")

# Save tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)
tokenizer.save_pretrained("./distilbert-sentiment-onnx")
```

### Export Different Model Types

```python
from optimum.onnxruntime import (
    ORTModelForQuestionAnswering,
    ORTModelForTokenClassification,
    ORTModelForCausalLM,
)

# Question Answering
qa_model = ORTModelForQuestionAnswering.from_pretrained(
    "distilbert-base-uncased-distilled-squad",
    export=True
)
qa_model.save_pretrained("./qa-model-onnx")

# Token Classification (NER)
ner_model = ORTModelForTokenClassification.from_pretrained(
    "dslim/bert-base-NER",
    export=True
)
ner_model.save_pretrained("./ner-model-onnx")

# Causal Language Model (GPT-2)
gpt2_model = ORTModelForCausalLM.from_pretrained(
    "gpt2",
    export=True
)
gpt2_model.save_pretrained("./gpt2-onnx")
```

### Export with Optimization

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from optimum.onnxruntime.configuration import OptimizationConfig

# Create optimization config
optimization_config = OptimizationConfig(
    optimization_level=2,  # O0, O1, O2, O99
    optimize_for_gpu=False,
    fp16=False  # Set to True for GPU FP16
)

# Export with optimization
model = ORTModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    export=True,
    optimization_config=optimization_config
)
model.save_pretrained("./bert-optimized-onnx")
```

---

## Method 3: Manual Export (Advanced)

For models not supported by Optimum, use transformers.onnx directly:

```python
from transformers import AutoModel, AutoTokenizer
from transformers.onnx import export
from pathlib import Path

# Load model and tokenizer
model_name = "bert-base-uncased"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Export to ONNX
onnx_path = Path("./bert-manual-onnx")
onnx_path.mkdir(exist_ok=True)

export(
    preprocessor=tokenizer,
    model=model,
    config=model.config.to_diff_dict(),
    opset=14,
    output=onnx_path / "model.onnx"
)

# Save tokenizer
tokenizer.save_pretrained(onnx_path)
```

---

## Verification and Testing

### Verify ONNX Model

```python
import onnx
import onnxruntime as ort

# Load and check model
onnx_model = onnx.load("./bert-base-uncased-onnx/model.onnx")
onnx.checker.check_model(onnx_model)
print("✓ Model is valid")

# Check opset version
print(f"Opset version: {onnx_model.opset_import[0].version}")

# Inspect inputs/outputs
for input in onnx_model.graph.input:
    print(f"Input: {input.name}")

for output in onnx_model.graph.output:
    print(f"Output: {output.name}")
```

### Test with ONNX Runtime (Python)

```python
import onnxruntime as ort
from transformers import AutoTokenizer

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("./bert-base-uncased-onnx")

# Create inference session
session = ort.InferenceSession("./bert-base-uncased-onnx/model.onnx")

# Prepare input
text = "This is a test sentence."
inputs = tokenizer(text, return_tensors="np")

# Run inference
outputs = session.run(
    None,
    {
        "input_ids": inputs["input_ids"],
        "attention_mask": inputs["attention_mask"],
    }
)

print(f"Output shape: {outputs[0].shape}")
```

---

## Deploying in .NET

### Step 1: Install NuGet Packages

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.ML.OnnxRuntime" Version="1.23.2" />
    <PackageReference Include="Microsoft.ML.OnnxRuntime.Managed" Version="1.23.2" />
    <PackageReference Include="Tokenizers.HuggingFace" Version="2.21.4" />
  </ItemGroup>
</Project>
```

### Step 2: Copy Model Files

```bash
# Copy ONNX model and tokenizer to your .NET project
cp -r bert-base-uncased-onnx/ ./MyDotNetApp/Models/
```

### Step 3: Load and Run in C#

```csharp
using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;
using Tokenizers.HuggingFace;

public class BertInference
{
    private readonly InferenceSession _session;
    private readonly Tokenizer _tokenizer;

    public BertInference(string modelPath, string tokenizerPath)
    {
        // Load ONNX model
        _session = new InferenceSession(modelPath);

        // Load tokenizer
        _tokenizer = Tokenizer.FromFile(tokenizerPath);
    }

    public float[] Predict(string text)
    {
        // Tokenize input
        var encoding = _tokenizer.Encode(text, addSpecialTokens: true);
        var inputIds = encoding.Ids;
        var attentionMask = encoding.AttentionMask;

        // Create tensors
        var inputIdsTensor = new DenseTensor<long>(
            inputIds.Select(x => (long)x).ToArray(),
            new[] { 1, inputIds.Length }
        );

        var attentionMaskTensor = new DenseTensor<long>(
            attentionMask.Select(x => (long)x).ToArray(),
            new[] { 1, attentionMask.Length }
        );

        // Create inputs
        var inputs = new List<NamedOnnxValue>
        {
            NamedOnnxValue.CreateFromTensor("input_ids", inputIdsTensor),
            NamedOnnxValue.CreateFromTensor("attention_mask", attentionMaskTensor)
        };

        // Run inference
        using var results = _session.Run(inputs);
        var output = results.First().AsEnumerable<float>().ToArray();

        return output;
    }

    public void Dispose()
    {
        _session?.Dispose();
    }
}

// Usage
var inference = new BertInference(
    "Models/bert-base-uncased-onnx/model.onnx",
    "Models/bert-base-uncased-onnx/tokenizer.json"
);

var result = inference.Predict("This is a test sentence.");
Console.WriteLine($"Output: {string.Join(", ", result.Take(10))}...");
```

### Step 4: Sentiment Classification Example

```csharp
public class SentimentAnalyzer
{
    private readonly InferenceSession _session;
    private readonly Tokenizer _tokenizer;
    private readonly string[] _labels = { "NEGATIVE", "POSITIVE" };

    public SentimentAnalyzer(string modelPath, string tokenizerPath)
    {
        _session = new InferenceSession(modelPath);
        _tokenizer = Tokenizer.FromFile(tokenizerPath);
    }

    public (string Label, float Confidence) AnalyzeSentiment(string text)
    {
        // Tokenize
        var encoding = _tokenizer.Encode(text, addSpecialTokens: true);

        // Create input tensors
        var inputIds = new DenseTensor<long>(
            encoding.Ids.Select(x => (long)x).ToArray(),
            new[] { 1, encoding.Ids.Length }
        );

        var attentionMask = new DenseTensor<long>(
            encoding.AttentionMask.Select(x => (long)x).ToArray(),
            new[] { 1, encoding.AttentionMask.Length }
        );

        // Run inference
        var inputs = new List<NamedOnnxValue>
        {
            NamedOnnxValue.CreateFromTensor("input_ids", inputIds),
            NamedOnnxValue.CreateFromTensor("attention_mask", attentionMask)
        };

        using var results = _session.Run(inputs);
        var logits = results.First().AsEnumerable<float>().ToArray();

        // Apply softmax
        var exp = logits.Select(Math.Exp).ToArray();
        var sum = exp.Sum();
        var probabilities = exp.Select(e => (float)(e / sum)).ToArray();

        // Get prediction
        var maxIdx = Array.IndexOf(probabilities, probabilities.Max());
        return (_labels[maxIdx], probabilities[maxIdx]);
    }
}

// Usage
var analyzer = new SentimentAnalyzer(
    "Models/distilbert-sentiment-onnx/model.onnx",
    "Models/distilbert-sentiment-onnx/tokenizer.json"
);

var (label, confidence) = analyzer.AnalyzeSentiment("This movie is amazing!");
Console.WriteLine($"Sentiment: {label} ({confidence:P2})");
```

---

## Optimization Strategies

### 1. Quantization (Reduce Model Size)

```bash
# INT8 quantization (75% size reduction)
optimum-cli export onnx \
  --model bert-base-uncased \
  --optimize O2 \
  --quantize \
  bert-quantized-onnx/

# Result: ~110MB → ~28MB
```

### 2. Graph Optimization

```bash
# O2 optimization (no quantization)
optimum-cli export onnx \
  --model bert-base-uncased \
  --optimize O2 \
  bert-optimized-onnx/

# Optimization levels:
# O0 - Disable all optimizations
# O1 - Basic optimizations
# O2 - Extended optimizations (recommended)
# O99 - All optimizations
```

### 3. Dynamic Quantization (Runtime)

```csharp
// Not directly supported in ONNX Runtime C# API
// Quantization should be done during export
```

### 4. GPU Acceleration

```xml
<!-- Install GPU package -->
<PackageReference Include="Microsoft.ML.OnnxRuntime.Gpu" Version="1.23.2" />
```

```csharp
// Use GPU execution provider
var sessionOptions = new SessionOptions();
sessionOptions.AppendExecutionProvider_CUDA(0); // Device ID 0

var session = new InferenceSession("model.onnx", sessionOptions);
```

### 5. DirectML (Windows GPU)

```xml
<PackageReference Include="Microsoft.ML.OnnxRuntime.DirectML" Version="1.23.2" />
```

```csharp
var sessionOptions = new SessionOptions();
sessionOptions.AppendExecutionProvider_DML(0);

var session = new InferenceSession("model.onnx", sessionOptions);
```

---

## Supported Model Architectures

### ✅ Fully Supported (Optimum)

- **BERT** (bert-base, bert-large, distilbert, roberta, etc.)
- **GPT-2** (gpt2, gpt2-medium, gpt2-large, gpt2-xl)
- **T5** (t5-small, t5-base, t5-large, flan-t5)
- **DistilBERT** (all variants)
- **RoBERTa** (roberta-base, roberta-large)
- **ALBERT** (albert-base, albert-large)
- **ELECTRA** (electra-small, electra-base)
- **XLM-RoBERTa** (multilingual models)
- **DeBERTa** (deberta-base, deberta-large)
- **Sentence Transformers** (all-MiniLM-L6-v2, etc.)

### ⚠️ Partially Supported

- **GPT-Neo** (may require custom config)
- **GPT-J** (large models, memory intensive)
- **BLOOM** (very large models)
- **LLaMA** (export possible, optimization varies)

### ❌ Not Supported / Experimental

- **Whisper** (audio models - different workflow)
- **Stable Diffusion** (vision models - different workflow)
- **CLIP** (multimodal - requires special handling)

Check latest support: https://huggingface.co/docs/optimum-onnx/

---

## Troubleshooting

### Issue: "Model not supported"

```bash
# Try manual export with transformers.onnx
python -c "from transformers.onnx import export; ..."
```

### Issue: "Opset version mismatch"

```bash
# Specify opset version
optimum-cli export onnx \
  --model bert-base-uncased \
  --opset 14 \
  bert-onnx/
```

### Issue: "Dynamic axes error"

Check model inputs/outputs match ONNX expectations. Some models require custom configurations.

### Issue: "Out of memory during export"

```bash
# Use smaller batch size or model variant
# Or export on machine with more RAM
```

### Issue: "Tokenizer not compatible"

Ensure you're using `Tokenizers.HuggingFace` for tokenizer.json files, not older formats.

---

## Best Practices

1. **Always verify** the exported model with Python ONNX Runtime before deploying
2. **Use optimization level O2** for production deployments
3. **Quantize models** for mobile/edge deployment (75% size reduction)
4. **Test tokenizer compatibility** with sample inputs
5. **Version control** both the model and tokenizer files
6. **Document** the export command and settings used
7. **Include** model.onnx, tokenizer.json, config.json in deployment
8. **Benchmark** performance on target hardware before committing
9. **Consider** DirectML (Windows) or CoreML (macOS) for consumer devices
10. **Monitor** HuggingFace Optimum updates for new model support

---

## Resources

- **HuggingFace Optimum Docs:** https://huggingface.co/docs/optimum-onnx/
- **ONNX Runtime C# Tutorial:** https://onnxruntime.ai/docs/tutorials/csharp/
- **BERT NLP C# Example:** https://onnxruntime.ai/docs/tutorials/csharp/bert-nlp-csharp-console-app.html
- **Model Hub:** https://huggingface.co/models (filter by "ONNX")

---

**Last Updated:** 2026-01-19
