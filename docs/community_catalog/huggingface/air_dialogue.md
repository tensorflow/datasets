# air_dialogue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/air_dialogue)
*   [Huggingface](https://huggingface.co/datasets/air_dialogue)


## air_dialogue_data


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:air_dialogue/air_dialogue_data')
```

*   **Description**:

```
AirDialogue, is a large dataset that contains 402,038 goal-oriented conversations. To collect this dataset, we create a contextgenerator which provides travel and flight restrictions. Then the human annotators are asked to play the role of a customer or an agent and interact with the goal of successfully booking a trip given the restrictions.
```

*   **License**: cc-by-nc-4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 321459
`'validation'` | 40363

*   **Features**:

```json
{
    "action": {
        "status": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "flight": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "intent": {
        "return_month": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "return_day": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "max_price": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "departure_airport": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "max_connections": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "departure_day": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "goal": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "departure_month": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "return_airport": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "timestamps": {
        "feature": {
            "dtype": "int64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "dialogue": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "expected_action": {
        "status": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "flight": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "search_info": [
        {
            "button_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "field_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "field_value": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "timestmamp": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "correct_sample": {
        "dtype": "bool_",
        "id": null,
        "_type": "Value"
    }
}
```



## air_dialogue_kb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:air_dialogue/air_dialogue_kb')
```

*   **Description**:

```
AirDialogue, is a large dataset that contains 402,038 goal-oriented conversations. To collect this dataset, we create a contextgenerator which provides travel and flight restrictions. Then the human annotators are asked to play the role of a customer or an agent and interact with the goal of successfully booking a trip given the restrictions.
```

*   **License**: cc-by-nc-4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 321459
`'validation'` | 40363

*   **Features**:

```json
{
    "kb": [
        {
            "airline": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "class": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "departure_airport": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "departure_day": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "departure_month": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "departure_time_num": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "flight_number": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "num_connections": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "price": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "return_airport": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "return_day": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "return_month": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "return_time_num": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "reservation": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


