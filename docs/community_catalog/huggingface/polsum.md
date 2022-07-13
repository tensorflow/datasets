# polsum

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/polsum)
*   [Huggingface](https://huggingface.co/datasets/polsum)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:polsum')
```

*   **Description**:

```
Polish Summaries Corpus: the corpus of Polish news summaries.
```

*   **License**: CC BY v.3
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 569

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "section": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "authors": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summaries": {
        "feature": {
            "ratio": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "author": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "body": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "spans": {
                "feature": {
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
                    "span_text": {
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


