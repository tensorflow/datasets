# yahoo_answers_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/yahoo_answers_qa)
*   [Huggingface](https://huggingface.co/datasets/yahoo_answers_qa)


## yahoo_answers_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:yahoo_answers_qa/yahoo_answers_qa')
```

*   **Description**:

```
Yahoo Non-Factoid Question Dataset is derived from Yahoo's Webscope L6 collection using machine learning techiques such that the questions would contain non-factoid answers.The dataset contains 87,361 questions and their corresponding answers. Each question contains its best answer along with additional other answers submitted by users. Only the best answer was reviewed in determining the quality of the question-answer pair.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 87362

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
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nbestanswers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "main_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


