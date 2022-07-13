# hybrid_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hybrid_qa)
*   [Huggingface](https://huggingface.co/datasets/hybrid_qa)


## hybrid_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hybrid_qa/hybrid_qa')
```

*   **Description**:

```
Existing question answering datasets focus on dealing with homogeneous information, based either only on text or KB/Table information alone. However, as human knowledge is distributed over heterogeneous forms, using homogeneous information alone might lead to severe coverage problems. To fill in the gap, we present HybridQA, a new large-scale question-answering dataset that requires reasoning on heterogeneous information. Each question is aligned with a Wikipedia table and multiple free-form corpora linked with the entities in the table. The questions are designed to aggregate both tabular information and text information, i.e., lack of either form would render the question unanswerable.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3463
`'train'` | 62682
`'validation'` | 3466

*   **Features**:

```json
{
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_postag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table": {
        "url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
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
        "data": [
            {
                "value": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "urls": [
                    {
                        "url": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "summary": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    }
                ]
            }
        ],
        "section_title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "section_text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "uid": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "intro": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```


