# nli_tr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/nli_tr)
*   [Huggingface](https://huggingface.co/datasets/nli_tr)


## snli_tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nli_tr/snli_tr')
```

*   **Description**:

```
The Natural Language Inference in Turkish (NLI-TR) is a set of two large scale datasets that were obtained by translating the foundational NLI corpora (SNLI and MNLI) using Amazon Translate.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 550152
`'validation'` | 10000

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
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
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## multinli_tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nli_tr/multinli_tr')
```

*   **Description**:

```
The Natural Language Inference in Turkish (NLI-TR) is a set of two large scale datasets that were obtained by translating the foundational NLI corpora (SNLI and MNLI) using Amazon Translate.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 392702
`'validation_matched'` | 10000
`'validation_mismatched'` | 10000

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
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
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


