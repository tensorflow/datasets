# wongnai_reviews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wongnai_reviews)
*   [Huggingface](https://huggingface.co/datasets/wongnai_reviews)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wongnai_reviews')
```

*   **Description**:

```
Wongnai's review dataset contains restaurant reviews and ratings, mainly in Thai language.
The reviews are in 5 classes ranging from 1 to 5 stars.
```

*   **License**: LGPL-3.0
*   **Version**: 1.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6203
`'train'` | 40000

*   **Features**:

```json
{
    "review_body": {
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


