# casino

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/casino)
*   [Huggingface](https://huggingface.co/datasets/casino)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:casino')
```

*   **Description**:

```
We provide a novel dataset (referred to as CaSiNo) of 1030 negotiation dialogues. Two participants take the role of campsite neighbors and negotiate for Food, Water, and Firewood packages, based on their individual preferences and requirements. This design keeps the task tractable, while still facilitating linguistically rich and personal conversations. This helps to overcome the limitations of prior negotiation datasets such as Deal or No Deal and Craigslist Bargain. Each dialogue consists of rich meta-data including participant demographics, personality, and their subjective evaluation of the negotiation in terms of satisfaction and opponent likeness.
```

*   **License**: The project is licensed under CC-BY-4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1030

*   **Features**:

```json
{
    "chat_logs": [
        {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "task_data": {
                "data": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "issue2youget": {
                    "Firewood": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Water": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Food": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "issue2theyget": {
                    "Firewood": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Water": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Food": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            },
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "participant_info": {
        "mturk_agent_1": {
            "value2issue": {
                "Low": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "Medium": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "High": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "value2reason": {
                "Low": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "Medium": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "High": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "outcomes": {
                "points_scored": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "satisfaction": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "opponent_likeness": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "demographics": {
                "age": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "gender": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "ethnicity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "education": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "personality": {
                "svo": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "big-five": {
                    "extraversion": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "agreeableness": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "conscientiousness": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "emotional-stability": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "openness-to-experiences": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    }
                }
            }
        },
        "mturk_agent_2": {
            "value2issue": {
                "Low": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "Medium": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "High": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "value2reason": {
                "Low": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "Medium": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "High": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "outcomes": {
                "points_scored": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "satisfaction": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "opponent_likeness": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "demographics": {
                "age": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "gender": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "ethnicity": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "education": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "personality": {
                "svo": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "big-five": {
                    "extraversion": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "agreeableness": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "conscientiousness": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "emotional-stability": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "openness-to-experiences": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    }
                }
            }
        }
    },
    "annotations": [
        [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    ]
}
```


