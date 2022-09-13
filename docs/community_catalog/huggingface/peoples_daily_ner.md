# peoples_daily_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/peoples_daily_ner)
*   [Huggingface](https://huggingface.co/datasets/peoples_daily_ner)


## peoples_daily_ner


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:peoples_daily_ner/peoples_daily_ner')
```

*   **Description**:

```
People's Daily NER Dataset is a commonly used dataset for Chinese NER, with
text from People's Daily (人民日报), the largest official newspaper.

The dataset is in BIO scheme. Entity types are: PER (person), ORG (organization)
and LOC (location).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4637
`'train'` | 20865
`'validation'` | 2319

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
            "num_classes": 7,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC"
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


