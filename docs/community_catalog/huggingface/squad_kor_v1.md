# squad_kor_v1

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/squad_kor_v1)
*   [Huggingface](https://huggingface.co/datasets/squad_kor_v1)


## squad_kor_v1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_kor_v1/squad_kor_v1')
```

*   **Description**:

```
KorQuAD 1.0 is a large-scale Korean dataset for machine reading comprehension task consisting of human generated questions for Wikipedia articles. We benchmark the data collecting process of SQuADv1.0 and crowdsourced 70,000+ question-answer pairs. 1,637 articles and 70,079 pairs of question answers were collected. 1,420 articles are used for the training set, 140 for the dev set, and 77 for the test set. 60,407 question-answer pairs are for the training set, 5,774 for the dev set, and 3,898 for the test set.
```

*   **License**: CC BY-ND 2.0 KR
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 60407
`'validation'` | 5774

*   **Features**:

```json
{
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
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


