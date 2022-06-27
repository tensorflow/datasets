# humicroedit

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/humicroedit)
*   [Huggingface](https://huggingface.co/datasets/humicroedit)


## subtask-1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:humicroedit/subtask-1')
```

*   **Description**:

```
This new dataset is designed to assess the funniness of edited news headlines.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'funlines'` | 8248
`'test'` | 3024
`'train'` | 9652
`'validation'` | 2419

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edit": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "grades": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meanGrade": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## subtask-2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:humicroedit/subtask-2')
```

*   **Description**:

```
This new dataset is designed to assess the funniness of edited news headlines.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'funlines'` | 1958
`'test'` | 2960
`'train'` | 9381
`'validation'` | 2355

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edit1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "grades1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meanGrade1": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "original2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edit2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "grades2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meanGrade2": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "equal",
            "sentence1",
            "sentence2"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


