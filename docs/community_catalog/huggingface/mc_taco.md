# mc_taco

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mc_taco)
*   [Huggingface](https://huggingface.co/datasets/mc_taco)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mc_taco/plain_text')
```

*   **Description**:

```
MC-TACO (Multiple Choice TemporAl COmmonsense) is a dataset of 13k question-answer
pairs that require temporal commonsense comprehension. A system receives a sentence
providing context information, a question designed to require temporal commonsense
knowledge, and multiple candidate answers. More than one candidate answer can be plausible.

The task is framed as binary classification: givent he context, the question,
and the candidate answer, the task is to determine whether the candidate
answer is plausible ("yes") or not ("no").
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9442
`'validation'` | 3783

*   **Features**:

```json
{
    "sentence": {
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
    "label": {
        "num_classes": 2,
        "names": [
            "no",
            "yes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "category": {
        "num_classes": 5,
        "names": [
            "Event Duration",
            "Event Ordering",
            "Frequency",
            "Typical Time",
            "Stationarity"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


