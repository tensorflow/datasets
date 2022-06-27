# qa_zre

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/qa_zre)
*   [Huggingface](https://huggingface.co/datasets/qa_zre)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa_zre')
```

*   **Description**:

```
A dataset reducing relation extraction to simple reading comprehension questions
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 120000
`'train'` | 8400000
`'validation'` | 6000

*   **Features**:

```json
{
    "relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
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


