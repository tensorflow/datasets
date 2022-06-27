# tweets_ar_en_parallel

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tweets_ar_en_parallel)
*   [Huggingface](https://huggingface.co/datasets/tweets_ar_en_parallel)


## parallelTweets


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweets_ar_en_parallel/parallelTweets')
```

*   **Description**:

```
Twitter users often post parallel tweets—tweets that contain the same content but are
    written in different languages. Parallel tweets can be an important resource for developing
    machine translation (MT) systems among other natural language processing (NLP) tasks. This
    resource is a result of a generic method for collecting parallel tweets. Using the method,
    we compiled a bilingual corpus of English-Arabic parallel tweets and a list of Twitter accounts
    who post English-Arabic tweets regularly. Additionally, we annotate a subset of Twitter accounts
    with their countries of origin and topic of interest, which provides insights about the population
    who post parallel tweets.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 166706

*   **Features**:

```json
{
    "ArabicTweetID": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "EnglishTweetID": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    }
}
```



## accountList


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweets_ar_en_parallel/accountList')
```

*   **Description**:

```
Twitter users often post parallel tweets—tweets that contain the same content but are
    written in different languages. Parallel tweets can be an important resource for developing
    machine translation (MT) systems among other natural language processing (NLP) tasks. This
    resource is a result of a generic method for collecting parallel tweets. Using the method,
    we compiled a bilingual corpus of English-Arabic parallel tweets and a list of Twitter accounts
    who post English-Arabic tweets regularly. Additionally, we annotate a subset of Twitter accounts
    with their countries of origin and topic of interest, which provides insights about the population
    who post parallel tweets.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1389

*   **Features**:

```json
{
    "account": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## countryTopicAnnotation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweets_ar_en_parallel/countryTopicAnnotation')
```

*   **Description**:

```
Twitter users often post parallel tweets—tweets that contain the same content but are
    written in different languages. Parallel tweets can be an important resource for developing
    machine translation (MT) systems among other natural language processing (NLP) tasks. This
    resource is a result of a generic method for collecting parallel tweets. Using the method,
    we compiled a bilingual corpus of English-Arabic parallel tweets and a list of Twitter accounts
    who post English-Arabic tweets regularly. Additionally, we annotate a subset of Twitter accounts
    with their countries of origin and topic of interest, which provides insights about the population
    who post parallel tweets.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200

*   **Features**:

```json
{
    "account": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "country": {
        "num_classes": 12,
        "names": [
            "QA",
            "BH",
            "AE",
            "OM",
            "SA",
            "PL",
            "JO",
            "IQ",
            "Other",
            "EG",
            "KW",
            "SY"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "topic": {
        "num_classes": 12,
        "names": [
            "Gov",
            "Culture",
            "Education",
            "Sports",
            "Travel",
            "Events",
            "Business",
            "Science",
            "Politics",
            "Health",
            "Governoment",
            "Media"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


