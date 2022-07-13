# style_change_detection

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/style_change_detection)
*   [Huggingface](https://huggingface.co/datasets/style_change_detection)


## narrow


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:style_change_detection/narrow')
```

*   **Description**:

```
The goal of the style change detection task is to identify text positions within a given multi-author document at which the author switches. Detecting these positions is a crucial part of the authorship identification process, and for multi-author document analysis in general.

Access to the dataset needs to be requested from zenodo.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3418
`'validation'` | 1713

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "authors": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "structure": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "site": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "multi-author": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "changes": {
        "feature": {
            "dtype": "bool",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wide


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:style_change_detection/wide')
```

*   **Description**:

```
The goal of the style change detection task is to identify text positions within a given multi-author document at which the author switches. Detecting these positions is a crucial part of the authorship identification process, and for multi-author document analysis in general.

Access to the dataset needs to be requested from zenodo.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8030
`'validation'` | 4019

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "authors": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "structure": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "site": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "multi-author": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "changes": {
        "feature": {
            "dtype": "bool",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


