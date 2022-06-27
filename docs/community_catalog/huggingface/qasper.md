# qasper

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/qasper)
*   [Huggingface](https://huggingface.co/datasets/qasper)


## qasper


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qasper/qasper')
```

*   **Description**:

```
A dataset containing 1585 papers with 5049 information-seeking questions asked by regular readers of NLP papers, and answered by a separate set of NLP practitioners.
```

*   **License**: CC BY 4.0
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 888
`'validation'` | 281

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstract": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "full_text": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "paragraphs": [
                {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            ]
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "qas": {
        "feature": {
            "question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "question_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "nlp_background": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "topic_background": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "paper_read": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_query": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "question_writer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answers": {
                "feature": {
                    "answer": {
                        "unanswerable": {
                            "dtype": "bool",
                            "id": null,
                            "_type": "Value"
                        },
                        "extractive_spans": {
                            "feature": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "length": -1,
                            "id": null,
                            "_type": "Sequence"
                        },
                        "yes_no": {
                            "dtype": "bool",
                            "id": null,
                            "_type": "Value"
                        },
                        "free_form_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence": {
                            "feature": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "length": -1,
                            "id": null,
                            "_type": "Sequence"
                        },
                        "highlighted_evidence": {
                            "feature": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "length": -1,
                            "id": null,
                            "_type": "Sequence"
                        }
                    },
                    "annotation_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "worker_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
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


