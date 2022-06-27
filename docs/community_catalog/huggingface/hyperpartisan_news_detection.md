# hyperpartisan_news_detection

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hyperpartisan_news_detection)
*   [Huggingface](https://huggingface.co/datasets/hyperpartisan_news_detection)


## byarticle


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hyperpartisan_news_detection/byarticle')
```

*   **Description**:

```
Hyperpartisan News Detection was a dataset created for PAN @ SemEval 2019 Task 4.
Given a news article text, decide whether it follows a hyperpartisan argumentation, i.e., whether it exhibits blind, prejudiced, or unreasoning allegiance to one party, faction, cause, or person.

There are 2 parts:
- byarticle: Labeled through crowdsourcing on an article basis. The data contains only articles for which a consensus among the crowdsourcing workers existed.
- bypublisher: Labeled by the overall bias of the publisher as provided by BuzzFeed journalists or MediaBiasFactCheck.com.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 645

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hyperpartisan": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "published_at": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## bypublisher


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hyperpartisan_news_detection/bypublisher')
```

*   **Description**:

```
Hyperpartisan News Detection was a dataset created for PAN @ SemEval 2019 Task 4.
Given a news article text, decide whether it follows a hyperpartisan argumentation, i.e., whether it exhibits blind, prejudiced, or unreasoning allegiance to one party, faction, cause, or person.

There are 2 parts:
- byarticle: Labeled through crowdsourcing on an article basis. The data contains only articles for which a consensus among the crowdsourcing workers existed.
- bypublisher: Labeled by the overall bias of the publisher as provided by BuzzFeed journalists or MediaBiasFactCheck.com.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 600000
`'validation'` | 600000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hyperpartisan": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "published_at": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bias": {
        "num_classes": 5,
        "names": [
            "right",
            "right-center",
            "least",
            "left-center",
            "left"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


