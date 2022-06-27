# liar

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/liar)
*   [Huggingface](https://huggingface.co/datasets/liar)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:liar')
```

*   **Description**:

```
LIAR is a dataset for fake news detection with 12.8K human labeled short statements from politifact.com's API, and each statement is evaluated by a politifact.com editor for its truthfulness. The distribution of labels in the LIAR dataset is relatively well-balanced: except for 1,050 pants-fire cases, the instances for all other labels range from 2,063 to 2,638. In each case, the labeler provides a lengthy analysis report to ground each judgment.
```

*   **License**: Unknown
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1283
`'train'` | 10269
`'validation'` | 1284

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 6,
        "names": [
            "false",
            "half-true",
            "mostly-true",
            "true",
            "barely-true",
            "pants-fire"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "statement": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "job_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "state_info": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "party_affiliation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "barely_true_counts": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "false_counts": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "half_true_counts": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "mostly_true_counts": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "pants_on_fire_counts": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


