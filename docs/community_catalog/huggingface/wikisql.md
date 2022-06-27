# wikisql

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wikisql)
*   [Huggingface](https://huggingface.co/datasets/wikisql)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikisql')
```

*   **Description**:

```
A large crowd-sourced dataset for developing natural language interfaces for relational databases
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15878
`'train'` | 56355
`'validation'` | 8421

*   **Features**:

```json
{
    "phase": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table": {
        "header": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "page_title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "page_id": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "types": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "id": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "section_title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "caption": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "rows": {
            "feature": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "sql": {
        "human_readable": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "sel": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "agg": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "conds": {
            "feature": {
                "column_index": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "operator_index": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "condition": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    }
}
```


