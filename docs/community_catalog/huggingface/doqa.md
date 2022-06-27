# doqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/doqa)
*   [Huggingface](https://huggingface.co/datasets/doqa)


## cooking


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:doqa/cooking')
```

*   **Description**:

```
DoQA is a dataset for accessing Domain Specific FAQs via conversational QA that contains 2,437 information-seeking question/answer dialogues 
(10,917 questions in total) on three different domains: cooking, travel and movies. Note that we include in the generic concept of FAQs also 
Community Question Answering sites, as well as corporate information in intranets which is maintained in textual form similar to FAQs, often 
referred to as internal “knowledge bases”.

These dialogues are created by crowd workers that play the following two roles: the user who asks questions about a given topic posted in Stack 
Exchange (https://stackexchange.com/), and the domain expert who replies to the questions by selecting a short span of text from the long textual 
reply in the original post. The expert can rephrase the selected span, in order to make it look more natural. The dataset covers unanswerable 
questions and some relevant dialogue acts.

DoQA enables the development and evaluation of conversational QA systems that help users access the knowledge buried in domain specific FAQs.
```

*   **License**: No known license
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1797
`'train'` | 4612
`'validation'` | 911

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "background": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "followup": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "yesno": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "orig_answer": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## movies


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:doqa/movies')
```

*   **Description**:

```
DoQA is a dataset for accessing Domain Specific FAQs via conversational QA that contains 2,437 information-seeking question/answer dialogues 
(10,917 questions in total) on three different domains: cooking, travel and movies. Note that we include in the generic concept of FAQs also 
Community Question Answering sites, as well as corporate information in intranets which is maintained in textual form similar to FAQs, often 
referred to as internal “knowledge bases”.

These dialogues are created by crowd workers that play the following two roles: the user who asks questions about a given topic posted in Stack 
Exchange (https://stackexchange.com/), and the domain expert who replies to the questions by selecting a short span of text from the long textual 
reply in the original post. The expert can rephrase the selected span, in order to make it look more natural. The dataset covers unanswerable 
questions and some relevant dialogue acts.

DoQA enables the development and evaluation of conversational QA systems that help users access the knowledge buried in domain specific FAQs.
```

*   **License**: No known license
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1884

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "background": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "followup": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "yesno": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "orig_answer": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## travel


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:doqa/travel')
```

*   **Description**:

```
DoQA is a dataset for accessing Domain Specific FAQs via conversational QA that contains 2,437 information-seeking question/answer dialogues 
(10,917 questions in total) on three different domains: cooking, travel and movies. Note that we include in the generic concept of FAQs also 
Community Question Answering sites, as well as corporate information in intranets which is maintained in textual form similar to FAQs, often 
referred to as internal “knowledge bases”.

These dialogues are created by crowd workers that play the following two roles: the user who asks questions about a given topic posted in Stack 
Exchange (https://stackexchange.com/), and the domain expert who replies to the questions by selecting a short span of text from the long textual 
reply in the original post. The expert can rephrase the selected span, in order to make it look more natural. The dataset covers unanswerable 
questions and some relevant dialogue acts.

DoQA enables the development and evaluation of conversational QA systems that help users access the knowledge buried in domain specific FAQs.
```

*   **License**: No known license
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1713

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "background": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "followup": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "yesno": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "orig_answer": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


