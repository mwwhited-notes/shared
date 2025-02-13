# OCR Notes

## Labeling

- https://www.youtube.com/watch?v=J0fNhvc3J7s
- https://github.com/microsoft/OCR-Form-Tools

## OCR

- [Surya](https://github.com/VikParuchuri/surya)
  - OCR in 90+ languages that benchmarks favorably vs cloud services
  - Line-level text detection in any language
  - Layout analysis (table, image, header, etc detection)
  - Reading order detection
  - Table recognition (detecting rows/columns)
- https://www.reddit.com/r/LocalLLaMA/comments/1hep8xa/recommendations_for_the_best_ocr_model_for/
- [Qwen2-VL](https://github.com/QwenLM/Qwen2-VL)
- [Pixtral 12B](https://mistral.ai/news/pixtral-12b/)
- [Extracting Structured Data from Complex Docs Using LLMs | Numind/NuExtract 1.5 Guide V2](https://www.youtube.com/watch?v=mqxQP0oT4Dg)
- [Fine-tune LiLT model for Information extraction from Image and PDF documents | UBIAI | Train LiLT |](https://www.youtube.com/watch?v=EVONngnrJbE)
- [Van Lindberg Structured Data from Unstructured Text PyCon 2016](https://www.youtube.com/watch?v=-K-XtxSyyvU)

## Datasets

- https://huggingface.co/datasets
- https://www.kaggle.com/datasets
- https://github.com/mukunku/ParquetViewer
- https://github.com/aloneguid/parquet-dotnet

## Models

- https://huggingface.co/microsoft/layoutlmv3-base
  - https://medium.com/dair-ai/papers-explained-10-layout-lm-32ec4bad6406
- https://huggingface.co/docs/transformers/model_doc/lilt

### LiLT

- https://medium.com/dair-ai/papers-explained-12-lilt-701057ec6d9e

### LayoutVM x

- https://medium.com/@matt.noe/tutorial-how-to-train-layoutlm-on-a-custom-dataset-with-hugging-face-cda58c96571c
- https://medium.com/@shivarama/layoutlmv3-from-zero-to-hero-part-2-d2659eaa7dee

## IDE Assistant

- https://ollama.com/blog/continue-code-assistant
- https://medium.com/@smfraser/how-to-use-a-local-llm-as-a-free-coding-copilot-in-vs-code-6dffc053369d
- https://www.pedroalonso.net/blog/local-ai-assitance-with-continue-ollama-vscode/#setting-up-your-environment
- https://www.2am.tech/blog/integrate-ollama-with-visual-studio-code-for-ai-coding-assistance

## General Notes

- https://github.com/meta-llama/llama/issues/176
- https://arxiv.org/html/2401.01313v2 - A Comprehensive Survey of Hallucination Mitigatio…
- https://medium.com/@yash9439/run-any-llm-on-distributed-multiple-gpus-locally-using-llama-cpp-2ff478a0dc3c
- https://www.csail.mit.edu/news/science-paper-if-transistors-cant-get-smaller-then-software-developers-have-get-smarter
- https://www.theverge.com/circuitbreaker/2016/10/6/13187820/one-nanometer-transistor-berkeley-lab-moores-law
- https://news.mit.edu/2020/mit-csail-computing-technology-after-moores-law-0605
- https://qz.com/852770/theres-a-limit-to-how-small-we-can-make-transistors-but-the-solution-is-photonic-chips
- https://towardsdatascience.com/memory-efficient-embeddings-d637cba7f006
- https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken
- https://medium.com/geekculture/mastering-token-costs-in-chatgpt-and-other-large-language-models-e724e36b4dca
- https://www.nytimes.com/2024/04/29/technology/ai-startups-financial-reality.html
- https://www.businessinsider.com/openai-2022-losses-hit-540-million-as-chatgpt-costs-soared-2023-5
- https://learn.microsoft.com/en-us/azure/aks/gpu-cluster
- https://www.postgresql.org/docs/current/explicit-locking.html
- https://stackoverflow.com/questions/61596711/in-kubernetes-how-can-i-scale-a-deployment-to-zero-when-idle
- https://youtu.be/cXw4mZZXJNU?si=ShMFPWJX4qTMd6iF
- https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding
- https://github.com/vyraun/Half-Size
- https://arxiv.org/abs/1708.03629 - [1708.03629] Simple and Effective Dimensionality…
- https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding
- https://www.linkedin.com/posts/tscottclendaniel_bigdata-datascience-machinelearning-activity-7194035623815479296-xKBl?utm_source=share&utm_medium=member_ios
- https://www.gartner.com/en/articles/what-s-new-in-the-2023-gartner-hype-cycle-for-emerging-technologies
- https://github.com/ollama/ollama/blob/main/docs/modelfile.md#valid-parameters-and-values
- https://huggingface.co/microsoft/git-base
- https://huggingface.co/microsoft/trocr-large-printed
- https://www.businessinsider.com/openai-destroyed-ai-training-datasets-lawsuit-authors-books-copyright-2024-5
- https://medium.com/@jm_51428/long-context-window-models-vs-rag-a73c35a763f2
- https://electrosome.com/xor-xnor-logic-function-diode-bridge-transistor/
- https://en.wikipedia.org/wiki/Binary_multiplier

## SQL

- [Install SQL Server Full-Text Search on Linux - SQL Server | Microsoft Learn](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-full-text-search?view=sql-server-ver16&tabs=rhel)
- [semantickeyphrasetable (Transact-SQL) - SQL Server | Microsoft Learn](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/semantickeyphrasetable-transact-sql?view=sql-server-ver16)
- [Semantic Search (SQL Server) - SQL Server | Microsoft Learn](https://learn.microsoft.com/en-us/sql/relational-databases/search/semantic-search-sql-server?view=sql-server-ver16#whatcanido)
- [https://www.kodyaz.com/sql-server-2014/fulltext-index-semantic-search-in-sql-server-2014.aspx](https://www.kodyaz.com/sql-server-2014/fulltext-index-semantic-search-in-sql-server-2014.aspx)
- [OpenSearch Dashboards - OpenSearch Documentation](https://www.opensearch.org/docs/latest/dashboards/)
- [10 Best Elasticsearch Alternatives in 2024 | ClickUp](https://clickup.com/blog/elasticsearch-alternatives/)
- [Keyword search - OpenSearch Documentation](https://opensearch.org/docs/latest/search-plugins/keyword-search/)


[.NET
clients - OpenSearch Documentation](https://opensearch.org/docs/latest/clients/dot-net/)

**From:** Matt Whited [[matt@whited.us](mailto:matt@whited.us)](%5Bmatt@whited.us%5D(mailto:matt@whited.us))

**Sent:** Sunday, March 3, 2024 4:30 PM

**To:** Matt Whited [[matt.whited@lightwellinc.com](mailto:matt.whited@lightwellinc.com)](%5Bmatt.whited@lightwellinc.com%5D(mailto:matt.whited@lightwellinc.com));
Matt Whited [[matt@whited.us](mailto:matt@whited.us)](%5Bmatt@whited.us%5D(mailto:matt@whited.us))

**Subject:**

[Data Version Control · DVC](https://dvc.org/)

[A
Modern Approach to Versioning Large Files for Machine learning and more | by
Dave Flynn | InfuseAI](https://blog.infuseai.io/a-modern-approach-to-versioning-large-datasets-for-machine-learning-fca2f541dd85)

[fstanis/awesome-webdav:
A curated list of awesome apps that support WebDAV and tools related to it.
(github.com)](https://github.com/fstanis/awesome-webdav)

[WebDAV Projects](http://webdav.org/projects/)

[sabre/dav](https://sabre.io/)

## Modules

[submodule "Scripts/LiLT/LiLT"]
	path = Scripts/LiLT/LiLT
	url = https://github.com/jpWang/LiLT.git
[submodule "Notes/AI ML Stuff/SimilaritySearchExample"]
	path = Notes/AI ML Stuff/SimilaritySearchExample
	url = https://github.com/EliassenInnovation/SimilaritySearchExample.git
[submodule "Notes/AI ML Stuff/VirtualRecruiter"]
	path = Notes/AI ML Stuff/VirtualRecruiter
	url = https://github.com/OutOfBandDevelopment/VirtualRecruiter.git
[submodule "Notes/AI ML Stuff/Transformers-Tutorials"]
	path = Notes/AI ML Stuff/Transformers-Tutorials
	url = https://github.com/mwwhited/Transformers-Tutorials.git
[submodule "Notes/AI ML Stuff/all-mpnet-base-v2-onnx"]
	path = Notes/AI ML Stuff/all-mpnet-base-v2-onnx
	url = https://huggingface.co/onnx-models/all-mpnet-base-v2-onnx
[submodule "Notes/AI ML Stuff/OMR-scanned-documents"]
	path = Notes/AI ML Stuff/OMR-scanned-documents
	url = https://huggingface.co/datasets/saurabh1896/OMR-scanned-documents/
