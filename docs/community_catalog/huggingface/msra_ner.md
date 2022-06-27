# msra_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/msra_ner)
*   [Huggingface](https://huggingface.co/datasets/msra_ner)


## msra_ner


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:msra_ner/msra_ner')
```

*   **Description**:

```
The Third International Chinese Language
Processing Bakeoff was held in Spring
2006 to assess the state of the art in two
important tasks: word segmentation and
named entity recognition. Twenty-nine
groups submitted result sets in the two
tasks across two tracks and a total of five
corpora. We found strong results in both
tasks as well as continuing challenges.

MSRA NER is one of the provided dataset.
There are three types of NE, PER (person),
ORG (organization) and LOC (location).
The dataset is in the BIO scheme.

For more details see https://faculty.washington.edu/levow/papers/sighan06.pdf
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3443
`'train'` | 45001

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


