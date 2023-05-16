# linnaeus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/linnaeus)
*   [Huggingface](https://huggingface.co/datasets/linnaeus)


## linnaeus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:linnaeus/linnaeus')
```

*   **Description**:

```
A novel corpus of full-text documents manually annotated for species mentions.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7143
`'train'` | 11936
`'validation'` | 4079

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
    "ner_tags": {
        "feature": {
            "num_classes": 3,
            "names": [
                "O",
                "B",
                "I"
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


