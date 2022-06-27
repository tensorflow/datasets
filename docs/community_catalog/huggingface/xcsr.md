# xcsr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/xcsr)
*   [Huggingface](https://huggingface.co/datasets/xcsr)


## X-CSQA-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-en')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-zh')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-de')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-es')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-fr')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-it')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-jap


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-jap')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-nl')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-pl')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-pt')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-ru')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-ar


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-ar')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-vi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-vi')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-hi')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-sw


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-sw')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CSQA-ur


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CSQA-ur')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1074
`'validation'` | 1000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-en')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-zh')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-de')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-es')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-fr')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-it')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-jap


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-jap')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-nl')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-pl')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-pt')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-ru')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-ar


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-ar')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-vi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-vi')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-hi')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-sw


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-sw')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## X-CODAH-ur


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xcsr/X-CODAH-ur')
```

*   **Description**:

```
To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "stem": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "choices": {
                "feature": {
                    "label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
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
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


