# hlgd

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hlgd)
*   [Huggingface](https://huggingface.co/datasets/hlgd)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hlgd')
```

*   **Description**:

```
HLGD is a binary classification dataset consisting of 20,056 labeled news headlines pairs indicating
whether the two headlines describe the same underlying world event or not.
```

*   **License**: Apache-2.0 License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2495
`'train'` | 15492
`'validation'` | 2069

*   **Features**:

```json
{
    "timeline_id": {
        "num_classes": 10,
        "names": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "headline_a": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "headline_b": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date_a": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date_b": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url_a": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url_b": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "same_event",
            "different_event"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


