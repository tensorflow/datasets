# thainer

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/thainer)
*   [Huggingface](https://huggingface.co/datasets/thainer)


## thainer


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:thainer/thainer')
```

*   **Description**:

```
ThaiNER (v1.3) is a 6,456-sentence named entity recognition dataset created from expanding the 2,258-sentence
[unnamed dataset](http://pioneer.chula.ac.th/~awirote/Data-Nutcha.zip) by
[Tirasaroj and Aroonmanakun (2012)](http://pioneer.chula.ac.th/~awirote/publications/).
It is used to train NER taggers in [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp).
The NER tags are annotated by [Tirasaroj and Aroonmanakun (2012)]((http://pioneer.chula.ac.th/~awirote/publications/))
for 2,258 sentences and the rest by [@wannaphong](https://github.com/wannaphong/).
The POS tags are done by [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp)'s `perceptron` engine trained on `orchid_ud`.
[@wannaphong](https://github.com/wannaphong/) is now the only maintainer of this dataset.
```

*   **License**: CC-BY 3.0
*   **Version**: 1.3.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6348

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
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
    "pos_tags": {
        "feature": {
            "num_classes": 14,
            "names": [
                "ADJ",
                "ADP",
                "ADV",
                "AUX",
                "CCONJ",
                "DET",
                "NOUN",
                "NUM",
                "PART",
                "PRON",
                "PROPN",
                "PUNCT",
                "SCONJ",
                "VERB"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 28,
            "names": [
                "B-DATE",
                "B-EMAIL",
                "B-LAW",
                "B-LEN",
                "B-LOCATION",
                "B-MONEY",
                "B-ORGANIZATION",
                "B-PERCENT",
                "B-PERSON",
                "B-PHONE",
                "B-TIME",
                "B-URL",
                "B-ZIP",
                "B-\u0e44\u0e21\u0e48\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19",
                "I-DATE",
                "I-EMAIL",
                "I-LAW",
                "I-LEN",
                "I-LOCATION",
                "I-MONEY",
                "I-ORGANIZATION",
                "I-PERCENT",
                "I-PERSON",
                "I-PHONE",
                "I-TIME",
                "I-URL",
                "I-\u0e44\u0e21\u0e48\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19",
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


