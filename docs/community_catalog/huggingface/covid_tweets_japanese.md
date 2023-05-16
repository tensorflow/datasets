# covid_tweets_japanese

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/covid_tweets_japanese)
*   [Huggingface](https://huggingface.co/datasets/covid_tweets_japanese)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covid_tweets_japanese')
```

*   **Description**:

```
53,640 Japanese tweets with annotation if a tweet is related to COVID-19 or not. The annotation is by majority decision by 5 - 10 crowd workers. Target tweets include "COVID" or "コロナ". The period of the tweets is from around January 2020 to around June 2020. The original tweets are not contained. Please use Twitter API to get them, for example.
```

*   **License**: CC-BY-ND 4.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 53639

*   **Features**:

```json
{
    "tweet_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "assessment_option_id": {
        "num_classes": 6,
        "names": [
            "63",
            "64",
            "65",
            "66",
            "67",
            "68"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


