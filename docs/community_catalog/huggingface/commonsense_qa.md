# commonsense_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/commonsense_qa)
*   [Huggingface](https://huggingface.co/datasets/commonsense_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:commonsense_qa')
```

*   **Description**:

```
CommonsenseQA is a new multiple-choice question answering dataset that requires different types of commonsense knowledge
to predict the correct answers . It contains 12,102 questions with one correct answer and four distractor answers.
The dataset is provided in two major training/validation/testing set splits: "Random split" which is the main evaluation
split, and "Question token split", see paper for details.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1140
`'train'` | 9741
`'validation'` | 1221

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_concept": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choices": {
        "feature": {
            "label": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
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


