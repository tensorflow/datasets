# kor_nli

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kor_nli)
*   [Huggingface](https://huggingface.co/datasets/kor_nli)


## multi_nli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_nli/multi_nli')
```

*   **Description**:

```
Korean Natural  Language Inference datasets
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 392702

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



## snli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_nli/snli')
```

*   **Description**:

```
Korean Natural  Language Inference datasets
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 550152

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



## xnli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_nli/xnli')
```

*   **Description**:

```
Korean Natural  Language Inference datasets
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5010
`'validation'` | 2490

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


