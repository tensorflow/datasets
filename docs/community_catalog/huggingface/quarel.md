# quarel

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/quarel)
*   [Huggingface](https://huggingface.co/datasets/quarel)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:quarel')
```

*   **Description**:

```
QuaRel is a crowdsourced dataset of 2771 multiple-choice story questions, including their logical forms.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 552
`'train'` | 1941
`'validation'` | 278

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "logical_forms": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "logical_form_pretty": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "world_literals": {
        "feature": {
            "world1": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "world2": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


