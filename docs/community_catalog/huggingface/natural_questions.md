# natural_questions

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/natural_questions)
*   [Huggingface](https://huggingface.co/datasets/natural_questions)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:natural_questions')
```

*   **Description**:

```
The NQ corpus contains questions from real users, and it requires QA systems to
read and comprehend an entire Wikipedia article that may or may not contain the
answer to the question. The inclusion of real user questions, and the
requirement that solutions should read an entire page to find the answer, cause
NQ to be a more realistic and challenging task than prior QA datasets.
```

*   **License**: No known license
*   **Version**: 0.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 307373
`'validation'` | 7830

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document": {
        "title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "html": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "tokens": {
            "feature": {
                "token": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "is_html": {
                    "dtype": "bool",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "question": {
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "tokens": {
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
    "annotations": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "long_answer": {
                "start_token": {
                    "dtype": "int64",
                    "id": null,
                    "_type": "Value"
                },
                "end_token": {
                    "dtype": "int64",
                    "id": null,
                    "_type": "Value"
                },
                "start_byte": {
                    "dtype": "int64",
                    "id": null,
                    "_type": "Value"
                },
                "end_byte": {
                    "dtype": "int64",
                    "id": null,
                    "_type": "Value"
                }
            },
            "short_answers": {
                "feature": {
                    "start_token": {
                        "dtype": "int64",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_token": {
                        "dtype": "int64",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_byte": {
                        "dtype": "int64",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_byte": {
                        "dtype": "int64",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "yes_no_answer": {
                "num_classes": 2,
                "names": [
                    "NO",
                    "YES"
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


