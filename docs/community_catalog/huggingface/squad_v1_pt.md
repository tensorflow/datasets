# squad_v1_pt

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/squad_v1_pt)
*   [Huggingface](https://huggingface.co/datasets/squad_v1_pt)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_v1_pt')
```

*   **Description**:

```
Portuguese translation of the SQuAD dataset. The translation was performed automatically using the Google Cloud API.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 87599
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


