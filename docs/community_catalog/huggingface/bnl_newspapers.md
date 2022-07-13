# bnl_newspapers

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bnl_newspapers)
*   [Huggingface](https://huggingface.co/datasets/bnl_newspapers)


## processed


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bnl_newspapers/processed')
```

*   **Description**:

```
Digitised historic newspapers from the Bibliothèque nationale (BnL) - the National Library of Luxembourg.
```

*   **License**: CC0
*   **Version**: 1.17.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 537558

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ispartof": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pub_date": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "publisher": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article_type": {
        "num_classes": 18,
        "names": [
            "ADVERTISEMENT_SECTION",
            "BIBLIOGRAPHY",
            "CHAPTER",
            "INDEX",
            "CONTRIBUTION",
            "TABLE_OF_CONTENTS",
            "WEATHER",
            "SHIPPING",
            "SECTION",
            "ARTICLE",
            "TITLE_SECTION",
            "DEATH_NOTICE",
            "SUPPLEMENT",
            "TABLE",
            "ADVERTISEMENT",
            "CHART_DIAGRAM",
            "ILLUSTRATION",
            "ISSUE"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "extent": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


