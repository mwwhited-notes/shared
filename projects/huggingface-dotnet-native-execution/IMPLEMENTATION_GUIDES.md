# Implementation Guides

## Overview

This document provides practical, end-to-end implementation guides for common scenarios using HuggingFace models in .NET applications.

---

## Scenario 1: BERT Sentiment Analysis (ONNX Runtime)

**Use Case:** Classify customer reviews as positive or negative
**Model:** distilbert-base-uncased-finetuned-sst-2-english
**Approach:** ONNX Runtime + HuggingFace Tokenizers

### Step 1: Export Model to ONNX

```bash
pip install optimum[exporters,onnxruntime]

optimum-cli export onnx \
  --model distilbert-base-uncased-finetuned-sst-2-english \
  --task text-classification \
  --optimize O2 \
  distilbert-sentiment-onnx/
```

### Step 2: Create .NET Console Application

```bash
dotnet new console -n SentimentAnalyzer
cd SentimentAnalyzer
dotnet add package Microsoft.ML.OnnxRuntime --version 1.23.2
dotnet add package Tokenizers.HuggingFace --version 2.21.4
```

### Step 3: Copy Model Files

```bash
mkdir Models
cp -r ../distilbert-sentiment-onnx/ ./Models/
```

### Step 4: Implement Sentiment Analyzer

```csharp
using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;
using Tokenizers.HuggingFace;

namespace SentimentAnalyzer;

public class SentimentClassifier : IDisposable
{
    private readonly InferenceSession _session;
    private readonly Tokenizer _tokenizer;
    private readonly string[] _labels = { "NEGATIVE", "POSITIVE" };

    public SentimentClassifier(string modelPath, string tokenizerPath)
    {
        var sessionOptions = new SessionOptions();
        sessionOptions.GraphOptimizationLevel = GraphOptimizationLevel.ORT_ENABLE_ALL;

        _session = new InferenceSession(modelPath, sessionOptions);
        _tokenizer = Tokenizer.FromFile(tokenizerPath);
    }

    public (string Label, float Confidence) Classify(string text)
    {
        // Tokenize input
        var encoding = _tokenizer.Encode(text, addSpecialTokens: true);

        // Prepare input tensors
        var inputIds = CreateLongTensor(encoding.Ids);
        var attentionMask = CreateLongTensor(encoding.AttentionMask);

        // Create inputs
        var inputs = new List<NamedOnnxValue>
        {
            NamedOnnxValue.CreateFromTensor("input_ids", inputIds),
            NamedOnnxValue.CreateFromTensor("attention_mask", attentionMask)
        };

        // Run inference
        using var results = _session.Run(inputs);
        var logits = results.First().AsEnumerable<float>().ToArray();

        // Apply softmax and get prediction
        var probabilities = Softmax(logits);
        var maxIdx = Array.IndexOf(probabilities, probabilities.Max());

        return (_labels[maxIdx], probabilities[maxIdx]);
    }

    private DenseTensor<long> CreateLongTensor(IReadOnlyList<uint> data)
    {
        var tensor = new DenseTensor<long>(new[] { 1, data.Count });
        for (int i = 0; i < data.Count; i++)
            tensor[0, i] = (long)data[i];
        return tensor;
    }

    private float[] Softmax(float[] logits)
    {
        var exp = logits.Select(Math.Exp).ToArray();
        var sum = exp.Sum();
        return exp.Select(e => (float)(e / sum)).ToArray();
    }

    public void Dispose()
    {
        _session?.Dispose();
    }
}

// Program.cs
class Program
{
    static void Main(string[] args)
    {
        using var classifier = new SentimentClassifier(
            "Models/distilbert-sentiment-onnx/model.onnx",
            "Models/distilbert-sentiment-onnx/tokenizer.json"
        );

        var reviews = new[]
        {
            "This movie was absolutely fantastic! Best film of the year.",
            "Terrible experience. Would not recommend.",
            "It was okay, nothing special.",
        };

        foreach (var review in reviews)
        {
            var (label, confidence) = classifier.Classify(review);
            Console.WriteLine($"Review: {review}");
            Console.WriteLine($"Sentiment: {label} ({confidence:P2})\n");
        }
    }
}
```

### Step 5: Run

```bash
dotnet run
```

**Expected Output:**
```
Review: This movie was absolutely fantastic! Best film of the year.
Sentiment: POSITIVE (99.87%)

Review: Terrible experience. Would not recommend.
Sentiment: NEGATIVE (99.94%)

Review: It was okay, nothing special.
Sentiment: POSITIVE (52.34%)
```

