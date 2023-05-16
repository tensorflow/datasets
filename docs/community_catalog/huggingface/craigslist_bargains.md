# craigslist_bargains

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/craigslist_bargains)
*   [Huggingface](https://huggingface.co/datasets/craigslist_bargains)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:craigslist_bargains')
```

*   **Description**:

```
We study negotiation dialogues where two agents, a buyer and a seller,
negotiate over the price of an time for sale. We collected a dataset of more
than 6K negotiation dialogues over multiple categories of products scraped from Craigslist.
Our goal is to develop an agent that negotiates with humans through such conversations.
The challenge is to handle both the negotiation strategy and the rich language for bargaining.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 838
`'train'` | 5247
`'validation'` | 597

*   **Features**:

```json
{
    "agent_info": {
        "feature": {
            "Bottomline": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Role": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Target": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "agent_turn": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "dialogue_acts": {
        "feature": {
            "intent": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "price": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "utterance": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "items": {
        "feature": {
            "Category": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Images": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Price": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "Description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


