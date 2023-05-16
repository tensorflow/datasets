# yahoo_answers_topics

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/yahoo_answers_topics)
*   [Huggingface](https://huggingface.co/datasets/yahoo_answers_topics)


## yahoo_answers_topics


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:yahoo_answers_topics/yahoo_answers_topics')
```

*   **Description**:

```
Yahoo! Answers Topic Classification is text classification dataset. The dataset is the Yahoo! Answers corpus as of 10/25/2007. The Yahoo! Answers topic classification dataset is constructed using 10 largest main categories. From all the answers and other meta-information, this dataset only used the best answer content and the main category information.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 60000
`'train'` | 1400000

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "topic": {
        "num_classes": 10,
        "names": [
            "Society & Culture",
            "Science & Mathematics",
            "Health",
            "Education & Reference",
            "Computers & Internet",
            "Sports",
            "Business & Finance",
            "Entertainment & Music",
            "Family & Relationships",
            "Politics & Government"
        ],
        "id": null,
        "_type": "ClassLabel"
    },
    "question_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "best_answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