---

## Scenario 2: Question Answering System (BERT QA)

**Use Case:** Extract answers from context documents
**Model:** distilbert-base-uncased-distilled-squad
**Approach:** ONNX Runtime

### Step 1: Export Model

```bash
optimum-cli export onnx \
  --model distilbert-base-uncased-distilled-squad \
  --task question-answering \
  --optimize O2 \
  distilbert-qa-onnx/
```

### Step 2: Create Project

```bash
dotnet new console -n QuestionAnswering
cd QuestionAnswering
dotnet add package Microsoft.ML.OnnxRuntime --version 1.23.2
dotnet add package Tokenizers.HuggingFace --version 2.21.4
```

### Step 3: Implement QA System

```csharp
using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;
using Tokenizers.HuggingFace;

public class QuestionAnswerer : IDisposable
{
    private readonly InferenceSession _session;
    private readonly Tokenizer _tokenizer;

    public QuestionAnswerer(string modelPath, string tokenizerPath)
    {
        _session = new InferenceSession(modelPath);
        _tokenizer = Tokenizer.FromFile(tokenizerPath);
    }

    public string Answer(string question, string context)
    {
        // Tokenize question and context together
        var encoding = _tokenizer.Encode(question, context, addSpecialTokens: true);

        var inputIds = CreateLongTensor(encoding.Ids);
        var attentionMask = CreateLongTensor(encoding.AttentionMask);

        var inputs = new List<NamedOnnxValue>
        {
            NamedOnnxValue.CreateFromTensor("input_ids", inputIds),
            NamedOnnxValue.CreateFromTensor("attention_mask", attentionMask)
        };

        // Run inference - outputs are start and end logits
        using var results = _session.Run(inputs);
        var startLogits = results[0].AsEnumerable<float>().ToArray();
        var endLogits = results[1].AsEnumerable<float>().ToArray();

        // Find best answer span
        var startIdx = Array.IndexOf(startLogits, startLogits.Max());
        var endIdx = Array.IndexOf(endLogits, endLogits.Max());

        if (endIdx < startIdx)
            return "Unable to find answer";

        // Decode answer tokens
        var answerTokens = encoding.Ids
            .Skip(startIdx)
            .Take(endIdx - startIdx + 1)
            .ToArray();

        return _tokenizer.Decode(answerTokens, skipSpecialTokens: true);
    }

    private DenseTensor<long> CreateLongTensor(IReadOnlyList<uint> data)
    {
        var tensor = new DenseTensor<long>(new[] { 1, data.Count });
        for (int i = 0; i < data.Count; i++)
            tensor[0, i] = (long)data[i];
        return tensor;
    }

    public void Dispose() => _session?.Dispose();
}

// Usage
class Program
{
    static void Main()
    {
        using var qa = new QuestionAnswerer(
            "Models/distilbert-qa-onnx/model.onnx",
            "Models/distilbert-qa-onnx/tokenizer.json"
        );

        var context = @"
            The Amazon rainforest is a moist broadleaf tropical rainforest in the Amazon
            biome that covers most of the Amazon basin of South America. The basin has an
            area of 7,000,000 square kilometers (2,700,000 sq mi).
        ";

        var questions = new[]
        {
            "What is the Amazon rainforest?",
            "How large is the Amazon basin?",
            "Where is the Amazon rainforest located?",
        };

        foreach (var question in questions)
        {
            var answer = qa.Answer(question, context);
            Console.WriteLine($"Q: {question}");
            Console.WriteLine($"A: {answer}\n");
        }
    }
}
```

---

## Scenario 3: Named Entity Recognition (Token Classification)

**Use Case:** Extract entities (person, location, organization) from text
**Model:** dslim/bert-base-NER
**Approach:** ONNX Runtime

### Step 1: Export Model

```bash
optimum-cli export onnx \
  --model dslim/bert-base-NER \
  --task token-classification \
  --optimize O2 \
  bert-ner-onnx/
```

### Step 2: Implement NER System

