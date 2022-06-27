# afrikaans_ner_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/afrikaans_ner_corpus)
*   [Huggingface](https://huggingface.co/datasets/afrikaans_ner_corpus)


## afrikaans_ner_corpus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:afrikaans_ner_corpus/afrikaans_ner_corpus')
```

*   **Description**:

```
Named entity annotated data from the NCHLT Text Resource Development: Phase II Project, annotated with PERSON, LOCATION, ORGANISATION and MISCELLANEOUS tags.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8962

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
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
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


