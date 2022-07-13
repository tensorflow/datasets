# turku_ner_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/turku_ner_corpus)
*   [Huggingface](https://huggingface.co/datasets/turku_ner_corpus)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:turku_ner_corpus')
```

*   **Description**:

```
An open, broad-coverage corpus for Finnish named entity recognition presented in Luoma et al. (2020) A Broad-coverage Corpus for Finnish Named Entity Recognition.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1555
`'train'` | 12217
`'validation'` | 1364

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
            "num_classes": 13,
            "names": [
                "B-DATE",
                "B-EVENT",
                "B-LOC",
                "B-ORG",
                "B-PER",
                "B-PRO",
                "I-DATE",
                "I-EVENT",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "I-PRO",
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