```csharp
public class NamedEntityRecognizer : IDisposable
{
    private readonly InferenceSession _session;
    private readonly Tokenizer _tokenizer;
    private readonly string[] _labels =
    {
        "O", "B-PER", "I-PER", "B-ORG", "I-ORG",
        "B-LOC", "I-LOC", "B-MISC", "I-MISC"
    };

    public NamedEntityRecognizer(string modelPath, string tokenizerPath)
    {
        _session = new InferenceSession(modelPath);
        _tokenizer = Tokenizer.FromFile(tokenizerPath);
    }

    public List<(string Text, string Label)> ExtractEntities(string text)
    {
        var encoding = _tokenizer.Encode(text, addSpecialTokens: true);

        var inputIds = CreateLongTensor(encoding.Ids);
        var attentionMask = CreateLongTensor(encoding.AttentionMask);

        var inputs = new List<NamedOnnxValue>
        {
            NamedOnnxValue.CreateFromTensor("input_ids", inputIds),
            NamedOnnxValue.CreateFromTensor("attention_mask", attentionMask)
        };

        using var results = _session.Run(inputs);
        var logits = results.First().AsEnumerable<float>().ToArray();

        // Reshape to [sequence_length, num_labels]
        var numLabels = _labels.Length;
        var seqLength = logits.Length / numLabels;

        var entities = new List<(string Text, string Label)>();

        for (int i = 1; i < seqLength - 1; i++) // Skip [CLS] and [SEP]
        {
            var tokenLogits = logits
                .Skip(i * numLabels)
                .Take(numLabels)
                .ToArray();

            var labelIdx = Array.IndexOf(tokenLogits, tokenLogits.Max());
            var label = _labels[labelIdx];

            if (label != "O")
            {
                var token = _tokenizer.Decode(new[] { encoding.Ids[i] });
                entities.Add((token, label));
            }
        }

        return MergeEntities(entities);
    }

    private List<(string Text, string Label)> MergeEntities(
        List<(string Text, string Label)> entities)
    {
        var merged = new List<(string Text, string Label)>();
        string currentText = "";
        string currentLabel = "";

        foreach (var (text, label) in entities)
        {
            if (label.StartsWith("B-"))
            {
                if (!string.IsNullOrEmpty(currentText))
                    merged.Add((currentText.Trim(), currentLabel));

                currentText = text;
                currentLabel = label.Substring(2); // Remove "B-"
            }
            else if (label.StartsWith("I-") && label.Substring(2) == currentLabel)
            {
                currentText += " " + text;
            }
        }

        if (!string.IsNullOrEmpty(currentText))
            merged.Add((currentText.Trim(), currentLabel));

        return merged;
    }

    private DenseTensor<long> CreateLongTensor(IReadOnlyList<uint> data)
    {
        var tensor = new DenseTensor<long>(new[] { 1, data.Count });
        for (int i = 0; i < data.Count; i++)
            tensor[0, i] = (long)data[i];
        return tensor;
    }

    public void Dispose() => _session?.Dispose();
}

// Usage
class Program
{
    static void Main()
    {
        using var ner = new NamedEntityRecognizer(
            "Models/bert-ner-onnx/model.onnx",
            "Models/bert-ner-onnx/tokenizer.json"
        );

        var text = "Elon Musk founded SpaceX and Tesla in California.";
        var entities = ner.ExtractEntities(text);

        Console.WriteLine($"Text: {text}\n");
        Console.WriteLine("Entities:");
        foreach (var (entityText, label) in entities)
        {
            Console.WriteLine($"  {entityText} ({label})");
        }
    }
}
```

---

## Scenario 4: Sentence Embeddings (Semantic Search)

**Use Case:** Generate embeddings for semantic similarity search
**Model:** sentence-transformers/all-MiniLM-L6-v2
**Approach:** ONNX Runtime

### Step 1: Export Model

```bash
optimum-cli export onnx \
  --model sentence-transformers/all-MiniLM-L6-v2 \
  --task feature-extraction \
  --optimize O2 \
  all-minilm-l6-v2-onnx/
```

### Step 2: Implement Embedding Generator

