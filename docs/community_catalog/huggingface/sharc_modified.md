# sharc_modified

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sharc_modified)
*   [Huggingface](https://huggingface.co/datasets/sharc_modified)


## mod


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sharc_modified/mod')
```

*   **Description**:

```
ShARC, a conversational QA task, requires a system to answer user questions based on rules expressed in natural language text. However, it is found that in the ShARC dataset there are multiple spurious patterns that could be exploited by neural models. SharcModified is a new dataset which reduces the patterns identified in the original dataset. To reduce the sensitivity of neural models, for each occurence of an instance conforming to any of the patterns, we automatically construct alternatives where we choose to either replace the current instance with an alternative instance which does not exhibit the pattern; or retain the original instance. The modified ShARC has two versions sharc-mod and history-shuffled. For morre details refer to Appendix A.3 .
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 21890
`'validation'` | 2270

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "snippet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "scenario": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "history": [
        {
            "follow_up_question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "follow_up_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "evidence": [
        {
            "follow_up_question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "follow_up_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## mod_dev_multi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sharc_modified/mod_dev_multi')
```

*   **Description**:

```
ShARC, a conversational QA task, requires a system to answer user questions based on rules expressed in natural language text. However, it is found that in the ShARC dataset there are multiple spurious patterns that could be exploited by neural models. SharcModified is a new dataset which reduces the patterns identified in the original dataset. To reduce the sensitivity of neural models, for each occurence of an instance conforming to any of the patterns, we automatically construct alternatives where we choose to either replace the current instance with an alternative instance which does not exhibit the pattern; or retain the original instance. The modified ShARC has two versions sharc-mod and history-shuffled. For morre details refer to Appendix A.3 .
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 2270

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "snippet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "scenario": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "history": [
        {
            "follow_up_question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "follow_up_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "evidence": [
        {
            "follow_up_question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "follow_up_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "all_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## history


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sharc_modified/history')
```

*   **Description**:

```
ShARC, a conversational QA task, requires a system to answer user questions based on rules expressed in natural language text. However, it is found that in the ShARC dataset there are multiple spurious patterns that could be exploited by neural models. SharcModified is a new dataset which reduces the patterns identified in the original dataset. To reduce the sensitivity of neural models, for each occurence of an instance conforming to any of the patterns, we automatically construct alternatives where we choose to either replace the current instance with an alternative instance which does not exhibit the pattern; or retain the original instance. The modified ShARC has two versions sharc-mod and history-shuffled. For morre details refer to Appendix A.3 .
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 21890
`'validation'` | 2270

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "snippet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "scenario": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "history": [
        {
            "follow_up_question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "follow_up_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "evidence": [
        {
            "follow_up_question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "follow_up_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## history_dev_multi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sharc_modified/history_dev_multi')
```

*   **Description**:

```
ShARC, a conversational QA task, requires a system to answer user questions based on rules expressed in natural language text. However, it is found that in the ShARC dataset there are multiple spurious patterns that could be exploited by neural models. SharcModified is a new dataset which reduces the patterns identified in the original dataset. To reduce the sensitivity of neural models, for each occurence of an instance conforming to any of the patterns, we automatically construct alternatives where we choose to either replace the current instance with an alternative instance which does not exhibit the pattern; or retain the original instance. The modified ShARC has two versions sharc-mod and history-shuffled. For morre details refer to Appendix A.3 .
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 2270

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "snippet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "scenario": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "history": [
        {
            "follow_up_question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "follow_up_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "evidence": [
        {
            "follow_up_question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "follow_up_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "all_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


