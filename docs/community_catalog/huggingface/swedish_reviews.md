# swedish_reviews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/swedish_reviews)
*   [Huggingface](https://huggingface.co/datasets/swedish_reviews)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swedish_reviews/plain_text')
```

*   **Description**:

```
Swedish reviews scarped from various public available websites
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 20697
`'train'` | 62089
`'validation'` | 20696

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
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


