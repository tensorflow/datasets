# openbookqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/openbookqa)
*   [Huggingface](https://huggingface.co/datasets/openbookqa)


## main


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:openbookqa/main')
```

*   **Description**:

```
OpenBookQA aims to promote research in advanced question-answering, probing a deeper understanding of both the topic
(with salient facts summarized as an open book, also provided with the dataset) and the language it is expressed in. In
particular, it contains questions that require multi-step reasoning, use of additional common and commonsense knowledge,
and rich text comprehension.
OpenBookQA is a new kind of question-answering dataset modeled after open book exams for assessing human understanding
of a subject.
```

*   **License**: No known license
*   **Version**: 1.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 4957
`'validation'` | 500

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_stem": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choices": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "label": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## additional


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:openbookqa/additional')
```

*   **Description**:

```
OpenBookQA aims to promote research in advanced question-answering, probing a deeper understanding of both the topic
(with salient facts summarized as an open book, also provided with the dataset) and the language it is expressed in. In
particular, it contains questions that require multi-step reasoning, use of additional common and commonsense knowledge,
and rich text comprehension.
OpenBookQA is a new kind of question-answering dataset modeled after open book exams for assessing human understanding
of a subject.
```

*   **License**: No known license
*   **Version**: 1.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 4957
`'validation'` | 500

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_stem": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choices": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "label": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fact1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "humanScore": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "clarity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "turkIdAnonymized": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