```csharp
public class SentenceEmbedder : IDisposable
{
    private readonly InferenceSession _session;
    private readonly Tokenizer _tokenizer;

    public SentenceEmbedder(string modelPath, string tokenizerPath)
    {
        _session = new InferenceSession(modelPath);
        _tokenizer = Tokenizer.FromFile(tokenizerPath);
    }

    public float[] GetEmbedding(string sentence)
    {
        var encoding = _tokenizer.Encode(sentence, addSpecialTokens: true);

        var inputIds = CreateLongTensor(encoding.Ids);
        var attentionMask = CreateLongTensor(encoding.AttentionMask);

        var inputs = new List<NamedOnnxValue>
        {
            NamedOnnxValue.CreateFromTensor("input_ids", inputIds),
            NamedOnnxValue.CreateFromTensor("attention_mask", attentionMask)
        };

        using var results = _session.Run(inputs);
        var embeddings = results.First().AsEnumerable<float>().ToArray();

        // Mean pooling
        var hiddenSize = 384; // Model-specific
        var seqLength = embeddings.Length / hiddenSize;
        var pooled = new float[hiddenSize];

        for (int i = 0; i < hiddenSize; i++)
        {
            float sum = 0;
            for (int j = 0; j < seqLength; j++)
            {
                if (encoding.AttentionMask[j] == 1)
                    sum += embeddings[j * hiddenSize + i];
            }
            pooled[i] = sum / seqLength;
        }

        // Normalize
        var magnitude = Math.Sqrt(pooled.Sum(x => x * x));
        for (int i = 0; i < pooled.Length; i++)
            pooled[i] /= (float)magnitude;

        return pooled;
    }

    public float CosineSimilarity(float[] a, float[] b)
    {
        float dot = 0;
        for (int i = 0; i < a.Length; i++)
            dot += a[i] * b[i];
        return dot; // Already normalized, so dot product = cosine similarity
    }

    private DenseTensor<long> CreateLongTensor(IReadOnlyList<uint> data)
    {
        var tensor = new DenseTensor<long>(new[] { 1, data.Count });
        for (int i = 0; i < data.Count; i++)
            tensor[0, i] = (long)data[i];
        return tensor;
    }

    public void Dispose() => _session?.Dispose();
}

// Usage - Semantic Search
class Program
{
    static void Main()
    {
        using var embedder = new SentenceEmbedder(
            "Models/all-minilm-l6-v2-onnx/model.onnx",
            "Models/all-minilm-l6-v2-onnx/tokenizer.json"
        );

        var query = "How do I reset my password?";
        var documents = new[]
        {
            "You can reset your password from the settings page.",
            "Our products are available in multiple colors.",
            "The meeting is scheduled for next Tuesday.",
            "Click 'Forgot Password' to reset your credentials.",
        };

        var queryEmbedding = embedder.GetEmbedding(query);

        Console.WriteLine($"Query: {query}\n");
        Console.WriteLine("Most similar documents:");

        var results = documents
            .Select(doc => new
            {
                Text = doc,
                Similarity = embedder.CosineSimilarity(
                    queryEmbedding,
                    embedder.GetEmbedding(doc)
                )
            })
            .OrderByDescending(x => x.Similarity)
            .ToList();

        foreach (var result in results)
        {
            Console.WriteLine($"  [{result.Similarity:F3}] {result.Text}");
        }
    }
}
```

---

## Scenario 5: TorchSharp GPT-2 Text Generation

**Use Case:** Generate text using GPT-2
**Approach:** TorchSharp with PyTorch weights

### Step 1: Install TorchSharp

```bash
dotnet new console -n TextGenerator
cd TextGenerator
dotnet add package TorchSharp --version 0.103.0
dotnet add package TorchSharp-cpu --version 0.103.0
# OR for GPU:
# dotnet add package TorchSharp-cuda-windows --version 0.103.0
dotnet add package TorchSharp.PyBridge --version 1.2.0
```

### Step 2: Export GPT-2 Weights (Python)

```python
import torch
from transformers import GPT2LMHeadModel

model = GPT2LMHeadModel.from_pretrained("gpt2")
torch.save(model.state_dict(), "gpt2-weights.pt")
```

### Step 3: Implement GPT-2 in TorchSharp

```csharp
using TorchSharp;
using TorchSharp.Modules;
using static TorchSharp.torch;
using static TorchSharp.torch.nn;

// Note: This is a simplified example
// Full GPT-2 implementation requires complete architecture

public class GPT2Generator : IDisposable
{
    private readonly Module<Tensor, Tensor> _model;
    private readonly Device _device;

    public GPT2Generator(string weightsPath, bool useGpu = false)
    {
        _device = useGpu && cuda.is_available()
            ? CUDA
            : CPU;

        // Load model architecture (simplified)
        // In practice, you'd implement full GPT2LMHeadModel
        _model = LoadGPT2Model(weightsPath);
        _model.to(_device);
        _model.eval();
    }

    private Module<Tensor, Tensor> LoadGPT2Model(string path)
    {
        // This would require full GPT-2 architecture implementation
        // See: https://github.com/tauerlund/Transformers.NET
        throw new NotImplementedException(
            "Full GPT-2 implementation requires complete architecture. " +
            "Use Transformers.NET for ready-to-use implementation."
        );
    }

    public void Dispose()
    {
        _model?.Dispose();
    }
}

// For production use, use Transformers.NET instead:
// https://github.com/tauerlund/Transformers.NET
```

