# ambig_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ambig_qa)
*   [Huggingface](https://huggingface.co/datasets/ambig_qa)


## light


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ambig_qa/light')
```

*   **Description**:

```
AmbigNQ, a dataset covering 14,042 questions from NQ-open, an existing open-domain QA benchmark. We find that over half of the questions in NQ-open are ambiguous. The types of ambiguity are diverse and sometimes subtle, many of which are only apparent after examining evidence provided by a very large text corpus.  AMBIGNQ, a dataset with
14,042 annotations on NQ-OPEN questions containing diverse types of ambiguity.
We provide two distributions of our new dataset AmbigNQ: a full version with all annotation metadata and a light version with only inputs and outputs.
```

*   **License**: CC BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10036
`'validation'` | 2002

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotations": {
        "feature": {
            "type": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "qaPairs": {
                "feature": {
                    "question": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "answer": {
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



## full


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ambig_qa/full')
```

*   **Description**:

```
AmbigNQ, a dataset covering 14,042 questions from NQ-open, an existing open-domain QA benchmark. We find that over half of the questions in NQ-open are ambiguous. The types of ambiguity are diverse and sometimes subtle, many of which are only apparent after examining evidence provided by a very large text corpus.  AMBIGNQ, a dataset with
14,042 annotations on NQ-OPEN questions containing diverse types of ambiguity.
We provide two distributions of our new dataset AmbigNQ: a full version with all annotation metadata and a light version with only inputs and outputs.
```

*   **License**: CC BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10036
`'validation'` | 2002

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotations": {
        "feature": {
            "type": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "qaPairs": {
                "feature": {
                    "question": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "answer": {
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
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "viewed_doc_titles": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "used_queries": {
        "feature": {
            "query": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "results": {
                "feature": {
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "snippet": {
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
    },
    "nq_answer": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "nq_doc_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


