# hellaswag

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hellaswag)
*   [Huggingface](https://huggingface.co/datasets/hellaswag)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hellaswag')
```

*   **Description**:

```

```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10003
`'train'` | 39905
`'validation'` | 10042

*   **Features**:

```json
{
    "ind": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "activity_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ctx_a": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ctx_b": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ctx": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "endings": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "source_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "split_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


