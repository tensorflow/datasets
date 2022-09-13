# norwegian_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/norwegian_ner)
*   [Huggingface](https://huggingface.co/datasets/norwegian_ner)


## bokmaal


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norwegian_ner/bokmaal')
```

*   **Description**:

```
Named entities Recognition dataset for Norwegian.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1939
`'train'` | 15696
`'validation'` | 2410

*   **Features**:

```json
{
    "idx": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
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
    "lemmas": {
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
            "num_classes": 17,
            "names": [
                "NOUN",
                "PUNCT",
                "ADP",
                "NUM",
                "SYM",
                "SCONJ",
                "ADJ",
                "PART",
                "DET",
                "CCONJ",
                "PROPN",
                "PRON",
                "X",
                "ADV",
                "INTJ",
                "VERB",
                "AUX"
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
            "num_classes": 17,
            "names": [
                "O",
                "B-OTH",
                "I-OTH",
                "E-OTH",
                "S-OTH",
                "B-ORG",
                "I-ORG",
                "E-ORG",
                "S-ORG",
                "B-PRS",
                "I-PRS",
                "E-PRS",
                "S-PRS",
                "B-GEO",
                "I-GEO",
                "E-GEO",
                "S-GEO"
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



## nynorsk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norwegian_ner/nynorsk')
```

*   **Description**:

```
Named entities Recognition dataset for Norwegian.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1511
`'train'` | 14174
`'validation'` | 1890

*   **Features**:

```json
{
    "idx": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
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
    "lemmas": {
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
            "num_classes": 17,
            "names": [
                "NOUN",
                "PUNCT",
                "ADP",
                "NUM",
                "SYM",
                "SCONJ",
                "ADJ",
                "PART",
                "DET",
                "CCONJ",
                "PROPN",
                "PRON",
                "X",
                "ADV",
                "INTJ",
                "VERB",
                "AUX"
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
            "num_classes": 17,
            "names": [
                "O",
                "B-OTH",
                "I-OTH",
                "E-OTH",
                "S-OTH",
                "B-ORG",
                "I-ORG",
                "E-ORG",
                "S-ORG",
                "B-PRS",
                "I-PRS",
                "E-PRS",
                "S-PRS",
                "B-GEO",
                "I-GEO",
                "E-GEO",
                "S-GEO"
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



## samnorsk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norwegian_ner/samnorsk')
```

*   **Description**:

```
Named entities Recognition dataset for Norwegian.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3450
`'train'` | 34170
`'validation'` | 4300

*   **Features**:

```json
{
    "idx": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
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
    "lemmas": {
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
            "num_classes": 17,
            "names": [
                "NOUN",
                "PUNCT",
                "ADP",
                "NUM",
                "SYM",
                "SCONJ",
                "ADJ",
                "PART",
                "DET",
                "CCONJ",
                "PROPN",
                "PRON",
                "X",
                "ADV",
                "INTJ",
                "VERB",
                "AUX"
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
            "num_classes": 17,
            "names": [
                "O",
                "B-OTH",
                "I-OTH",
                "E-OTH",
                "S-OTH",
                "B-ORG",
                "I-ORG",
                "E-ORG",
                "S-ORG",
                "B-PRS",
                "I-PRS",
                "E-PRS",
                "S-PRS",
                "B-GEO",
                "I-GEO",
                "E-GEO",
                "S-GEO"
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


