# tne

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tne)
*   [Huggingface](https://huggingface.co/datasets/tne)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tne')
```

*   **Description**:

```
TNE is an NLU task, which focus on relations between noun phrases (NPs) that can be mediated via prepositions.
The dataset contains 5,497 documents, annotated exhaustively with all possible links between the NPs in each document.
```

*   **License**: MIT
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'test_ood'` | 509
`'train'` | 3988
`'validation'` | 500

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
    "nps": [
        {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "first_char": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "last_char": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "first_token": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "last_token": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "np_relations": [
        {
            "anchor": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "complement": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "preposition": {
                "num_classes": 24,
                "names": [
                    "about",
                    "for",
                    "with",
                    "from",
                    "among",
                    "by",
                    "on",
                    "at",
                    "during",
                    "of",
                    "member(s) of",
                    "in",
                    "after",
                    "under",
                    "to",
                    "into",
                    "before",
                    "near",
                    "outside",
                    "around",
                    "between",
                    "against",
                    "over",
                    "inside"
                ],
                "id": null,
                "_type": "ClassLabel"
            },
            "complement_coref_cluster_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "coref": [
        {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "members": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "np_type": {
                "num_classes": 3,
                "names": [
                    "standard",
                    "time/date/measurement",
                    "idiomatic"
                ],
                "id": null,
                "_type": "ClassLabel"
            }
        }
    ],
    "metadata": {
        "annotators": {
            "coref_worker": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "consolidator_worker": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "np-relations_worker": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "source": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```


