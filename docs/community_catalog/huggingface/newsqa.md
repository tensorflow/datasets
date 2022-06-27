# newsqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/newsqa)
*   [Huggingface](https://huggingface.co/datasets/newsqa)


## combined-csv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:newsqa/combined-csv')
```

*   **Description**:

```
NewsQA is a challenging machine comprehension dataset of over 100,000 human-generated question-answer pairs. Crowdworkers supply questions and answers based on a set of over 10,000 news articles from CNN, with answers consisting of spans of text from the corresponding articles.
```

*   **License**: NewsQA CodeCopyright (c) Microsoft Corporation All rights reserved. MIT License 
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 119633

*   **Features**:

```json
{
    "story_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "story_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_char_ranges": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## combined-json


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:newsqa/combined-json')
```

*   **Description**:

```
NewsQA is a challenging machine comprehension dataset of over 100,000 human-generated question-answer pairs. Crowdworkers supply questions and answers based on a set of over 10,000 news articles from CNN, with answers consisting of spans of text from the corresponding articles.
```

*   **License**: NewsQA CodeCopyright (c) Microsoft Corporation All rights reserved. MIT License 
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 12744

*   **Features**:

```json
{
    "storyId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "questions": {
        "feature": {
            "q": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "isAnswerAbsent": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "isQuestionBad": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "consensus": {
                "s": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "e": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "badQuestion": {
                    "dtype": "bool",
                    "id": null,
                    "_type": "Value"
                },
                "noAnswer": {
                    "dtype": "bool",
                    "id": null,
                    "_type": "Value"
                }
            },
            "answers": {
                "feature": {
                    "sourcerAnswers": {
                        "feature": {
                            "s": {
                                "dtype": "int32",
                                "id": null,
                                "_type": "Value"
                            },
                            "e": {
                                "dtype": "int32",
                                "id": null,
                                "_type": "Value"
                            },
                            "badQuestion": {
                                "dtype": "bool",
                                "id": null,
                                "_type": "Value"
                            },
                            "noAnswer": {
                                "dtype": "bool",
                                "id": null,
                                "_type": "Value"
                            }
                        },
                        "length": -1,
                        "id": null,
                        "_type": "Sequence"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "validated_answers": {
                "feature": {
                    "s": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "e": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "badQuestion": {
                        "dtype": "bool",
                        "id": null,
                        "_type": "Value"
                    },
                    "noAnswer": {
                        "dtype": "bool",
                        "id": null,
                        "_type": "Value"
                    },
                    "count": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## split


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:newsqa/split')
```

*   **Description**:

```
NewsQA is a challenging machine comprehension dataset of over 100,000 human-generated question-answer pairs. Crowdworkers supply questions and answers based on a set of over 10,000 news articles from CNN, with answers consisting of spans of text from the corresponding articles.
```

*   **License**: NewsQA CodeCopyright (c) Microsoft Corporation All rights reserved. MIT License 
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5126
`'train'` | 92549
`'validation'` | 5166

*   **Features**:

```json
{
    "story_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "story_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_token_ranges": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


