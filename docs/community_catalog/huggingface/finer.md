# finer

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/finer)
*   [Huggingface](https://huggingface.co/datasets/finer)


## finer


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:finer/finer')
```

*   **Description**:

```
The directory data contains a corpus of Finnish technology related news articles with a manually prepared
named entity annotation (digitoday.2014.csv). The text material was extracted from the archives of Digitoday,
a Finnish online technology news source (www.digitoday.fi). The corpus consists of 953 articles
(193,742 word tokens) with six named entity classes (organization, location, person, product, event, and date).
The corpus is available for research purposes and can be readily used for development of NER systems for Finnish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3512
`'test_wikipedia'` | 3360
`'train'` | 13497
`'validation'` | 986

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
                "O",
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
                "I-PRO"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "nested_ner_tags": {
        "feature": {
            "num_classes": 13,
            "names": [
                "O",
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
                "I-PRO"
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


