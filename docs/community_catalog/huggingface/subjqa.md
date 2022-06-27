# subjqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/subjqa)
*   [Huggingface](https://huggingface.co/datasets/subjqa)


## books


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:subjqa/books')
```

*   **Description**:

```
SubjQA is a question answering dataset that focuses on subjective questions and answers.
The dataset consists of roughly 10,000 questions over reviews from 6 different domains: books, movies, grocery,
electronics, TripAdvisor (i.e. hotels), and restaurants.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 345
`'train'` | 1314
`'validation'` | 256

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "q_reviews_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_subj_level": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "ques_subj_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "is_ques_subjective": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
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
            },
            "answer_subj_level": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "ans_subj_score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "is_ans_subjective": {
                "dtype": "bool",
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



## electronics


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:subjqa/electronics')
```

*   **Description**:

```
SubjQA is a question answering dataset that focuses on subjective questions and answers.
The dataset consists of roughly 10,000 questions over reviews from 6 different domains: books, movies, grocery,
electronics, TripAdvisor (i.e. hotels), and restaurants.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 358
`'train'` | 1295
`'validation'` | 255

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "q_reviews_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_subj_level": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "ques_subj_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "is_ques_subjective": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
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
            },
            "answer_subj_level": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "ans_subj_score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "is_ans_subjective": {
                "dtype": "bool",
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



## grocery


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:subjqa/grocery')
```

*   **Description**:

```
SubjQA is a question answering dataset that focuses on subjective questions and answers.
The dataset consists of roughly 10,000 questions over reviews from 6 different domains: books, movies, grocery,
electronics, TripAdvisor (i.e. hotels), and restaurants.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 591
`'train'` | 1124
`'validation'` | 218

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "q_reviews_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_subj_level": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "ques_subj_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "is_ques_subjective": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
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
            },
            "answer_subj_level": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "ans_subj_score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "is_ans_subjective": {
                "dtype": "bool",
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
ds = tfds.load('huggingface:subjqa/movies')
```

*   **Description**:

```
SubjQA is a question answering dataset that focuses on subjective questions and answers.
The dataset consists of roughly 10,000 questions over reviews from 6 different domains: books, movies, grocery,
electronics, TripAdvisor (i.e. hotels), and restaurants.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 291
`'train'` | 1369
`'validation'` | 261

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "q_reviews_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_subj_level": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "ques_subj_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "is_ques_subjective": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
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
            },
            "answer_subj_level": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "ans_subj_score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "is_ans_subjective": {
                "dtype": "bool",
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



## restaurants


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:subjqa/restaurants')
```

*   **Description**:

```
SubjQA is a question answering dataset that focuses on subjective questions and answers.
The dataset consists of roughly 10,000 questions over reviews from 6 different domains: books, movies, grocery,
electronics, TripAdvisor (i.e. hotels), and restaurants.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 266
`'train'` | 1400
`'validation'` | 267

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "q_reviews_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_subj_level": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "ques_subj_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "is_ques_subjective": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
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
            },
            "answer_subj_level": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "ans_subj_score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "is_ans_subjective": {
                "dtype": "bool",
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



## tripadvisor


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:subjqa/tripadvisor')
```

*   **Description**:

```
SubjQA is a question answering dataset that focuses on subjective questions and answers.
The dataset consists of roughly 10,000 questions over reviews from 6 different domains: books, movies, grocery,
electronics, TripAdvisor (i.e. hotels), and restaurants.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 512
`'train'` | 1165
`'validation'` | 230

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nn_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_mod": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_asp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "q_reviews_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_subj_level": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "ques_subj_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "is_ques_subjective": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
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
            },
            "answer_subj_level": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "ans_subj_score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "is_ans_subjective": {
                "dtype": "bool",
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


