# conv_ai_2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/conv_ai_2)
*   [Huggingface](https://huggingface.co/datasets/conv_ai_2)


## conv_ai_2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conv_ai_2/conv_ai_2')
```

*   **Description**:

```
ConvAI is a dataset of human-to-bot conversations labelled for quality. This data can be used to train a metric for evaluating dialogue systems. Moreover, it can be used in the development of chatbots themselves: it contains the information on the quality of utterances and entire dialogues, that can guide a dialogue system in search of better answers.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3495

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dialog_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dialog": [
        {
            "id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "sender": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "sender_class": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "bot_profile": {
        "feature": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "user_profile": {
        "feature": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "eval_score": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "profile_match": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