---

## Scenario 6: ASP.NET Core Web API with BERT

**Use Case:** RESTful API for sentiment analysis
**Approach:** ONNX Runtime in ASP.NET Core

### Step 1: Create Web API

```bash
dotnet new webapi -n SentimentAPI
cd SentimentAPI
dotnet add package Microsoft.ML.OnnxRuntime --version 1.23.2
dotnet add package Tokenizers.HuggingFace --version 2.21.4
```

### Step 2: Implement Service

```csharp
// Services/SentimentService.cs
public interface ISentimentService
{
    Task<SentimentResult> AnalyzeAsync(string text);
}

public class SentimentResult
{
    public string Label { get; set; }
    public float Confidence { get; set; }
}

public class SentimentService : ISentimentService, IDisposable
{
    private readonly InferenceSession _session;
    private readonly Tokenizer _tokenizer;
    private readonly string[] _labels = { "NEGATIVE", "POSITIVE" };

    public SentimentService(IConfiguration config)
    {
        var modelPath = config["Models:Sentiment:Path"];
        var tokenizerPath = config["Models:Sentiment:Tokenizer"];

        _session = new InferenceSession(modelPath);
        _tokenizer = Tokenizer.FromFile(tokenizerPath);
    }

    public Task<SentimentResult> AnalyzeAsync(string text)
    {
        var encoding = _tokenizer.Encode(text, addSpecialTokens: true);

        var inputIds = CreateTensor(encoding.Ids);
        var attentionMask = CreateTensor(encoding.AttentionMask);

        var inputs = new List<NamedOnnxValue>
        {
            NamedOnnxValue.CreateFromTensor("input_ids", inputIds),
            NamedOnnxValue.CreateFromTensor("attention_mask", attentionMask)
        };

        using var results = _session.Run(inputs);
        var logits = results.First().AsEnumerable<float>().ToArray();
        var probabilities = Softmax(logits);
        var maxIdx = Array.IndexOf(probabilities, probabilities.Max());

        return Task.FromResult(new SentimentResult
        {
            Label = _labels[maxIdx],
            Confidence = probabilities[maxIdx]
        });
    }

    // Helper methods omitted for brevity

    public void Dispose() => _session?.Dispose();
}
```

### Step 3: Register Service

```csharp
// Program.cs
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddSingleton<ISentimentService, SentimentService>();

var app = builder.Build();
app.MapControllers();
app.Run();
```

### Step 4: Create Controller

```csharp
// Controllers/SentimentController.cs
[ApiController]
[Route("api/[controller]")]
public class SentimentController : ControllerBase
{
    private readonly ISentimentService _sentimentService;

    public SentimentController(ISentimentService sentimentService)
    {
        _sentimentService = sentimentService;
    }

    [HttpPost("analyze")]
    public async Task<ActionResult<SentimentResult>> Analyze(
        [FromBody] AnalyzeRequest request)
    {
        if (string.IsNullOrWhiteSpace(request.Text))
            return BadRequest("Text is required");

        var result = await _sentimentService.AnalyzeAsync(request.Text);
        return Ok(result);
    }
}

public class AnalyzeRequest
{
    public string Text { get; set; }
}
```

### Step 5: Test

```bash
curl -X POST http://localhost:5000/api/sentiment/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"This is amazing!"}'
```

---

## Best Practices

### 1. Model Management
- Store models in dedicated folder (e.g., `Models/`)
- Version control model metadata (config.json, model version)
- Don't commit large model files to git (use Git LFS or external storage)

### 2. Performance Optimization
- Use singleton services for model loading (ASP.NET Core)
- Implement model caching for frequently used models
- Consider batch processing for multiple inputs
- Use GPU acceleration when available

### 3. Error Handling
```csharp
try
{
    var result = classifier.Classify(text);
}
catch (OnnxRuntimeException ex)
{
    _logger.LogError(ex, "ONNX inference failed");
    // Handle gracefully
}
```

### 4. Testing
```csharp
[Fact]
public void TestSentimentClassification()
{
    var classifier = new SentimentClassifier(modelPath, tokenizerPath);
    var (label, confidence) = classifier.Classify("Great!");

    Assert.Equal("POSITIVE", label);
    Assert.True(confidence > 0.5f);
}
```

---

**Last Updated:** 2026-01-19
