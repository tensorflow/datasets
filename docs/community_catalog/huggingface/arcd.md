# arcd

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/arcd)
*   [Huggingface](https://huggingface.co/datasets/arcd)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:arcd/plain_text')
```

*   **Description**:

```
Arabic Reading Comprehension Dataset (ARCD) composed of 1,395 questions      posed by crowdworkers on Wikipedia articles.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 693
`'validation'` | 702

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


