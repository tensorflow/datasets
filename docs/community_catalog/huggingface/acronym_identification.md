# acronym_identification

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/acronym_identification)
*   [Huggingface](https://huggingface.co/datasets/acronym_identification)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:acronym_identification')
```

*   **Description**:

```
Acronym identification training and development sets for the acronym identification task at SDU@AAAI-21.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1750
`'train'` | 14006
`'validation'` | 1717

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
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
            "num_classes": 5,
            "names": [
                "B-long",
                "B-short",
                "I-long",
                "I-short",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


