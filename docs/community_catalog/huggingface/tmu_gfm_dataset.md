# tmu_gfm_dataset

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tmu_gfm_dataset)
*   [Huggingface](https://huggingface.co/datasets/tmu_gfm_dataset)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tmu_gfm_dataset')
```

*   **Description**:

```
A dataset for GEC metrics with manual evaluations of grammaticality, fluency, and meaning preservation for system outputs. More detail about the creation of the dataset can be found in Yoshimura et al. (2020).
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4221

*   **Features**:

```json
{
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "grammer": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "fluency": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "meaning": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "system": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ave_g": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "ave_f": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "ave_m": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


