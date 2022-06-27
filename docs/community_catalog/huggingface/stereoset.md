# stereoset

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/stereoset)
*   [Huggingface](https://huggingface.co/datasets/stereoset)


## intersentence


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:stereoset/intersentence')
```

*   **Description**:

```
Stereoset is a dataset that measures stereotype bias in language models. Stereoset consists of 17,000 sentences that
measures model preferences across gender, race, religion, and profession.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 2123

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bias_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentences": {
        "feature": {
            "sentence": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "labels": {
                "feature": {
                    "label": {
                        "num_classes": 4,
                        "names": [
                            "anti-stereotype",
                            "stereotype",
                            "unrelated",
                            "related"
                        ],
                        "names_file": null,
                        "id": null,
                        "_type": "ClassLabel"
                    },
                    "human_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "gold_label": {
                "num_classes": 3,
                "names": [
                    "anti-stereotype",
                    "stereotype",
                    "unrelated"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## intrasentence


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:stereoset/intrasentence')
```

*   **Description**:

```
Stereoset is a dataset that measures stereotype bias in language models. Stereoset consists of 17,000 sentences that
measures model preferences across gender, race, religion, and profession.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 2106

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bias_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentences": {
        "feature": {
            "sentence": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "labels": {
                "feature": {
                    "label": {
                        "num_classes": 4,
                        "names": [
                            "anti-stereotype",
                            "stereotype",
                            "unrelated",
                            "related"
                        ],
                        "names_file": null,
                        "id": null,
                        "_type": "ClassLabel"
                    },
                    "human_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "gold_label": {
                "num_classes": 3,
                "names": [
                    "anti-stereotype",
                    "stereotype",
                    "unrelated"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


