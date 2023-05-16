# offenseval2020_tr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/offenseval2020_tr)
*   [Huggingface](https://huggingface.co/datasets/offenseval2020_tr)


## offenseval2020-turkish


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:offenseval2020_tr/offenseval2020-turkish')
```

*   **Description**:

```
OffensEval-TR 2020 is a Turkish offensive language corpus. The corpus consist of randomly sampled tweets, and annotated in a similar way to OffensEval and GermEval.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3528
`'train'` | 31756

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "tweet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subtask_a": {
        "num_classes": 2,
        "names": [
            "NOT",
            "OFF"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


