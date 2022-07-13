# flue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/flue)
*   [Huggingface](https://huggingface.co/datasets/flue)


## CLS


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:flue/CLS')
```

*   **Description**:

```
FLUE is an evaluation setup for French NLP systems similar to the popular GLUE benchmark. The goal is to enable further reproducible experiments in the future and to share models and progress on the French language.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5999
`'train'` | 5997

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
            "negative",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## PAWS-X


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:flue/PAWS-X')
```

*   **Description**:

```
FLUE is an evaluation setup for French NLP systems similar to the popular GLUE benchmark. The goal is to enable further reproducible experiments in the future and to share models and progress on the French language.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 49399
`'validation'` | 1988

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
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## XNLI


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:flue/XNLI')
```

*   **Description**:

```
FLUE is an evaluation setup for French NLP systems similar to the popular GLUE benchmark. The goal is to enable further reproducible experiments in the future and to share models and progress on the French language.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5010
`'train'` | 392702
`'validation'` | 2490

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypo": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "contradiction",
            "entailment",
            "neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## WSD-V


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:flue/WSD-V')
```

*   **Description**:

```
FLUE is an evaluation setup for French NLP systems similar to the popular GLUE benchmark. The goal is to enable further reproducible experiments in the future and to share models and progress on the French language.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3121
`'train'` | 269821

*   **Features**:

```json
{
    "sentence": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pos_tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "lemmas": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "fine_pos_tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "disambiguate_tokens_ids": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "disambiguate_labels": {
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
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


