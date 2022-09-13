# schema_guided_dstc8

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/schema_guided_dstc8)
*   [Huggingface](https://huggingface.co/datasets/schema_guided_dstc8)


## dialogues


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:schema_guided_dstc8/dialogues')
```

*   **Description**:

```
The Schema-Guided Dialogue dataset (SGD) was developed for the Dialogue State Tracking task of the Eights Dialogue Systems Technology Challenge (dstc8).
The SGD dataset consists of over 18k annotated multi-domain, task-oriented conversations between a human and a virtual assistant.
These conversations involve interactions with services and APIs spanning 17 domains, ranging from banks and events to media, calendar, travel, and weather.
For most of these domains, the SGD dataset contains multiple different APIs, many of which have overlapping functionalities but different interfaces,
which reflects common real-world scenarios.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4201
`'train'` | 16142
`'validation'` | 2482

*   **Features**:

```json
{
    "dialogue_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "services": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "turns": {
        "feature": {
            "speaker": {
                "num_classes": 2,
                "names": [
                    "USER",
                    "SYSTEM"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "utterance": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "frames": {
                "feature": {
                    "service": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "slots": {
                        "feature": {
                            "slot": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "start": {
                                "dtype": "int32",
                                "id": null,
                                "_type": "Value"
                            },
                            "exclusive_end": {
                                "dtype": "int32",
                                "id": null,
                                "_type": "Value"
                            }
                        },
                        "length": -1,
                        "id": null,
                        "_type": "Sequence"
                    },
                    "state": {
                        "active_intent": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "requested_slots": {
                            "feature": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "length": -1,
                            "id": null,
                            "_type": "Sequence"
                        },
                        "slot_values": {
                            "feature": {
                                "slot_name": {
                                    "dtype": "string",
                                    "id": null,
                                    "_type": "Value"
                                },
                                "slot_value_list": {
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
                    },
                    "actions": {
                        "feature": {
                            "act": {
                                "num_classes": 18,
                                "names": [
                                    "AFFIRM",
                                    "AFFIRM_INTENT",
                                    "CONFIRM",
                                    "GOODBYE",
                                    "INFORM",
                                    "INFORM_COUNT",
                                    "INFORM_INTENT",
                                    "NEGATE",
                                    "NEGATE_INTENT",
                                    "NOTIFY_FAILURE",
                                    "NOTIFY_SUCCESS",
                                    "OFFER",
                                    "OFFER_INTENT",
                                    "REQUEST",
                                    "REQUEST_ALTS",
                                    "REQ_MORE",
                                    "SELECT",
                                    "THANK_YOU"
                                ],
                                "names_file": null,
                                "id": null,
                                "_type": "ClassLabel"
                            },
                            "slot": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "canonical_values": {
                                "feature": {
                                    "dtype": "string",
                                    "id": null,
                                    "_type": "Value"
                                },
                                "length": -1,
                                "id": null,
                                "_type": "Sequence"
                            },
                            "values": {
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
                    "service_results": {
                        "feature": {
                            "service_results_list": {
                                "feature": {
                                    "service_slot_name": {
                                        "dtype": "string",
                                        "id": null,
                                        "_type": "Value"
                                    },
                                    "service_canonical_value": {
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
                    "service_call": {
                        "method": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "parameters": {
                            "feature": {
                                "parameter_slot_name": {
                                    "dtype": "string",
                                    "id": null,
                                    "_type": "Value"
                                },
                                "parameter_canonical_value": {
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



## schema


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:schema_guided_dstc8/schema')
```

*   **Description**:

```
The Schema-Guided Dialogue dataset (SGD) was developed for the Dialogue State Tracking task of the Eights Dialogue Systems Technology Challenge (dstc8).
The SGD dataset consists of over 18k annotated multi-domain, task-oriented conversations between a human and a virtual assistant.
These conversations involve interactions with services and APIs spanning 17 domains, ranging from banks and events to media, calendar, travel, and weather.
For most of these domains, the SGD dataset contains multiple different APIs, many of which have overlapping functionalities but different interfaces,
which reflects common real-world scenarios.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 21
`'train'` | 26
`'validation'` | 17

*   **Features**:

```json
{
    "service_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "slots": {
        "feature": {
            "name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "is_categorical": {
                "dtype": "bool",
                "id": null,
                "_type": "Value"
            },
            "possible_values": {
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
    "intents": {
        "feature": {
            "name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "is_transactional": {
                "dtype": "bool",
                "id": null,
                "_type": "Value"
            },
            "required_slots": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "optional_slots": {
                "feature": {
                    "slot_name": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "slot_value": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "result_slots": {
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


