# amazon_polarity

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/amazon_polarity)
*   [Huggingface](https://huggingface.co/datasets/amazon_polarity)


## amazon_polarity


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amazon_polarity/amazon_polarity')
```

*   **Description**:

```
The Amazon reviews dataset consists of reviews from amazon.
The data span a period of 18 years, including ~35 million reviews up to March 2013.
Reviews include product and user information, ratings, and a plaintext review.
```

*   **License**: Apache License 2.0
*   **Version**: 3.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 400000
`'train'` | 3600000

*   **Features**:

```json
{
    "label": {
        "num_classes": 2,
        "names": [
            "negative",
            "positive"
        ],
        "id": null,
        "_type": "ClassLabel"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


