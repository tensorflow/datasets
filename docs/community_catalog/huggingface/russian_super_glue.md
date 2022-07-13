# russian_super_glue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/russian_super_glue)
*   [Huggingface](https://huggingface.co/datasets/russian_super_glue)


## lidirus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/lidirus')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
"LiDiRus (Linguistic Diagnostic for Russian) is a diagnostic dataset that covers a large volume of linguistic phenomena,
while allowing you to evaluate information systems on a simple test of textual entailment recognition.
See more details diagnostics.
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1104

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "knowledge": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lexical-semantics": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "logic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "predicate-argument-structure": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "entailment",
            "not_entailment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## rcb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/rcb')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
The Russian Commitment Bank is a corpus of naturally occurring discourses whose final sentence contains
a clause-embedding predicate under an entailment canceling operator (question, modal, negation, antecedent
of conditional).
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 438
`'train'` | 438
`'validation'` | 220

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "verb": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "negation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "contradiction",
            "neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## parus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/parus')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
Choice of Plausible Alternatives for Russian language
Choice of Plausible Alternatives for Russian language (PARus) evaluation provides researchers with a tool for assessing
progress in open-domain commonsense causal reasoning. Each question in PARus is composed of a premise and two
alternatives, where the task is to select the alternative that more plausibly has a causal relation with the premise.
The correct alternative is randomized so that the expected performance of randomly guessing is 50%.
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 400
`'validation'` | 100

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "choice1",
            "choice2"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## muserc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/muserc')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
We present a reading comprehension challenge in which questions can only be answered by taking into account information
from multiple sentences. The dataset is the first to study multi-sentence inference at scale, with an open-ended set of
question types that requires reasoning skills.
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7614
`'train'` | 11950
`'validation'` | 2235

*   **Features**:

```json
{
    "paragraph": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "paragraph": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "question": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "answer": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        }
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## terra


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/terra')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
Textual Entailment Recognition has been proposed recently as a generic task that captures major semantic inference
needs across many NLP applications, such as Question Answering, Information Retrieval, Information Extraction,
and Text Summarization. This task requires to recognize, given two text fragments, whether the meaning of one text is
entailed (can be inferred) from the other text.
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3198
`'train'` | 2616
`'validation'` | 307

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "entailment",
            "not_entailment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## russe


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/russe')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
WiC: The Word-in-Context Dataset A reliable benchmark for the evaluation of context-sensitive word embeddings.
Depending on its context, an ambiguous word can refer to multiple, potentially unrelated, meanings. Mainstream static
word embeddings, such as Word2vec and GloVe, are unable to reflect this dynamic semantic nature. Contextualised word
embeddings are an attempt at addressing this limitation by computing dynamic representations for words which can adapt
based on context.
Russian SuperGLUE task borrows original data from the Russe project, Word Sense Induction and Disambiguation
shared task (2018)
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 18892
`'train'` | 19845
`'validation'` | 8505

*   **Features**:

```json
{
    "word": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "start1": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "start2": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end1": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end2": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "gold_sense1": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "gold_sense2": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## rwsd


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/rwsd')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
A Winograd schema is a pair of sentences that differ in only one or two words and that contain an ambiguity that is
resolved in opposite ways in the two sentences and requires the use of world knowledge and reasoning for its resolution.
The schema takes its name from a well-known example by Terry Winograd.
The set would then be presented as a challenge for AI programs, along the lines of the Turing test. The strengths of
the challenge are that it is clear-cut, in that the answer to each schema is a binary choice; vivid, in that it is
obvious to non-experts that a program that fails to get the right answers clearly has serious gaps in its understanding;
and difficult, in that it is far beyond the current state of the art.
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 154
`'train'` | 606
`'validation'` | 204

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span1_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "span2_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "span1_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span2_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## danetqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/danetqa')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
DaNetQA is a question answering dataset for yes/no questions. These questions are naturally occurring -- they are
generated in unprompted and unconstrained settings.

Each example is a triplet of (question, passage, answer), with the title of the page as optional additional context.
The text-pair classification setup is similar to existing natural language inference tasks.

By sampling questions from a distribution of information-seeking queries (rather than prompting annotators for
text pairs), we observe significantly more challenging examples compared to existing NLI datasets.
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 805
`'train'` | 1749
`'validation'` | 821

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "passage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## rucos


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:russian_super_glue/rucos')
```

*   **Description**:

```
Recent advances in the field of universal language models and transformers require the development of a methodology for
their broad diagnostics and testing for general intellectual skills - detection of natural language inference,
commonsense reasoning, ability to perform simple logical operations regardless of text subject or lexicon. For the first
time, a benchmark of nine tasks, collected and organized analogically to the SuperGLUE methodology, was developed from
scratch for the Russian language. We provide baselines, human level evaluation, an open-source framework for evaluating
models and an overall leaderboard of transformer models for the Russian language.
Russian reading comprehension with Commonsense reasoning (RuCoS) is a large-scale reading comprehension dataset which
requires commonsense reasoning. RuCoS consists of queries automatically generated from CNN/Daily Mail news articles;
the answer to each query is a text span from a summarizing passage of the corresponding news. The goal of RuCoS is to
evaluate a machine`s ability of commonsense reasoning in reading comprehension.
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7257
`'train'` | 72193
`'validation'` | 7577

*   **Features**:

```json
{
    "passage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entities": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "idx": {
        "passage": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "query": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        }
    }
}
```


