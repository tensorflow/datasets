# arsentd_lev

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/arsentd_lev)
*   [Huggingface](https://huggingface.co/datasets/arsentd_lev)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:arsentd_lev')
```

*   **Description**:

```
The Arabic Sentiment Twitter Dataset for Levantine dialect (ArSenTD-LEV) contains 4,000 tweets written in Arabic and equally retrieved from Jordan, Lebanon, Palestine and Syria.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4000

*   **Features**:

```json
{
    "Tweet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Country": {
        "num_classes": 4,
        "names": [
            "jordan",
            "lebanon",
            "syria",
            "palestine"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Topic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Sentiment": {
        "num_classes": 5,
        "names": [
            "negative",
            "neutral",
            "positive",
            "very_negative",
            "very_positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Sentiment_Expression": {
        "num_classes": 3,
        "names": [
            "explicit",
            "implicit",
            "none"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Sentiment_Target": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


