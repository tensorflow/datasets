# art

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/art)
*   [Huggingface](https://huggingface.co/datasets/art)


## anli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:art/anli')
```

*   **Description**:

```
the Abductive Natural Language Inference Dataset from AI2
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 169654
`'validation'` | 1532

*   **Features**:

```json
{
    "observation_1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "observation_2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis_1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis_2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "0",
            "1",
            "2"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


