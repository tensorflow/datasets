# turkish_product_reviews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/turkish_product_reviews)
*   [Huggingface](https://huggingface.co/datasets/turkish_product_reviews)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:turkish_product_reviews')
```

*   **Description**:

```
Turkish Product Reviews.
This repository contains 235.165 product reviews collected online. There are 220.284 positive, 14881 negative reviews.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 235165

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentiment": {
        "num_classes": 2,
        "names": [
            "negative",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


