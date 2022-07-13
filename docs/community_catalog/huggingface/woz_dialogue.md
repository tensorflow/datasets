# woz_dialogue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/woz_dialogue)
*   [Huggingface](https://huggingface.co/datasets/woz_dialogue)


## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:woz_dialogue/en')
```

*   **Description**:

```
Wizard-of-Oz (WOZ) is a dataset for training task-oriented dialogue systems. The dataset is designed around the task of finding a restaurant in the Cambridge, UK area. There are three informable slots (food, pricerange,area) that users can use to constrain the search and six requestable slots (address, phone, postcode plus the three informable slots) that the user can ask a value for once a restaurant has been offered.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 400
`'train'` | 600
`'validation'` | 200

*   **Features**:

```json
{
    "dialogue_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dialogue": [
        {
            "turn_label": {
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
            "asr": {
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
            "system_transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "turn_idx": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "belief_state": [
                {
                    "slots": {
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
                    "act": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ],
            "transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "system_acts": {
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
            }
        }
    ]
}
```



## de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:woz_dialogue/de')
```

*   **Description**:

```
Wizard-of-Oz (WOZ) is a dataset for training task-oriented dialogue systems. The dataset is designed around the task of finding a restaurant in the Cambridge, UK area. There are three informable slots (food, pricerange,area) that users can use to constrain the search and six requestable slots (address, phone, postcode plus the three informable slots) that the user can ask a value for once a restaurant has been offered.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 400
`'train'` | 600
`'validation'` | 200

*   **Features**:

```json
{
    "dialogue_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dialogue": [
        {
            "turn_label": {
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
            "asr": {
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
            "system_transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "turn_idx": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "belief_state": [
                {
                    "slots": {
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
                    "act": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ],
            "transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "system_acts": {
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
            }
        }
    ]
}
```



## de_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:woz_dialogue/de_en')
```

*   **Description**:

```
Wizard-of-Oz (WOZ) is a dataset for training task-oriented dialogue systems. The dataset is designed around the task of finding a restaurant in the Cambridge, UK area. There are three informable slots (food, pricerange,area) that users can use to constrain the search and six requestable slots (address, phone, postcode plus the three informable slots) that the user can ask a value for once a restaurant has been offered.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 400
`'train'` | 600
`'validation'` | 200

*   **Features**:

```json
{
    "dialogue_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dialogue": [
        {
            "turn_label": {
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
            "asr": {
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
            "system_transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "turn_idx": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "belief_state": [
                {
                    "slots": {
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
                    "act": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ],
            "transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "system_acts": {
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
            }
        }
    ]
}
```



## it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:woz_dialogue/it')
```

*   **Description**:

```
Wizard-of-Oz (WOZ) is a dataset for training task-oriented dialogue systems. The dataset is designed around the task of finding a restaurant in the Cambridge, UK area. There are three informable slots (food, pricerange,area) that users can use to constrain the search and six requestable slots (address, phone, postcode plus the three informable slots) that the user can ask a value for once a restaurant has been offered.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 400
`'train'` | 600
`'validation'` | 200

*   **Features**:

```json
{
    "dialogue_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dialogue": [
        {
            "turn_label": {
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
            "asr": {
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
            "system_transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "turn_idx": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "belief_state": [
                {
                    "slots": {
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
                    "act": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ],
            "transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "system_acts": {
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
            }
        }
    ]
}
```



## it_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:woz_dialogue/it_en')
```

*   **Description**:

```
Wizard-of-Oz (WOZ) is a dataset for training task-oriented dialogue systems. The dataset is designed around the task of finding a restaurant in the Cambridge, UK area. There are three informable slots (food, pricerange,area) that users can use to constrain the search and six requestable slots (address, phone, postcode plus the three informable slots) that the user can ask a value for once a restaurant has been offered.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 400
`'train'` | 600
`'validation'` | 200

*   **Features**:

```json
{
    "dialogue_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dialogue": [
        {
            "turn_label": {
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
            "asr": {
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
            "system_transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "turn_idx": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "belief_state": [
                {
                    "slots": {
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
                    "act": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ],
            "transcript": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "system_acts": {
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
            }
        }
    ]
}
```


