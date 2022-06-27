# taskmaster1

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/taskmaster1)
*   [Huggingface](https://huggingface.co/datasets/taskmaster1)


## one_person_dialogs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster1/one_person_dialogs')
```

*   **Description**:

```
Taskmaster-1:Toward a Realistic and Diverse Dialog Dataset) is an evaluation set for commonsense question-answering in the sentence completion style of SWAG. As opposed to other automatically generated NLI datasets, CODAH is adversarially constructed by humans who can view feedback from a pre-trained model and use this information to design challenging commonsense questions. Our experimental results show that CODAH questions present a complementary extension to the SWAG dataset, testing additional modes of common sense.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 770
`'train'` | 6168
`'validation'` | 770

*   **Features**:

```json
{
    "conversation_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "instruction_id": {
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



## woz_dialogs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster1/woz_dialogs')
```

*   **Description**:

```
Taskmaster-1:Toward a Realistic and Diverse Dialog Dataset) is an evaluation set for commonsense question-answering in the sentence completion style of SWAG. As opposed to other automatically generated NLI datasets, CODAH is adversarially constructed by humans who can view feedback from a pre-trained model and use this information to design challenging commonsense questions. Our experimental results show that CODAH questions present a complementary extension to the SWAG dataset, testing additional modes of common sense.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5507

*   **Features**:

```json
{
    "conversation_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "instruction_id": {
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


