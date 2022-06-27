# sesotho_ner_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sesotho_ner_corpus)
*   [Huggingface](https://huggingface.co/datasets/sesotho_ner_corpus)


## sesotho_ner_corpus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sesotho_ner_corpus/sesotho_ner_corpus')
```

*   **Description**:

```
Named entity annotated data from the NCHLT Text Resource Development: Phase II Project, annotated with PERSON, LOCATION, ORGANISATION and MISCELLANEOUS tags.
```

*   **License**: Creative Commons Attribution 2.5 South Africa License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 9472

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


