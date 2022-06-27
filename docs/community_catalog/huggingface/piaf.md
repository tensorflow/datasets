# piaf

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/piaf)
*   [Huggingface](https://huggingface.co/datasets/piaf)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:piaf/plain_text')
```

*   **Description**:

```
Piaf is a reading comprehension dataset. This version, published in February 2020, contains 3835 questions on French Wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3835

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
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


