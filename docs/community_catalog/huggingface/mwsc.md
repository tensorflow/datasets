# mwsc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mwsc)
*   [Huggingface](https://huggingface.co/datasets/mwsc)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mwsc')
```

*   **Description**:

```
Examples taken from the Winograd Schema Challenge modified to ensure that answers are a single word from the context.
This modified Winograd Schema Challenge (MWSC) ensures that scores are neither inflated nor deflated by oddities in phrasing.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 100
`'train'` | 80
`'validation'` | 82

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


