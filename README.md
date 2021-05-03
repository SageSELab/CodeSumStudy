# CodeSummarizationEmpiricalStudy

### Project structure
#### CodeBERT
The source code for this model is forked from [CodeXGLUE-Repository](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Text/code-to-text).
Some small changes are applied. However, we follow the same instructions for fine-tuning and inference. 
- CodeBERT/preprocessing: Contains the preprocessing techniques applied in the [Funcom](http://leclair.tech/data/funcom/) dataset. Some of the techniques are chosen from [previous work](https://arxiv.org/abs/2102.02017).

#### NeuralCodeSum:
The source code for this model is forked from [NeuralCodeSum-Repository](https://github.com/wasiahmad/NeuralCodeSum). We follow the same steps for training/testing the model.
- NeuralCodeSum/preprocessing: In addition to preprocessing techniques applied in the CodeBERT, we added some other preprocessing techniques, e.g., split tokens for this model.

#### Code2seq
We used the open-source implementation from [code2seq-repo](https://github.com/tech-srl/code2seq)
- code2seq/JavaExtractor: modified dataset-build and AST generation files. Original repo: [LRNavin/AutoComments](https://github.com/LRNavin/AutoComments)
- code2seq/preproc: dataset preprocess folder (part of AST generation) with slight modification in code2seq/preproc/feature_extractor.py

### Experiments
- code2seq/code2seq_commands.ipynb: Notebook containing Funcom data preprocessing steps for code2seq, study result analysis and statistical significance test for BLEU score

#### Qualitative Study Results
This folder contains all the categories selected by each of the annotators. Also, the final categories after resolving conflicts are also mentioned there for each of the samples.