# norne

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/norne)
*   [Huggingface](https://huggingface.co/datasets/norne)


## bokmaal


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/bokmaal')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
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
    "lang": {
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
            "num_classes": 19,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-GPE_LOC",
                "I-GPE_LOC",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-GPE_ORG",
                "I-GPE_ORG",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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



## nynorsk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/nynorsk')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
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
    "lang": {
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
            "num_classes": 19,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-GPE_LOC",
                "I-GPE_LOC",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-GPE_ORG",
                "I-GPE_ORG",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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



## combined


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/combined')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3450
`'train'` | 29870
`'validation'` | 4300

*   **Features**:

```json
{
    "idx": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
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
            "num_classes": 19,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-GPE_LOC",
                "I-GPE_LOC",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-GPE_ORG",
                "I-GPE_ORG",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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



## bokmaal-7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/bokmaal-7')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
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
    "lang": {
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
            "num_classes": 15,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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



## nynorsk-7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/nynorsk-7')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
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
    "lang": {
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
            "num_classes": 15,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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



## combined-7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/combined-7')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3450
`'train'` | 29870
`'validation'` | 4300

*   **Features**:

```json
{
    "idx": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
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
            "num_classes": 15,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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



## bokmaal-8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/bokmaal-8')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
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
    "lang": {
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
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-GPE",
                "I-GPE",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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



## nynorsk-8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/nynorsk-8')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
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
    "lang": {
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
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-GPE",
                "I-GPE",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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



## combined-8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:norne/combined-8')
```

*   **Description**:

```
NorNE is a manually annotated
corpus of named entities which extends the annotation of the existing
Norwegian Dependency Treebank. Comprising both of the official standards of
written Norwegian (Bokmål and Nynorsk), the corpus contains around 600,000
tokens and annotates a rich set of entity types including persons,
organizations, locations, geo-political entities, products, and events,
in addition to a class corresponding to nominals derived from names.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3450
`'train'` | 29870
`'validation'` | 4300

*   **Features**:

```json
{
    "idx": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
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
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-PROD",
                "I-PROD",
                "B-LOC",
                "I-LOC",
                "B-GPE",
                "I-GPE",
                "B-DRV",
                "I-DRV",
                "B-EVT",
                "I-EVT",
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


