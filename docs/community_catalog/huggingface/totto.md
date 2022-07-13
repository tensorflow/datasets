# totto

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/totto)
*   [Huggingface](https://huggingface.co/datasets/totto)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:totto')
```

*   **Description**:

```
ToTTo is an open-domain English table-to-text dataset with over 120,000 training examples that proposes a controlled generation task: given a Wikipedia table and a set of highlighted table cells, produce a one-sentence description.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7700
`'train'` | 120761
`'validation'` | 7700

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "table_page_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_webpage_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_section_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_section_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table": [
        [
            {
                "column_span": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "is_header": {
                    "dtype": "bool",
                    "id": null,
                    "_type": "Value"
                },
                "row_span": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "value": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            }
        ]
    ],
    "highlighted_cells": {
        "feature": {
            "feature": {
                "dtype": "int32",
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
    "example_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_annotations": {
        "feature": {
            "original_sentence": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "sentence_after_deletion": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "sentence_after_ambiguity": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "final_sentence": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "overlap_subset": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


