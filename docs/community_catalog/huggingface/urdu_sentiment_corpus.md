# urdu_sentiment_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/urdu_sentiment_corpus)
*   [Huggingface](https://huggingface.co/datasets/urdu_sentiment_corpus)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:urdu_sentiment_corpus')
```

*   **Description**:

```
“Urdu Sentiment Corpus” (USC) shares the dat of Urdu tweets for the sentiment analysis and polarity detection.
The dataset is consisting of tweets and overall, the dataset is comprising over 17, 185 tokens
with 52% records as positive, and 48 % records as negative.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1000

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentiment": {
        "num_classes": 3,
        "names": [
            "P",
            "N",
            "O"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


