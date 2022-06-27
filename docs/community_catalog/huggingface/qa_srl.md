# qa_srl

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/qa_srl)
*   [Huggingface](https://huggingface.co/datasets/qa_srl)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa_srl/plain_text')
```

*   **Description**:

```
The dataset contains question-answer pairs to model verbal predicate-argument structure. The questions start with wh-words (Who, What, Where, What, etc.) and contain a verb predicate in the sentence; the answers are phrases in the sentence. 
There were 2 datsets used in the paper, newswire and wikipedia. Unfortunately the newswiredataset is built from CoNLL-2009 English training set that is covered under license
Thus, we are providing only Wikipedia training set here. Please check README.md for more details on newswire dataset.
For the Wikipedia domain, randomly sampled sentences from the English Wikipedia (excluding questions and sentences with fewer than 10 or more than 60 words) were taken.
This new dataset is designed to solve this great NLP task and is crafted with a lot of care.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2201
`'train'` | 6414
`'validation'` | 2183

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sent_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "predicate_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "predicate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answers": {
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


