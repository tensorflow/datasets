# nsmc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/nsmc)
*   [Huggingface](https://huggingface.co/datasets/nsmc)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nsmc')
```

*   **Description**:

```
This is a movie review dataset in the Korean language. Reviews were scraped from Naver movies. The dataset construction is based on the method noted in Large movie review dataset from Maas et al., 2011.
```

*   **License**: CC0 1.0 Universal (CC0 1.0)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 50000
`'train'` | 150000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document": {
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


