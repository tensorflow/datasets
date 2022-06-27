# ecthr_cases

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ecthr_cases)
*   [Huggingface](https://huggingface.co/datasets/ecthr_cases)


## alleged-violation-prediction


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ecthr_cases/alleged-violation-prediction')
```

*   **Description**:

```
The ECtHR Cases dataset is designed for experimentation of neural judgment prediction and rationale extraction considering ECtHR cases.
```

*   **License**: CC BY-NC-SA (Creative Commons / Attribution-NonCommercial-ShareAlike)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 9000
`'validation'` | 1000

*   **Features**:

```json
{
    "facts": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "labels": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "silver_rationales": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "gold_rationales": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## violation-prediction


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ecthr_cases/violation-prediction')
```

*   **Description**:

```
The ECtHR Cases dataset is designed for experimentation of neural judgment prediction and rationale extraction considering ECtHR cases.
```

*   **License**: CC BY-NC-SA (Creative Commons / Attribution-NonCommercial-ShareAlike)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 9000
`'validation'` | 1000

*   **Features**:

```json
{
    "facts": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "labels": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "silver_rationales": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


