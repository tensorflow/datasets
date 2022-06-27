# sofc_materials_articles

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sofc_materials_articles)
*   [Huggingface](https://huggingface.co/datasets/sofc_materials_articles)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sofc_materials_articles')
```

*   **Description**:

```
The SOFC-Exp corpus consists of 45 open-access scholarly articles annotated by domain experts.
A corpus and an inter-annotator agreement study demonstrate the complexity of the suggested
named entity recognition and slot filling tasks as well as high annotation quality is presented
in the accompanying paper.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11
`'train'` | 26
`'validation'` | 8

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_offsets": {
        "feature": {
            "begin_char_offset": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "end_char_offset": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "sentences": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "sentence_labels": {
        "feature": {
            "dtype": "int64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "token_offsets": {
        "feature": {
            "offsets": {
                "feature": {
                    "begin_char_offset": {
                        "dtype": "int64",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_char_offset": {
                        "dtype": "int64",
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
    "tokens": {
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
    "entity_labels": {
        "feature": {
            "feature": {
                "num_classes": 9,
                "names": [
                    "B-DEVICE",
                    "B-EXPERIMENT",
                    "B-MATERIAL",
                    "B-VALUE",
                    "I-DEVICE",
                    "I-EXPERIMENT",
                    "I-MATERIAL",
                    "I-VALUE",
                    "O"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "slot_labels": {
        "feature": {
            "feature": {
                "num_classes": 39,
                "names": [
                    "B-anode_material",
                    "B-cathode_material",
                    "B-conductivity",
                    "B-current_density",
                    "B-degradation_rate",
                    "B-device",
                    "B-electrolyte_material",
                    "B-experiment_evoking_word",
                    "B-fuel_used",
                    "B-interlayer_material",
                    "B-interconnect_material",
                    "B-open_circuit_voltage",
                    "B-power_density",
                    "B-resistance",
                    "B-support_material",
                    "B-thickness",
                    "B-time_of_operation",
                    "B-voltage",
                    "B-working_temperature",
                    "I-anode_material",
                    "I-cathode_material",
                    "I-conductivity",
                    "I-current_density",
                    "I-degradation_rate",
                    "I-device",
                    "I-electrolyte_material",
                    "I-experiment_evoking_word",
                    "I-fuel_used",
                    "I-interlayer_material",
                    "I-interconnect_material",
                    "I-open_circuit_voltage",
                    "I-power_density",
                    "I-resistance",
                    "I-support_material",
                    "I-thickness",
                    "I-time_of_operation",
                    "I-voltage",
                    "I-working_temperature",
                    "O"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
        "feature": {
            "relation_label": {
                "num_classes": 4,
                "names": [
                    "coreference",
                    "experiment_variation",
                    "same_experiment",
                    "thickness"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "start_span_id": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "end_span_id": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "slots": {
        "feature": {
            "frame_participant_label": {
                "num_classes": 15,
                "names": [
                    "anode_material",
                    "cathode_material",
                    "current_density",
                    "degradation_rate",
                    "device",
                    "electrolyte_material",
                    "fuel_used",
                    "interlayer_material",
                    "open_circuit_voltage",
                    "power_density",
                    "resistance",
                    "support_material",
                    "time_of_operation",
                    "voltage",
                    "working_temperature"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "slot_id": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "spans": {
        "feature": {
            "span_id": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "entity_label": {
                "num_classes": 4,
                "names": [
                    "",
                    "DEVICE",
                    "MATERIAL",
                    "VALUE"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "sentence_id": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "experiment_mention_type": {
                "num_classes": 5,
                "names": [
                    "",
                    "current_exp",
                    "future_work",
                    "general_info",
                    "previous_work"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "begin_char_offset": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "end_char_offset": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "experiments": {
        "feature": {
            "experiment_id": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "span_id": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "slots": {
                "feature": {
                    "frame_participant_label": {
                        "num_classes": 16,
                        "names": [
                            "anode_material",
                            "cathode_material",
                            "current_density",
                            "degradation_rate",
                            "conductivity",
                            "device",
                            "electrolyte_material",
                            "fuel_used",
                            "interlayer_material",
                            "open_circuit_voltage",
                            "power_density",
                            "resistance",
                            "support_material",
                            "time_of_operation",
                            "voltage",
                            "working_temperature"
                        ],
                        "names_file": null,
                        "id": null,
                        "_type": "ClassLabel"
                    },
                    "slot_id": {
                        "dtype": "int64",
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
    }
}
```


