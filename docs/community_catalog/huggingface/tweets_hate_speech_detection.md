# tweets_hate_speech_detection

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tweets_hate_speech_detection)
*   [Huggingface](https://huggingface.co/datasets/tweets_hate_speech_detection)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweets_hate_speech_detection')
```

*   **Description**:

```
The objective of this task is to detect hate speech in tweets. For the sake of simplicity, we say a tweet contains hate speech if it has a racist or sexist sentiment associated with it. So, the task is to classify racist or sexist tweets from other tweets.

Formally, given a training sample of tweets and labels, where label ‘1’ denotes the tweet is racist/sexist and label ‘0’ denotes the tweet is not racist/sexist, your objective is to predict the labels on the given test dataset.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 31962

*   **Features**:

```json
{
    "label": {
        "num_classes": 2,
        "names": [
            "no-hate-speech",
            "hate-speech"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "tweet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


