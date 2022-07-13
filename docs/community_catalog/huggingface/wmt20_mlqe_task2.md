# wmt20_mlqe_task2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wmt20_mlqe_task2)
*   [Huggingface](https://huggingface.co/datasets/wmt20_mlqe_task2)


## en-de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task2/en-de')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 2 evaluates the application of QE for post-editing purposes. It consists of predicting:
- A/ Word-level tags. This is done both on source side (to detect which words caused errors)
and target side (to detect mistranslated or missing words).
  - A1/ Each token is tagged as either `OK` or `BAD`. Additionally,
  each gap between two words is tagged as `BAD` if one or more
  missing words should have been there, and `OK` otherwise. Note
  that number of tags for each target sentence is 2*N+1, where
  N is the number of tokens in the sentence.
  - A2/ Tokens are tagged as `OK` if they were correctly
  translated, and `BAD` otherwise. Gaps are not tagged.
- B/ Sentence-level HTER scores. HTER (Human Translation Error Rate)
is the ratio between the number of edits (insertions/deletions/replacements)
needed and the reference translation length.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "de"
        ],
        "id": null,
        "_type": "Translation"
    },
    "src_tags": {
        "feature": {
            "num_classes": 2,
            "names": [
                "BAD",
                "OK"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mt_tags": {
        "feature": {
            "num_classes": 2,
            "names": [
                "BAD",
                "OK"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pe": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hter": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "alignments": {
        "feature": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task2/en-zh')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 2 evaluates the application of QE for post-editing purposes. It consists of predicting:
- A/ Word-level tags. This is done both on source side (to detect which words caused errors)
and target side (to detect mistranslated or missing words).
  - A1/ Each token is tagged as either `OK` or `BAD`. Additionally,
  each gap between two words is tagged as `BAD` if one or more
  missing words should have been there, and `OK` otherwise. Note
  that number of tags for each target sentence is 2*N+1, where
  N is the number of tokens in the sentence.
  - A2/ Tokens are tagged as `OK` if they were correctly
  translated, and `BAD` otherwise. Gaps are not tagged.
- B/ Sentence-level HTER scores. HTER (Human Translation Error Rate)
is the ratio between the number of edits (insertions/deletions/replacements)
needed and the reference translation length.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "zh"
        ],
        "id": null,
        "_type": "Translation"
    },
    "src_tags": {
        "feature": {
            "num_classes": 2,
            "names": [
                "BAD",
                "OK"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mt_tags": {
        "feature": {
            "num_classes": 2,
            "names": [
                "BAD",
                "OK"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pe": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hter": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "alignments": {
        "feature": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


