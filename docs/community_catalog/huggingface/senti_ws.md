# senti_ws

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/senti_ws)
*   [Huggingface](https://huggingface.co/datasets/senti_ws)


## pos-tagging


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:senti_ws/pos-tagging')
```

*   **Description**:

```
SentimentWortschatz, or SentiWS for short, is a publicly available German-language resource for sentiment analysis, and pos-tagging. The POS tags are ["NN", "VVINF", "ADJX", "ADV"] -> ["noun", "verb", "adjective", "adverb"], and positive and negative polarity bearing words are weighted within the interval of [-1, 1].
```

*   **License**: Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3471

*   **Features**:

```json
{
    "word": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pos-tag": {
        "num_classes": 4,
        "names": [
            "NN",
            "VVINF",
            "ADJX",
            "ADV"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## sentiment-scoring


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:senti_ws/sentiment-scoring')
```

*   **Description**:

```
SentimentWortschatz, or SentiWS for short, is a publicly available German-language resource for sentiment analysis, and pos-tagging. The POS tags are ["NN", "VVINF", "ADJX", "ADV"] -> ["noun", "verb", "adjective", "adverb"], and positive and negative polarity bearing words are weighted within the interval of [-1, 1].
```

*   **License**: Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3471

*   **Features**:

```json
{
    "word": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentiment-score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


