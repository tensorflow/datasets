# persian_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/persian_ner)
*   [Huggingface](https://huggingface.co/datasets/persian_ner)


## fold1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:persian_ner/fold1')
```

*   **Description**:

```
The dataset includes 250,015 tokens and 7,682 Persian sentences in total. It is available in 3 folds to be used in turn as training and test sets. The NER tags are in IOB format.
```

*   **License**: Creative Commons Attribution 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2560
`'train'` | 5121

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 13,
            "names": [
                "O",
                "I-event",
                "I-fac",
                "I-loc",
                "I-org",
                "I-pers",
                "I-pro",
                "B-event",
                "B-fac",
                "B-loc",
                "B-org",
                "B-pers",
                "B-pro"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## fold2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:persian_ner/fold2')
```

*   **Description**:

```
The dataset includes 250,015 tokens and 7,682 Persian sentences in total. It is available in 3 folds to be used in turn as training and test sets. The NER tags are in IOB format.
```

*   **License**: Creative Commons Attribution 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2561
`'train'` | 5120

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 13,
            "names": [
                "O",
                "I-event",
                "I-fac",
                "I-loc",
                "I-org",
                "I-pers",
                "I-pro",
                "B-event",
                "B-fac",
                "B-loc",
                "B-org",
                "B-pers",
                "B-pro"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## fold3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:persian_ner/fold3')
```

*   **Description**:

```
The dataset includes 250,015 tokens and 7,682 Persian sentences in total. It is available in 3 folds to be used in turn as training and test sets. The NER tags are in IOB format.
```

*   **License**: Creative Commons Attribution 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2560
`'train'` | 5121

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 13,
            "names": [
                "O",
                "I-event",
                "I-fac",
                "I-loc",
                "I-org",
                "I-pers",
                "I-pro",
                "B-event",
                "B-fac",
                "B-loc",
                "B-org",
                "B-pers",
                "B-pro"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


