# multidoc2dial

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multidoc2dial)
*   [Huggingface](https://huggingface.co/datasets/multidoc2dial)


## dialogue_domain


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multidoc2dial/dialogue_domain')
```

*   **Description**:

```
MultiDoc2Dial is a new task and dataset on modeling goal-oriented dialogues grounded in multiple documents. Most previous works treat document-grounded dialogue modeling as a machine reading comprehension task based on a single given document or passage. We aim to address more realistic scenarios where a goal-oriented information-seeking conversation involves multiple topics, and hence is grounded on different documents.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3474
`'validation'` | 661

*   **Features**:

```json
{
    "dial_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "turns": [
        {
            "turn_id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "role": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "da": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "references": [
                {
                    "id_sp": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "doc_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ],
            "utterance": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```



## document_domain


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multidoc2dial/document_domain')
```

*   **Description**:

```
MultiDoc2Dial is a new task and dataset on modeling goal-oriented dialogues grounded in multiple documents. Most previous works treat document-grounded dialogue modeling as a machine reading comprehension task based on a single given document or passage. We aim to address more realistic scenarios where a goal-oriented information-seeking conversation involves multiple topics, and hence is grounded on different documents.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 488

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "doc_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "spans": [
        {
            "id_sp": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "tag": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "start_sp": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end_sp": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text_sp": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "parent_titles": {
                "feature": {
                    "id_sp": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "level": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "id_sec": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "start_sec": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text_sec": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "end_sec": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "doc_html_ts": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "doc_html_raw": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## multidoc2dial


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multidoc2dial/multidoc2dial')
```

*   **Description**:

```
MultiDoc2Dial is a new task and dataset on modeling goal-oriented dialogues grounded in multiple documents. Most previous works treat document-grounded dialogue modeling as a machine reading comprehension task based on a single given document or passage. We aim to address more realistic scenarios where a goal-oriented information-seeking conversation involves multiple topics, and hence is grounded on different documents.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5
`'train'` | 21451
`'validation'` | 4201

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
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "da": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


