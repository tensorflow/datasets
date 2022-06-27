# qasc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/qasc)
*   [Huggingface](https://huggingface.co/datasets/qasc)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qasc')
```

*   **Description**:

```
QASC is a question-answering dataset with a focus on sentence composition. It consists of 9,980 8-way multiple-choice 
questions about grade school science (8,134 train, 926 dev, 920 test), and comes with a corpus of 17M sentences.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 920
`'train'` | 8134
`'validation'` | 926

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
    "fact2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "combinedfact": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "formatted_question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


