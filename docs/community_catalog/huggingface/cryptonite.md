# cryptonite

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cryptonite)
*   [Huggingface](https://huggingface.co/datasets/cryptonite)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cryptonite')
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



## cryptonite


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cryptonite/cryptonite')
```

*   **Description**:

```
Cryptonite: A Cryptic Crossword Benchmark for Extreme Ambiguity in Language
Current NLP datasets targeting ambiguity can be solved by a native speaker with relative ease. We present Cryptonite, 
a large-scale dataset based on cryptic crosswords, which is both linguistically complex and naturally sourced. Each 
example in Cryptonite is a cryptic clue, a short phrase or sentence with a misleading surface reading, whose solving 
requires disambiguating semantic, syntactic, and phonetic wordplays, as well as world knowledge. Cryptic clues pose a 
challenge even for experienced solvers, though top-tier experts can solve them with almost 100% accuracy. Cryptonite 
is a challenging task for current models; fine-tuning T5-Large on 470k cryptic clues achieves only 7.6% accuracy, on 
par with the accuracy of a rule-based clue solver (8.6%).
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 26157
`'train'` | 470804
`'validation'` | 26156

*   **Features**:

```json
{
    "clue": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "enumeration": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "publisher": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "quick": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


