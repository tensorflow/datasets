# movie_rationales

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/movie_rationales)
*   [Huggingface](https://huggingface.co/datasets/movie_rationales)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:movie_rationales')
```

*   **Description**:

```
The movie rationale dataset contains human annotated rationales for movie
reviews.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 199
`'train'` | 1600
`'validation'` | 200

*   **Features**:

```json
{
    "review": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "NEG",
            "POS"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "evidences": {
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


