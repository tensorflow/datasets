# ar_res_reviews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ar_res_reviews)
*   [Huggingface](https://huggingface.co/datasets/ar_res_reviews)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ar_res_reviews')
```

*   **Description**:

```
Dataset of 8364 restaurant reviews scrapped from qaym.com in Arabic for sentiment analysis
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8364

*   **Features**:

```json
{
    "polarity": {
        "num_classes": 2,
        "names": [
            "negative",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "restaurant_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "user_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


