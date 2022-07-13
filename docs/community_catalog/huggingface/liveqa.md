# liveqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/liveqa)
*   [Huggingface](https://huggingface.co/datasets/liveqa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:liveqa')
```

*   **Description**:

```
This is LiveQA, a Chinese dataset constructed from play-by-play live broadcast.
It contains 117k multiple-choice questions written by human commentators for over 1,670 NBA games,
which are collected from the Chinese Hupu website.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1670

*   **Features**:

```json
{
    "id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "passages": {
        "feature": {
            "is_question": {
                "dtype": "bool",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "candidate1": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "candidate2": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer": {
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


