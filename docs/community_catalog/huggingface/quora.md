# quora

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/quora)
*   [Huggingface](https://huggingface.co/datasets/quora)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:quora')
```

*   **Description**:

```
The Quora dataset is composed of question pairs, and the task is to determine if the questions are paraphrases of each other (have the same meaning).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 404290

*   **Features**:

```json
{
    "questions": {
        "feature": {
            "id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "is_duplicate": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    }
}
```


