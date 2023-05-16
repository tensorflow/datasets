# taskmaster2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/taskmaster2)
*   [Huggingface](https://huggingface.co/datasets/taskmaster2)


## flights


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster2/flights')
```

*   **Description**:

```
Taskmaster is dataset for goal oriented conversations. The Taskmaster-2 dataset consists of 17,289 dialogs in the seven domains which include restaurants, food ordering, movies, hotels, flights, music and sports. Unlike Taskmaster-1, which includes both written "self-dialogs" and spoken two-person dialogs, Taskmaster-2 consists entirely of spoken two-person dialogs. In addition, while Taskmaster-1 is almost exclusively task-based, Taskmaster-2 contains a good number of search- and recommendation-oriented dialogs. All dialogs in this release were created using a Wizard of Oz (WOz) methodology in which crowdsourced workers played the role of a 'user' and trained call center operators played the role of the 'assistant'. In this way, users were led to believe they were interacting with an automated system that “spoke” using text-to-speech (TTS) even though it was in fact a human behind the scenes. As a result, users could express themselves however they chose in the context of an automated interface.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2481

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



## food-ordering


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster2/food-ordering')
```

*   **Description**:

```
Taskmaster is dataset for goal oriented conversationas. The Taskmaster-2 dataset consists of 17,289 dialogs in the seven domains which include restaurants, food ordering, movies, hotels, flights, music and sports. Unlike Taskmaster-1, which includes both written "self-dialogs" and spoken two-person dialogs, Taskmaster-2 consists entirely of spoken two-person dialogs. In addition, while Taskmaster-1 is almost exclusively task-based, Taskmaster-2 contains a good number of search- and recommendation-oriented dialogs. All dialogs in this release were created using a Wizard of Oz (WOz) methodology in which crowdsourced workers played the role of a 'user' and trained call center operators played the role of the 'assistant'. In this way, users were led to believe they were interacting with an automated system that “spoke” using text-to-speech (TTS) even though it was in fact a human behind the scenes. As a result, users could express themselves however they chose in the context of an automated interface.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1050

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



## hotels


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster2/hotels')
```

*   **Description**:

```
Taskmaster is dataset for goal oriented conversationas. The Taskmaster-2 dataset consists of 17,289 dialogs in the seven domains which include restaurants, food ordering, movies, hotels, flights, music and sports. Unlike Taskmaster-1, which includes both written "self-dialogs" and spoken two-person dialogs, Taskmaster-2 consists entirely of spoken two-person dialogs. In addition, while Taskmaster-1 is almost exclusively task-based, Taskmaster-2 contains a good number of search- and recommendation-oriented dialogs. All dialogs in this release were created using a Wizard of Oz (WOz) methodology in which crowdsourced workers played the role of a 'user' and trained call center operators played the role of the 'assistant'. In this way, users were led to believe they were interacting with an automated system that “spoke” using text-to-speech (TTS) even though it was in fact a human behind the scenes. As a result, users could express themselves however they chose in the context of an automated interface.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2357

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



## movies


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster2/movies')
```

*   **Description**:

```
Taskmaster is dataset for goal oriented conversationas. The Taskmaster-2 dataset consists of 17,289 dialogs in the seven domains which include restaurants, food ordering, movies, hotels, flights, music and sports. Unlike Taskmaster-1, which includes both written "self-dialogs" and spoken two-person dialogs, Taskmaster-2 consists entirely of spoken two-person dialogs. In addition, while Taskmaster-1 is almost exclusively task-based, Taskmaster-2 contains a good number of search- and recommendation-oriented dialogs. All dialogs in this release were created using a Wizard of Oz (WOz) methodology in which crowdsourced workers played the role of a 'user' and trained call center operators played the role of the 'assistant'. In this way, users were led to believe they were interacting with an automated system that “spoke” using text-to-speech (TTS) even though it was in fact a human behind the scenes. As a result, users could express themselves however they chose in the context of an automated interface.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3056

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



## music


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster2/music')
```

*   **Description**:

```
Taskmaster is dataset for goal oriented conversationas. The Taskmaster-2 dataset consists of 17,289 dialogs in the seven domains which include restaurants, food ordering, movies, hotels, flights, music and sports. Unlike Taskmaster-1, which includes both written "self-dialogs" and spoken two-person dialogs, Taskmaster-2 consists entirely of spoken two-person dialogs. In addition, while Taskmaster-1 is almost exclusively task-based, Taskmaster-2 contains a good number of search- and recommendation-oriented dialogs. All dialogs in this release were created using a Wizard of Oz (WOz) methodology in which crowdsourced workers played the role of a 'user' and trained call center operators played the role of the 'assistant'. In this way, users were led to believe they were interacting with an automated system that “spoke” using text-to-speech (TTS) even though it was in fact a human behind the scenes. As a result, users could express themselves however they chose in the context of an automated interface.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1603

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



## restaurant-search


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster2/restaurant-search')
```

*   **Description**:

```
Taskmaster is dataset for goal oriented conversationas. The Taskmaster-2 dataset consists of 17,289 dialogs in the seven domains which include restaurants, food ordering, movies, hotels, flights, music and sports. Unlike Taskmaster-1, which includes both written "self-dialogs" and spoken two-person dialogs, Taskmaster-2 consists entirely of spoken two-person dialogs. In addition, while Taskmaster-1 is almost exclusively task-based, Taskmaster-2 contains a good number of search- and recommendation-oriented dialogs. All dialogs in this release were created using a Wizard of Oz (WOz) methodology in which crowdsourced workers played the role of a 'user' and trained call center operators played the role of the 'assistant'. In this way, users were led to believe they were interacting with an automated system that “spoke” using text-to-speech (TTS) even though it was in fact a human behind the scenes. As a result, users could express themselves however they chose in the context of an automated interface.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3276

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



## sports


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:taskmaster2/sports')
```

*   **Description**:

```
Taskmaster is dataset for goal oriented conversationas. The Taskmaster-2 dataset consists of 17,289 dialogs in the seven domains which include restaurants, food ordering, movies, hotels, flights, music and sports. Unlike Taskmaster-1, which includes both written "self-dialogs" and spoken two-person dialogs, Taskmaster-2 consists entirely of spoken two-person dialogs. In addition, while Taskmaster-1 is almost exclusively task-based, Taskmaster-2 contains a good number of search- and recommendation-oriented dialogs. All dialogs in this release were created using a Wizard of Oz (WOz) methodology in which crowdsourced workers played the role of a 'user' and trained call center operators played the role of the 'assistant'. In this way, users were led to believe they were interacting with an automated system that “spoke” using text-to-speech (TTS) even though it was in fact a human behind the scenes. As a result, users could express themselves however they chose in the context of an automated interface.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3481

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


