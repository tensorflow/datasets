# coqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/coqa)
*   [Huggingface](https://huggingface.co/datasets/coqa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:coqa')
```

*   **Description**:

```
CoQA: A Conversational Question Answering Challenge
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7199
`'validation'` | 500

*   **Features**:

```json
{
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "story": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "questions": {
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
            "input_text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "answer_end": {
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


