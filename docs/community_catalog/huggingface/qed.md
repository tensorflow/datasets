# qed

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/qed)
*   [Huggingface](https://huggingface.co/datasets/qed)


## qed


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qed/qed')
```

*   **Description**:

```
QED, is a linguistically informed, extensible framework for explanations in question answering. A QED explanation specifies the relationship between a question and answer according to formal semantic notions such as referential equality, sentencehood, and entailment. It is an expertannotated dataset of QED explanations built upon a subset of the Google Natural Questions dataset.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7638
`'validation'` | 1355

*   **Features**:

```json
{
    "example_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "title_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paragraph_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_starts": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "original_nq_answers": [
        {
            "start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "string": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "annotation": {
        "referential_equalities": [
            {
                "question_reference": {
                    "start": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "string": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "sentence_reference": {
                    "start": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "bridge": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "string": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            }
        ],
        "answer": [
            {
                "sentence_reference": {
                    "start": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "bridge": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "string": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "paragraph_reference": {
                    "start": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "string": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            }
        ],
        "explanation_type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "selected_sentence": {
            "start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "string": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    }
}
```


