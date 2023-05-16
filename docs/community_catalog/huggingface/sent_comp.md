# sent_comp

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sent_comp)
*   [Huggingface](https://huggingface.co/datasets/sent_comp)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sent_comp')
```

*   **Description**:

```
Large corpus of uncompressed and compressed sentences from news articles.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 200000
`'validation'` | 10000

*   **Features**:

```json
{
    "graph": {
        "id": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "sentence": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "node": {
            "feature": {
                "form": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "mid": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "word": {
                    "feature": {
                        "id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "form": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "stem": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "tag": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    },
                    "length": -1,
                    "id": null,
                    "_type": "Sequence"
                },
                "gender": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "head_word_index": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "edge": {
            "feature": {
                "parent_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "child_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "entity_mention": {
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
                "head": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "name": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "mid": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "is_proper_name_entity": {
                    "dtype": "bool",
                    "id": null,
                    "_type": "Value"
                },
                "gender": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "compression": {
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "edge": {
            "feature": {
                "parent_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "child_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "headline": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "compression_ratio": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source_tree": {
        "id": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "sentence": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "node": {
            "feature": {
                "form": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "mid": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "word": {
                    "feature": {
                        "id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "form": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "stem": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "tag": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    },
                    "length": -1,
                    "id": null,
                    "_type": "Sequence"
                },
                "gender": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "head_word_index": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "edge": {
            "feature": {
                "parent_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "child_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "entity_mention": {
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
                "head": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "name": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "mid": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "is_proper_name_entity": {
                    "dtype": "bool",
                    "id": null,
                    "_type": "Value"
                },
                "gender": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "compression_untransformed": {
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "edge": {
            "feature": {
                "parent_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "child_id": {
                    "dtype": "int32",
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


