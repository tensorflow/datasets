# ms_marco

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ms_marco)
*   [Huggingface](https://huggingface.co/datasets/ms_marco)


## v1.1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ms_marco/v1.1')
```

*   **Description**:

```
Starting with a paper released at NIPS 2016, MS MARCO is a collection of datasets focused on deep learning in search.

The first dataset was a question answering dataset featuring 100,000 real Bing questions and a human generated answer. 
Since then we released a 1,000,000 question dataset, a natural langauge generation dataset, a passage ranking dataset, 
keyphrase extraction dataset, crawling dataset, and a conversational search.

There have been 277 submissions. 20 KeyPhrase Extraction submissions, 87 passage ranking submissions, 0 document ranking 
submissions, 73 QnA V2 submissions, 82 NLGEN submisions, and 15 QnA V1 submissions

This data comes in three tasks/forms: Original QnA dataset(v1.1), Question Answering(v2.1), Natural Language Generation(v2.1). 

The original question answering datset featured 100,000 examples and was released in 2016. Leaderboard is now closed but data is availible below.

The current competitive tasks are Question Answering and Natural Language Generation. Question Answering features over 1,000,000 queries and 
is much like the original QnA dataset but bigger and with higher quality. The Natural Language Generation dataset features 180,000 examples and 
builds upon the QnA dataset to deliver answers that could be spoken by a smart speaker.


version v1.1
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9650
`'train'` | 82326
`'validation'` | 10047

*   **Features**:

```json
{
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "passages": {
        "feature": {
            "is_selected": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "passage_text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "query_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "wellFormedAnswers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## v2.1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ms_marco/v2.1')
```

*   **Description**:

```
Starting with a paper released at NIPS 2016, MS MARCO is a collection of datasets focused on deep learning in search.

The first dataset was a question answering dataset featuring 100,000 real Bing questions and a human generated answer. 
Since then we released a 1,000,000 question dataset, a natural langauge generation dataset, a passage ranking dataset, 
keyphrase extraction dataset, crawling dataset, and a conversational search.

There have been 277 submissions. 20 KeyPhrase Extraction submissions, 87 passage ranking submissions, 0 document ranking 
submissions, 73 QnA V2 submissions, 82 NLGEN submisions, and 15 QnA V1 submissions

This data comes in three tasks/forms: Original QnA dataset(v1.1), Question Answering(v2.1), Natural Language Generation(v2.1). 

The original question answering datset featured 100,000 examples and was released in 2016. Leaderboard is now closed but data is availible below.

The current competitive tasks are Question Answering and Natural Language Generation. Question Answering features over 1,000,000 queries and 
is much like the original QnA dataset but bigger and with higher quality. The Natural Language Generation dataset features 180,000 examples and 
builds upon the QnA dataset to deliver answers that could be spoken by a smart speaker.


version v2.1
```

*   **License**: No known license
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 101092
`'train'` | 808731
`'validation'` | 101093

*   **Features**:

```json
{
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "passages": {
        "feature": {
            "is_selected": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "passage_text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "query_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "wellFormedAnswers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


