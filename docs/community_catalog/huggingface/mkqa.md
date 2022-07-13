# mkqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mkqa)
*   [Huggingface](https://huggingface.co/datasets/mkqa)


## mkqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mkqa/mkqa')
```

*   **Description**:

```
We introduce MKQA, an open-domain question answering evaluation set comprising 10k question-answer pairs aligned across 26 typologically diverse languages (260k question-answer pairs in total). The goal of this dataset is to provide a challenging benchmark for question answering quality across a wide set of languages.
```

*   **License**: CC BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10000

*   **Features**:

```json
{
    "example_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "queries": {
        "ar": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "da": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "de": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "en": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "es": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "fi": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "fr": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "he": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "hu": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "it": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "ja": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "ko": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "km": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "ms": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "nl": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "no": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "pl": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "pt": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "ru": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "sv": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "th": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "tr": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "vi": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "zh_cn": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "zh_hk": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "zh_tw": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "ar": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "da": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "de": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "en": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "es": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "fi": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "fr": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "he": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "hu": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "it": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "ja": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "ko": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "km": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "ms": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "nl": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "no": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "pl": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "pt": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "ru": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "sv": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "th": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "tr": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "vi": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "zh_cn": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "zh_hk": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ],
        "zh_tw": [
            {
                "type": {
                    "num_classes": 8,
                    "names": [
                        "entity",
                        "long_answer",
                        "unanswerable",
                        "date",
                        "number",
                        "number_with_unit",
                        "short_phrase",
                        "binary"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                },
                "entity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "aliases": [
                    {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                ]
            }
        ]
    }
}
```


