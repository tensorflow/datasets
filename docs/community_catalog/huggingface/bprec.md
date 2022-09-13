# bprec

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bprec)
*   [Huggingface](https://huggingface.co/datasets/bprec)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bprec')
```

*   **Description**:

```
Dataset consisting of Polish language texts annotated to recognize brand-product relations.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'banking'` | 561
`'cosmetics'` | 2384
`'electro'` | 382
`'tele'` | 2391

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ner": {
        "feature": {
            "source": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            },
            "target": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## all


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bprec/all')
```

*   **Description**:

```
Dataset consisting of Polish language texts annotated to recognize brand-product relations.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5718

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ner": {
        "feature": {
            "source": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            },
            "target": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## tele


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bprec/tele')
```

*   **Description**:

```
Dataset consisting of Polish language texts annotated to recognize brand-product relations.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2391

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ner": {
        "feature": {
            "source": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            },
            "target": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## electro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bprec/electro')
```

*   **Description**:

```
Dataset consisting of Polish language texts annotated to recognize brand-product relations.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 382

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ner": {
        "feature": {
            "source": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            },
            "target": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## cosmetics


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bprec/cosmetics')
```

*   **Description**:

```
Dataset consisting of Polish language texts annotated to recognize brand-product relations.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2384

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ner": {
        "feature": {
            "source": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            },
            "target": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## banking


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bprec/banking')
```

*   **Description**:

```
Dataset consisting of Polish language texts annotated to recognize brand-product relations.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 561

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ner": {
        "feature": {
            "source": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            },
            "target": {
                "from": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "to": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "type": {
                    "num_classes": 10,
                    "names": [
                        "PRODUCT_NAME",
                        "PRODUCT_NAME_IMP",
                        "PRODUCT_NO_BRAND",
                        "BRAND_NAME",
                        "BRAND_NAME_IMP",
                        "VERSION",
                        "PRODUCT_ADJ",
                        "BRAND_ADJ",
                        "LOCATION",
                        "LOCATION_IMP"
                    ],
                    "names_file": null,
                    "id": null,
                    "_type": "ClassLabel"
                }
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


