# thaiqa_squad

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/thaiqa_squad)
*   [Huggingface](https://huggingface.co/datasets/thaiqa_squad)


## thaiqa_squad


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:thaiqa_squad/thaiqa_squad')
```

*   **Description**:

```
`thaiqa_squad` is an open-domain, extractive question answering dataset (4,000 questions in `train` and 74 questions in `dev`) in
[SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) format, originally created by [NECTEC](https://www.nectec.or.th/en/) from
Wikipedia articles and adapted to [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) format by [PyThaiNLP](https://github.com/PyThaiNLP/).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4000
`'validation'` | 74

*   **Features**:

```json
{
    "question_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "article_id": {
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
    "answers": {
        "feature": {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_begin_position": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "answer_end_position": {
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


