# selqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/selqa)
*   [Huggingface](https://huggingface.co/datasets/selqa)


## answer_selection_analysis


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:selqa/answer_selection_analysis')
```

*   **Description**:

```
The SelQA dataset provides crowdsourced annotation for two selection-based question answer tasks, 
answer sentence selection and answer triggering.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1590
`'train'` | 5529
`'validation'` | 785

*   **Features**:

```json
{
    "section": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "is_paraphrase": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "topic": {
        "num_classes": 10,
        "names": [
            "MUSIC",
            "TV",
            "TRAVEL",
            "ART",
            "SPORT",
            "COUNTRY",
            "MOVIES",
            "HISTORICAL EVENTS",
            "SCIENCE",
            "FOOD"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "answers": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "q_types": {
        "feature": {
            "num_classes": 7,
            "names": [
                "what",
                "why",
                "when",
                "who",
                "where",
                "how",
                ""
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



## answer_selection_experiments


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:selqa/answer_selection_experiments')
```

*   **Description**:

```
The SelQA dataset provides crowdsourced annotation for two selection-based question answer tasks, 
answer sentence selection and answer triggering.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 19435
`'train'` | 66438
`'validation'` | 9377

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## answer_triggering_analysis


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:selqa/answer_triggering_analysis')
```

*   **Description**:

```
The SelQA dataset provides crowdsourced annotation for two selection-based question answer tasks, 
answer sentence selection and answer triggering.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1590
`'train'` | 5529
`'validation'` | 785

*   **Features**:

```json
{
    "section": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "is_paraphrase": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "topic": {
        "num_classes": 10,
        "names": [
            "MUSIC",
            "TV",
            "TRAVEL",
            "ART",
            "SPORT",
            "COUNTRY",
            "MOVIES",
            "HISTORICAL EVENTS",
            "SCIENCE",
            "FOOD"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "q_types": {
        "feature": {
            "num_classes": 7,
            "names": [
                "what",
                "why",
                "when",
                "who",
                "where",
                "how",
                ""
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "candidate_list": {
        "feature": {
            "article": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "section": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "candidates": {
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
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## answer_triggering_experiments


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:selqa/answer_triggering_experiments')
```

*   **Description**:

```
The SelQA dataset provides crowdsourced annotation for two selection-based question answer tasks, 
answer sentence selection and answer triggering.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 59845
`'train'` | 205075
`'validation'` | 28798

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


