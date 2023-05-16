# crows_pairs

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/crows_pairs)
*   [Huggingface](https://huggingface.co/datasets/crows_pairs)


## crows_pairs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:crows_pairs/crows_pairs')
```

*   **Description**:

```
CrowS-Pairs, a challenge dataset for measuring the degree to which U.S. stereotypical biases present in the masked language models (MLMs).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1508

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "sent_more": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sent_less": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stereo_antistereo": {
        "num_classes": 2,
        "names": [
            "stereo",
            "antistereo"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "bias_type": {
        "num_classes": 9,
        "names": [
            "race-color",
            "socioeconomic",
            "gender",
            "disability",
            "nationality",
            "sexual-orientation",
            "physical-appearance",
            "religion",
            "age"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "annotations": {
        "feature": {
            "feature": {
                "num_classes": 9,
                "names": [
                    "race-color",
                    "socioeconomic",
                    "gender",
                    "disability",
                    "nationality",
                    "sexual-orientation",
                    "physical-appearance",
                    "religion",
                    "age"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "anon_writer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "anon_annotators": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


