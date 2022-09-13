# squad_es

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/squad_es)
*   [Huggingface](https://huggingface.co/datasets/squad_es)


## v1.1.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_es/v1.1.0')
```

*   **Description**:

```
automatic translation of the Stanford Question Answering Dataset (SQuAD) v2 into Spanish
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 87595
`'validation'` | 10570

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


