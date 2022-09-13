# deal_or_no_dialog

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/deal_or_no_dialog)
*   [Huggingface](https://huggingface.co/datasets/deal_or_no_dialog)


## dialogues


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:deal_or_no_dialog/dialogues')
```

*   **Description**:

```
A large dataset of human-human negotiations on a multi-issue bargaining task, where agents who cannot observe each other’s reward functions must reach anagreement (o a deal) via natural language dialogue.
```

*   **License**: The project is licenced under CC-by-NC
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1052
`'train'` | 10095
`'validation'` | 1087

*   **Features**:

```json
{
    "input": {
        "feature": {
            "count": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "value": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "dialogue": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "partner_input": {
        "feature": {
            "count": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "value": {
                "dtype": "int32",
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



## self_play


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:deal_or_no_dialog/self_play')
```

*   **Description**:

```
A large dataset of human-human negotiations on a multi-issue bargaining task, where agents who cannot observe each other’s reward functions must reach anagreement (o a deal) via natural language dialogue.
```

*   **License**: The project is licenced under CC-by-NC
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8172

*   **Features**:

```json
{
    "input": {
        "feature": {
            "count": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "value": {
                "dtype": "int32",
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


