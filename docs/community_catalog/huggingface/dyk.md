# dyk

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/dyk)
*   [Huggingface](https://huggingface.co/datasets/dyk)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:dyk')
```

*   **Description**:

```
The Did You Know (pol. Czy wiesz?) dataset consists of human-annotated question-answer pairs. The task is to predict if the answer is correct. We chose the negatives which have the largest token overlap with a question.
```

*   **License**: CC BY-SA 3.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1029
`'train'` | 4154

*   **Features**:

```json
{
    "q_id": {
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
    "target": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


