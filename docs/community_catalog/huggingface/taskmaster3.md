# taskmaster3

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/taskmaster3)
*   [Huggingface](https://huggingface.co/datasets/taskmaster3)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster3')
```

*   **Description**:

```
Taskmaster is dataset for goal oriented conversations. The Taskmaster-3 dataset consists of 23,757 movie ticketing dialogs. By "movie ticketing" we mean conversations where the customer's goal is to purchase tickets after deciding on theater, time, movie name, number of tickets, and date, or opt out of the transaction. This collection was created using the "self-dialog" method. This means a single, crowd-sourced worker is paid to create a conversation writing turns for both speakers, i.e. the customer and the ticketing agent.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 23757

*   **Features**:

```json
{
    "conversation_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "vertical": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "instructions": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "scenario": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterances": [
        {
            "index": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "speaker": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "apis": [
                {
                    "name": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "index": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "args": [
                        {
                            "arg_name": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "arg_value": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        }
                    ],
                    "response": [
                        {
                            "response_name": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            },
                            "response_value": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        }
                    ]
                }
            ],
            "segments": [
                {
                    "start_index": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_index": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "annotations": [
                        {
                            "name": {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
```


