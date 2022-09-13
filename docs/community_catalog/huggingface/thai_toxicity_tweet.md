# thai_toxicity_tweet

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/thai_toxicity_tweet)
*   [Huggingface](https://huggingface.co/datasets/thai_toxicity_tweet)


## thai_toxicity_tweet


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:thai_toxicity_tweet/thai_toxicity_tweet')
```

*   **Description**:

```
Thai Toxicity Tweet Corpus contains 3,300 tweets annotated by humans with guidelines including a 44-word dictionary.
The author obtained 2,027 and 1,273 toxic and non-toxic tweets, respectively; these were labeled by three annotators. The result of corpus
analysis indicates that tweets that include toxic words are not always toxic. Further, it is more likely that a tweet is toxic, if it contains
toxic words indicating their original meaning. Moreover, disagreements in annotation are primarily because of sarcasm, unclear existing
target, and word sense ambiguity.

Notes from data cleaner: The data is included into [huggingface/datasets](https://www.github.com/huggingface/datasets) in Dec 2020.
By this time, 506 of the tweets are not available publicly anymore. We denote these by `TWEET_NOT_FOUND` in `tweet_text`. 
Processing can be found at [this PR](https://github.com/tmu-nlp/ThaiToxicityTweetCorpus/pull/1).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3300

*   **Features**:

```json
{
    "tweet_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tweet_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "toxic_votes": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "nontoxic_votes": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "is_toxic": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


