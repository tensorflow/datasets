# narrativeqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/narrativeqa)
*   [Huggingface](https://huggingface.co/datasets/narrativeqa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:narrativeqa')
```

*   **Description**:

```
The NarrativeQA dataset for question answering on long documents (movie scripts, books). It includes the list of documents with Wikipedia summaries, links to full stories, and questions and answers.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10557
`'train'` | 32747
`'validation'` | 3461

*   **Features**:

```json
{
    "document": {
        "id": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "kind": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "file_size": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "word_count": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "start": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "end": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "summary": {
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
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
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
    "answers": [
        {
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
        }
    ]
}
```


