# muchocine

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/muchocine)
*   [Huggingface](https://huggingface.co/datasets/muchocine)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:muchocine')
```

*   **Description**:

```
The Muchocine reviews dataset contains 3,872 longform movie reviews in Spanish language,
each with a shorter summary review, and a rating on a 1-5 scale.
```

*   **License**: CC-BY-2.1
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3872

*   **Features**:

```json
{
    "review_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "star_rating": {
        "num_classes": 5,
        "names": [
            "1",
            "2",
            "3",
            "4",
            "5"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


