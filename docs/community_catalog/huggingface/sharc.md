# sharc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sharc)
*   [Huggingface](https://huggingface.co/datasets/sharc)


## sharc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sharc/sharc')
```

*   **Description**:

```
ShARC is a Conversational Question Answering dataset focussing on question answering from texts containing rules. The goal is to answer questions by possibly asking follow-up questions first. It is assumed assume that the question is often underspecified, in the sense that the question does not provide enough information to be answered directly. However, an agent can use the supporting rule text to infer what needs to be asked in order to determine the final answer.
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
    },
    "negative_question": {
        "dtype": "bool_",
        "id": null,
        "_type": "Value"
    },
    "negative_scenario": {
        "dtype": "bool_",
        "id": null,
        "_type": "Value"
    }
}
```


