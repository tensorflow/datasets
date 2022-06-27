# enriched_web_nlg

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/enriched_web_nlg)
*   [Huggingface](https://huggingface.co/datasets/enriched_web_nlg)


## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:enriched_web_nlg/en')
```

*   **Description**:

```
WebNLG is a valuable resource and benchmark for the Natural Language Generation (NLG) community. However, as other NLG benchmarks, it only consists of a collection of parallel raw representations and their corresponding textual realizations. This work aimed to provide intermediate representations of the data for the development and evaluation of popular tasks in the NLG pipeline architecture (Reiter and Dale, 2000), such as Discourse Ordering, Lexicalization, Aggregation and Referring Expression Generation.
```

*   **License**: CC Attribution-Noncommercial-Share Alike 4.0 International
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 872
`'test'` | 1862
`'train'` | 6940

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
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
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
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
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "template": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "sorted_triple_sets": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "lexicalization": {
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
```



## de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:enriched_web_nlg/de')
```

*   **Description**:

```
WebNLG is a valuable resource and benchmark for the Natural Language Generation (NLG) community. However, as other NLG benchmarks, it only consists of a collection of parallel raw representations and their corresponding textual realizations. This work aimed to provide intermediate representations of the data for the development and evaluation of popular tasks in the NLG pipeline architecture (Reiter and Dale, 2000), such as Discourse Ordering, Lexicalization, Aggregation and Referring Expression Generation.
```

*   **License**: CC Attribution-Noncommercial-Share Alike 4.0 International
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 872
`'train'` | 6940

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
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
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
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
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "template": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "sorted_triple_sets": {
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
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


