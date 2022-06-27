# re_dial

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/re_dial)
*   [Huggingface](https://huggingface.co/datasets/re_dial)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:re_dial')
```

*   **Description**:

```
ReDial (Recommendation Dialogues) is an annotated dataset of dialogues, where users
recommend movies to each other. The dataset was collected by a team of researchers working at
Polytechnique Montréal, MILA – Quebec AI Institute, Microsoft Research Montréal, HEC Montreal, and Element AI.

The dataset allows research at the intersection of goal-directed dialogue systems
(such as restaurant recommendation) and free-form (also called “chit-chat”) dialogue systems.
```

*   **License**: CC BY 4.0 License.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1342
`'train'` | 10006

*   **Features**:

```json
{
    "movieMentions": [
        {
            "movieId": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "movieName": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "respondentQuestions": [
        {
            "movieId": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "suggested": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "seen": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "liked": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "messages": [
        {
            "timeOffset": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "senderWorkerId": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "messageId": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "conversationId": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "respondentWorkerId": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "initiatorWorkerId": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "initiatorQuestions": [
        {
            "movieId": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "suggested": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "seen": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "liked": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```


