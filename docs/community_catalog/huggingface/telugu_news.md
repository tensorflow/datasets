# telugu_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/telugu_news)
*   [Huggingface](https://huggingface.co/datasets/telugu_news)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:telugu_news')
```

*   **Description**:

```
This dataset contains Telugu language news articles along with respective
topic labels (business, editorial, entertainment, nation, sport) extracted from
the daily Andhra Jyoti. This dataset could be used to build Classification and Language Models.
```

*   **License**: Data files © Original Authors
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4329
`'train'` | 17312

*   **Features**:

```json
{
    "sno": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "heading": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic": {
        "num_classes": 5,
        "names": [
            "business",
            "editorial",
            "entertainment",
            "nation",
            "sports"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


