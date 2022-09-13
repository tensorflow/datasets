# mutual_friends

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mutual_friends)
*   [Huggingface](https://huggingface.co/datasets/mutual_friends)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mutual_friends/plain_text')
```

*   **Description**:

```
Our goal is to build systems that collaborate with people by exchanging
information through natural language and reasoning over structured knowledge
base. In the MutualFriend task, two agents, A and B, each have a private
knowledge base, which contains a list of friends with multiple attributes
(e.g., name, school, major, etc.). The agents must chat with each other
to find their unique mutual friend.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1107
`'train'` | 8967
`'validation'` | 1083

*   **Features**:

```json
{
    "uuid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "scenario_uuid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "scenario_alphas": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "scenario_attributes": {
        "feature": {
            "unique": {
                "dtype": "bool_",
                "id": null,
                "_type": "Value"
            },
            "value_type": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "scenario_kbs": {
        "feature": {
            "feature": {
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
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "agents": {
        "1": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "0": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "outcome_reward": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "events": {
        "actions": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "start_times": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "data_messages": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "data_selects": {
            "feature": {
                "attributes": {
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
        "agents": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "times": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    }
}
```


