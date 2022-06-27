# multi_woz_v22

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multi_woz_v22)
*   [Huggingface](https://huggingface.co/datasets/multi_woz_v22)


## v2.2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_woz_v22/v2.2')
```

*   **Description**:

```
Multi-Domain Wizard-of-Oz dataset (MultiWOZ), a fully-labeled collection of human-human written conversations spanning over multiple domains and topics.
MultiWOZ 2.1 (Eric et al., 2019) identified and fixed many erroneous annotations and user utterances in the original version, resulting in an
improved version of the dataset. MultiWOZ 2.2 is a yet another improved version of this dataset, which identifies and fizes dialogue state annotation errors
across 17.3% of the utterances on top of MultiWOZ 2.1 and redefines the ontology by disallowing vocabularies of slots with a large number of possible values
(e.g., restaurant name, time of booking) and introducing standardized slot span annotations for these slots.
```

*   **License**: Apache License 2.0
*   **Version**: 2.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 8437
`'validation'` | 1000

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
            "turn_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "speaker": {
                "num_classes": 2,
                "names": [
                    "USER",
                    "SYSTEM"
                ],
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
                        "slots_values": {
                            "feature": {
                                "slots_values_name": {
                                    "dtype": "string",
                                    "id": null,
                                    "_type": "Value"
                                },
                                "slots_values_list": {
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
                    "slots": {
                        "feature": {
                            "slot": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "value": {
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
                            },
                            "copy_from": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "copy_from_value": {
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
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "dialogue_acts": {
                "dialog_act": {
                    "feature": {
                        "act_type": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "act_slots": {
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
                        }
                    },
                    "length": -1,
                    "id": null,
                    "_type": "Sequence"
                },
                "span_info": {
                    "feature": {
                        "act_type": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "act_slot_name": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "act_slot_value": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "span_start": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "span_end": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## v2.2_active_only


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_woz_v22/v2.2_active_only')
```

*   **Description**:

```
Multi-Domain Wizard-of-Oz dataset (MultiWOZ), a fully-labeled collection of human-human written conversations spanning over multiple domains and topics.
MultiWOZ 2.1 (Eric et al., 2019) identified and fixed many erroneous annotations and user utterances in the original version, resulting in an
improved version of the dataset. MultiWOZ 2.2 is a yet another improved version of this dataset, which identifies and fizes dialogue state annotation errors
across 17.3% of the utterances on top of MultiWOZ 2.1 and redefines the ontology by disallowing vocabularies of slots with a large number of possible values
(e.g., restaurant name, time of booking) and introducing standardized slot span annotations for these slots.
```

*   **License**: Apache License 2.0
*   **Version**: 2.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 8437
`'validation'` | 1000

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
            "turn_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "speaker": {
                "num_classes": 2,
                "names": [
                    "USER",
                    "SYSTEM"
                ],
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
                        "slots_values": {
                            "feature": {
                                "slots_values_name": {
                                    "dtype": "string",
                                    "id": null,
                                    "_type": "Value"
                                },
                                "slots_values_list": {
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
                    "slots": {
                        "feature": {
                            "slot": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "value": {
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
                            },
                            "copy_from": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "copy_from_value": {
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
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "dialogue_acts": {
                "dialog_act": {
                    "feature": {
                        "act_type": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "act_slots": {
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
                        }
                    },
                    "length": -1,
                    "id": null,
                    "_type": "Sequence"
                },
                "span_info": {
                    "feature": {
                        "act_type": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "act_slot_name": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "act_slot_value": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "span_start": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "span_end": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


