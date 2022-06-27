# dream

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/dream)
*   [Huggingface](https://huggingface.co/datasets/dream)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:dream/plain_text')
```

*   **Description**:

```
DREAM is a multiple-choice Dialogue-based REAding comprehension exaMination dataset. In contrast to existing reading comprehension datasets, DREAM is the first to focus on in-depth multi-turn multi-party dialogue understanding.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2041
`'train'` | 6116
`'validation'` | 2040

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dialogue_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dialogue": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice": {
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


