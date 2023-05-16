# doc2dial

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/doc2dial)
*   [Huggingface](https://huggingface.co/datasets/doc2dial)


## dialogue_domain


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:doc2dial/dialogue_domain')
```

*   **Description**:

```
Doc2dial is dataset of goal-oriented dialogues that are grounded in the associated documents. It includes over 4500 annotated conversations with an average of 14 turns that are grounded in over 450 documents from four domains. Compared to the prior document-grounded dialogue datasets this dataset covers a variety of dialogue scenes in information-seeking conversations.
```

*   **License**: No known license
*   **Version**: 1.0.1
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
    "doc_id": {
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
                    "sp_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "label": {
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
ds = tfds.load('huggingface:doc2dial/document_domain')
```

*   **Description**:

```
Doc2dial is dataset of goal-oriented dialogues that are grounded in the associated documents. It includes over 4500 annotated conversations with an average of 14 turns that are grounded in over 450 documents from four domains. Compared to the prior document-grounded dialogue datasets this dataset covers a variety of dialogue scenes in information-seeking conversations.
```

*   **License**: No known license
*   **Version**: 1.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3416

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
                "dtype": "string",
                "id": null,
                "_type": "Value"
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



## doc2dial_rc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:doc2dial/doc2dial_rc')
```

*   **Description**:

```
Doc2dial is dataset of goal-oriented dialogues that are grounded in the associated documents. It includes over 4500 annotated conversations with an average of 14 turns that are grounded in over 450 documents from four domains. Compared to the prior document-grounded dialogue datasets this dataset covers a variety of dialogue scenes in information-seeking conversations.
```

*   **License**: No known license
*   **Version**: 1.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 20431
`'validation'` | 3972

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
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


