# dutch_social

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/dutch_social)
*   [Huggingface](https://huggingface.co/datasets/dutch_social)


## dutch_social


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:dutch_social/dutch_social')
```

*   **Description**:

```
The dataset contains around 271,342 tweets. The tweets are filtered via the official Twitter API to
contain tweets in Dutch language or by users who have specified their location information within Netherlands
geographical boundaries. Using natural language processing we have classified the tweets for their HISCO codes.
If the user has provided their location within Dutch boundaries, we have also classified them to their respective
provinces The objective of this dataset is to make research data available publicly in a FAIR (Findable, Accessible,
Interoperable, Reusable) way. Twitter's Terms of Service Licensed under Attribution-NonCommercial 4.0 International
(CC BY-NC 4.0) (2020-10-27)
```

*   **License**: CC BY-NC 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 54268
`'train'` | 162805
`'validation'` | 54269

*   **Features**:

```json
{
    "full_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text_translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "screen_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "desc_translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "location": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "weekofyear": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "weekday": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "month": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "day": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "point_info": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "point": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "latitude": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    },
    "longitude": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    },
    "altitude": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    },
    "province": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hisco_standard": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hisco_code": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "industry": {
        "dtype": "bool_",
        "id": null,
        "_type": "Value"
    },
    "sentiment_pattern": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    },
    "subjective_pattern": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "neg",
            "neu",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


