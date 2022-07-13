# ethos

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ethos)
*   [Huggingface](https://huggingface.co/datasets/ethos)


## binary


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ethos/binary')
```

*   **Description**:

```

```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 998

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "no_hate_speech",
            "hate_speech"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## multilabel


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ethos/multilabel')
```

*   **Description**:

```

```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 433

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "violence": {
        "num_classes": 2,
        "names": [
            "not_violent",
            "violent"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "directed_vs_generalized": {
        "num_classes": 2,
        "names": [
            "generalied",
            "directed"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "gender": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "race": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "national_origin": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "disability": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "religion": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "sexual_orientation": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


