# kilt_wikipedia

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kilt_wikipedia)
*   [Huggingface](https://huggingface.co/datasets/kilt_wikipedia)


## 2019-08-01


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_wikipedia/2019-08-01')
```

*   **Description**:

```
KILT-Wikipedia: Wikipedia pre-processed for KILT.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'full'` | 5903530

*   **Features**:

```json
{
    "kilt_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "wikipedia_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "wikipedia_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "feature": {
            "paragraph": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "anchors": {
        "feature": {
            "paragraph_id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
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
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "href": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wikipedia_title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wikipedia_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "categories": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "wikidata_info": {
        "description": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "enwikiquote_title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "wikidata_id": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "wikidata_label": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "wikipedia_title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "aliases": {
            "feature": {
                "alias": {
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
    "history": {
        "pageid": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "parentid": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "revid": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "pre_dump": {
            "dtype": "bool",
            "id": null,
            "_type": "Value"
        },
        "timestamp": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```


