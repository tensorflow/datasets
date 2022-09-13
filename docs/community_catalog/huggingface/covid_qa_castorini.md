# covid_qa_castorini

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/covid_qa_castorini)
*   [Huggingface](https://huggingface.co/datasets/covid_qa_castorini)


## covid_qa_deepset


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covid_qa_castorini/covid_qa_deepset')
```

*   **Description**:

```
COVID-QA is a Question Answering dataset consisting of 2,019 question/answer pairs annotated by volunteer biomedical experts on scientific articles related to COVID-19.
```

*   **License**: Apache License 2.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2019

*   **Features**:

```json
{
    "document_id": {
        "dtype": "int32",
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
    "is_impossible": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "int32",
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
    }
}
```



## covidqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covid_qa_castorini/covidqa')
```

*   **Description**:

```
CovidQA is the beginnings of a question answering dataset specifically designed for COVID-19, built by hand from knowledge gathered from Kaggle's COVID-19 Open Research Dataset Challenge.
```

*   **License**: Apache License 2.0
*   **Version**: 0.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 27

*   **Features**:

```json
{
    "category_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "keyword_query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
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
            "exact_answer": {
                "dtype": "string",
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



## covid_qa_castorini


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covid_qa_castorini/covid_qa_castorini')
```

*   **Description**:

```
CovidQA is the beginnings of a question answering dataset specifically designed for COVID-19, built by hand from knowledge gathered from Kaggle's COVID-19 Open Research Dataset Challenge.
```

*   **License**: Apache License 2.0
*   **Version**: 0.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 27

*   **Features**:

```json
{
    "category_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "keyword_query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
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
            "exact_answer": {
                "dtype": "string",
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


