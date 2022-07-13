# jnlpba

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/jnlpba)
*   [Huggingface](https://huggingface.co/datasets/jnlpba)


## jnlpba


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:jnlpba/jnlpba')
```

*   **Description**:

```
The data came from the GENIA version 3.02 corpus (Kim et al., 2003). This was formed from a controlled search
on MEDLINE using the MeSH terms human, blood cells and transcription factors. From this search 2,000 abstracts
were selected and hand annotated according to a small taxonomy of 48 classes based on a chemical classification.
Among the classes, 36 terminal classes were used to annotate the GENIA corpus.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 37094
`'validation'` | 7714

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
            "num_classes": 11,
            "names": [
                "O",
                "B-DNA",
                "I-DNA",
                "B-RNA",
                "I-RNA",
                "B-cell_line",
                "I-cell_line",
                "B-cell_type",
                "I-cell_type",
                "B-protein",
                "I-protein"
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


