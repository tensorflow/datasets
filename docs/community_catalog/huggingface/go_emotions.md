# go_emotions

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/go_emotions)
*   [Huggingface](https://huggingface.co/datasets/go_emotions)


## raw


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:go_emotions/raw')
```

*   **Description**:

```
The GoEmotions dataset contains 58k carefully curated Reddit comments labeled for 27 emotion categories or Neutral.
The emotion categories are admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire,
disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness,
optimism, pride, realization, relief, remorse, sadness, surprise.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 211225

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "author": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subreddit": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "link_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "parent_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "created_utc": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "rater_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "example_very_unclear": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "admiration": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "amusement": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "anger": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "annoyance": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "approval": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "caring": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "confusion": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "curiosity": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "desire": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "disappointment": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "disapproval": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "disgust": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "embarrassment": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "excitement": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "fear": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "gratitude": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "grief": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "joy": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "love": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "nervousness": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "optimism": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "pride": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "realization": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "relief": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "remorse": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "sadness": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "surprise": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "neutral": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## simplified


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:go_emotions/simplified')
```

*   **Description**:

```
The GoEmotions dataset contains 58k carefully curated Reddit comments labeled for 27 emotion categories or Neutral.
The emotion categories are admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire,
disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness,
optimism, pride, realization, relief, remorse, sadness, surprise.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5427
`'train'` | 43410
`'validation'` | 5426

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 28,
            "names": [
                "admiration",
                "amusement",
                "anger",
                "annoyance",
                "approval",
                "caring",
                "confusion",
                "curiosity",
                "desire",
                "disappointment",
                "disapproval",
                "disgust",
                "embarrassment",
                "excitement",
                "fear",
                "gratitude",
                "grief",
                "joy",
                "love",
                "nervousness",
                "optimism",
                "pride",
                "realization",
                "relief",
                "remorse",
                "sadness",
                "surprise",
                "neutral"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


