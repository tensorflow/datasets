# wino_bias

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wino_bias)
*   [Huggingface](https://huggingface.co/datasets/wino_bias)


## wino_bias


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wino_bias/wino_bias')
```

*   **Description**:

```
WinoBias, a Winograd-schema dataset for coreference resolution focused on gender bias.
The corpus contains Winograd-schema style sentences with entities corresponding to people
referred by their occupation (e.g. the nurse, the doctor, the carpenter).
```

*   **License**: MIT License (https://github.com/uclanlp/corefBias/blob/master/LICENSE)
*   **Version**: 4.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 150335

*   **Features**:

```json
{
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "part_number": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_number": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
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
            "num_classes": 54,
            "names": [
                "\"",
                "''",
                "#",
                "$",
                "(",
                ")",
                ",",
                ".",
                ":",
                "``",
                "CC",
                "CD",
                "DT",
                "EX",
                "FW",
                "IN",
                "JJ",
                "JJR",
                "JJS",
                "LS",
                "MD",
                "NN",
                "NNP",
                "NNPS",
                "NNS",
                "NN|SYM",
                "PDT",
                "POS",
                "PRP",
                "PRP$",
                "RB",
                "RBR",
                "RBS",
                "RP",
                "SYM",
                "TO",
                "UH",
                "VB",
                "VBD",
                "VBG",
                "VBN",
                "VBP",
                "VBZ",
                "WDT",
                "WP",
                "WP$",
                "WRB",
                "HYPH",
                "XX",
                "NFP",
                "AFX",
                "ADD",
                "-LRB-",
                "-RRB-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "parse_bit": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_lemma": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_framenet_id": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_sense": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "speaker": {
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
            "num_classes": 38,
            "names": [
                "B-PERSON",
                "I-PERSON",
                "B-NORP",
                "I-NORP",
                "B-FAC",
                "I-FAC",
                "B-ORG",
                "I-ORG",
                "B-GPE",
                "I-GPE",
                "B-LOC",
                "I-LOC",
                "B-PRODUCT",
                "I-PRODUCT",
                "B-EVENT",
                "I-EVENT",
                "B-WORK_OF_ART",
                "I-WORK_OF_ART",
                "B-LAW",
                "I-LAW",
                "B-LANGUAGE",
                "I-LANGUAGE",
                "B-DATE",
                "I-DATE",
                "B-TIME",
                "I-TIME",
                "B-PERCENT",
                "I-PERCENT",
                "B-MONEY",
                "I-MONEY",
                "B-QUANTITY",
                "I-QUANTITY",
                "B-ORDINAL",
                "I-ORDINAL",
                "B-CARDINAL",
                "I-CARDINAL",
                "*",
                "0"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "verbal_predicates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## type1_pro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wino_bias/type1_pro')
```

*   **Description**:

```
WinoBias, a Winograd-schema dataset for coreference resolution focused on gender bias.
The corpus contains Winograd-schema style sentences with entities corresponding to people
referred by their occupation (e.g. the nurse, the doctor, the carpenter).
```

*   **License**: MIT License (https://github.com/uclanlp/corefBias/blob/master/LICENSE)
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 396
`'validation'` | 396

*   **Features**:

```json
{
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "part_number": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_number": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
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
            "num_classes": 55,
            "names": [
                "\"",
                "''",
                "#",
                "$",
                "(",
                ")",
                ",",
                ".",
                ":",
                "``",
                "CC",
                "CD",
                "DT",
                "EX",
                "FW",
                "IN",
                "JJ",
                "JJR",
                "JJS",
                "LS",
                "MD",
                "NN",
                "NNP",
                "NNPS",
                "NNS",
                "NN|SYM",
                "PDT",
                "POS",
                "PRP",
                "PRP$",
                "RB",
                "RBR",
                "RBS",
                "RP",
                "SYM",
                "TO",
                "UH",
                "VB",
                "VBD",
                "VBG",
                "VBN",
                "VBP",
                "VBZ",
                "WDT",
                "WP",
                "WP$",
                "WRB",
                "HYPH",
                "XX",
                "NFP",
                "AFX",
                "ADD",
                "-LRB-",
                "-RRB-",
                "-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "parse_bit": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_lemma": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_framenet_id": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_sense": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "speaker": {
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
            "num_classes": 39,
            "names": [
                "B-PERSON",
                "I-PERSON",
                "B-NORP",
                "I-NORP",
                "B-FAC",
                "I-FAC",
                "B-ORG",
                "I-ORG",
                "B-GPE",
                "I-GPE",
                "B-LOC",
                "I-LOC",
                "B-PRODUCT",
                "I-PRODUCT",
                "B-EVENT",
                "I-EVENT",
                "B-WORK_OF_ART",
                "I-WORK_OF_ART",
                "B-LAW",
                "I-LAW",
                "B-LANGUAGE",
                "I-LANGUAGE",
                "B-DATE",
                "I-DATE",
                "B-TIME",
                "I-TIME",
                "B-PERCENT",
                "I-PERCENT",
                "B-MONEY",
                "I-MONEY",
                "B-QUANTITY",
                "I-QUANTITY",
                "B-ORDINAL",
                "I-ORDINAL",
                "B-CARDINAL",
                "I-CARDINAL",
                "*",
                "0",
                "-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "verbal_predicates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "coreference_clusters": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## type1_anti


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wino_bias/type1_anti')
```

*   **Description**:

```
WinoBias, a Winograd-schema dataset for coreference resolution focused on gender bias.
The corpus contains Winograd-schema style sentences with entities corresponding to people
referred by their occupation (e.g. the nurse, the doctor, the carpenter).
```

*   **License**: MIT License (https://github.com/uclanlp/corefBias/blob/master/LICENSE)
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 396
`'validation'` | 396

*   **Features**:

```json
{
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "part_number": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_number": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
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
            "num_classes": 55,
            "names": [
                "\"",
                "''",
                "#",
                "$",
                "(",
                ")",
                ",",
                ".",
                ":",
                "``",
                "CC",
                "CD",
                "DT",
                "EX",
                "FW",
                "IN",
                "JJ",
                "JJR",
                "JJS",
                "LS",
                "MD",
                "NN",
                "NNP",
                "NNPS",
                "NNS",
                "NN|SYM",
                "PDT",
                "POS",
                "PRP",
                "PRP$",
                "RB",
                "RBR",
                "RBS",
                "RP",
                "SYM",
                "TO",
                "UH",
                "VB",
                "VBD",
                "VBG",
                "VBN",
                "VBP",
                "VBZ",
                "WDT",
                "WP",
                "WP$",
                "WRB",
                "HYPH",
                "XX",
                "NFP",
                "AFX",
                "ADD",
                "-LRB-",
                "-RRB-",
                "-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "parse_bit": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_lemma": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_framenet_id": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_sense": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "speaker": {
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
            "num_classes": 39,
            "names": [
                "B-PERSON",
                "I-PERSON",
                "B-NORP",
                "I-NORP",
                "B-FAC",
                "I-FAC",
                "B-ORG",
                "I-ORG",
                "B-GPE",
                "I-GPE",
                "B-LOC",
                "I-LOC",
                "B-PRODUCT",
                "I-PRODUCT",
                "B-EVENT",
                "I-EVENT",
                "B-WORK_OF_ART",
                "I-WORK_OF_ART",
                "B-LAW",
                "I-LAW",
                "B-LANGUAGE",
                "I-LANGUAGE",
                "B-DATE",
                "I-DATE",
                "B-TIME",
                "I-TIME",
                "B-PERCENT",
                "I-PERCENT",
                "B-MONEY",
                "I-MONEY",
                "B-QUANTITY",
                "I-QUANTITY",
                "B-ORDINAL",
                "I-ORDINAL",
                "B-CARDINAL",
                "I-CARDINAL",
                "*",
                "0",
                "-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "verbal_predicates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "coreference_clusters": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## type2_pro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wino_bias/type2_pro')
```

*   **Description**:

```
WinoBias, a Winograd-schema dataset for coreference resolution focused on gender bias.
The corpus contains Winograd-schema style sentences with entities corresponding to people
referred by their occupation (e.g. the nurse, the doctor, the carpenter).
```

*   **License**: MIT License (https://github.com/uclanlp/corefBias/blob/master/LICENSE)
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 396
`'validation'` | 396

*   **Features**:

```json
{
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "part_number": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_number": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
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
            "num_classes": 55,
            "names": [
                "\"",
                "''",
                "#",
                "$",
                "(",
                ")",
                ",",
                ".",
                ":",
                "``",
                "CC",
                "CD",
                "DT",
                "EX",
                "FW",
                "IN",
                "JJ",
                "JJR",
                "JJS",
                "LS",
                "MD",
                "NN",
                "NNP",
                "NNPS",
                "NNS",
                "NN|SYM",
                "PDT",
                "POS",
                "PRP",
                "PRP$",
                "RB",
                "RBR",
                "RBS",
                "RP",
                "SYM",
                "TO",
                "UH",
                "VB",
                "VBD",
                "VBG",
                "VBN",
                "VBP",
                "VBZ",
                "WDT",
                "WP",
                "WP$",
                "WRB",
                "HYPH",
                "XX",
                "NFP",
                "AFX",
                "ADD",
                "-LRB-",
                "-RRB-",
                "-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "parse_bit": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_lemma": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_framenet_id": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_sense": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "speaker": {
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
            "num_classes": 39,
            "names": [
                "B-PERSON",
                "I-PERSON",
                "B-NORP",
                "I-NORP",
                "B-FAC",
                "I-FAC",
                "B-ORG",
                "I-ORG",
                "B-GPE",
                "I-GPE",
                "B-LOC",
                "I-LOC",
                "B-PRODUCT",
                "I-PRODUCT",
                "B-EVENT",
                "I-EVENT",
                "B-WORK_OF_ART",
                "I-WORK_OF_ART",
                "B-LAW",
                "I-LAW",
                "B-LANGUAGE",
                "I-LANGUAGE",
                "B-DATE",
                "I-DATE",
                "B-TIME",
                "I-TIME",
                "B-PERCENT",
                "I-PERCENT",
                "B-MONEY",
                "I-MONEY",
                "B-QUANTITY",
                "I-QUANTITY",
                "B-ORDINAL",
                "I-ORDINAL",
                "B-CARDINAL",
                "I-CARDINAL",
                "*",
                "0",
                "-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "verbal_predicates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "coreference_clusters": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## type2_anti


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wino_bias/type2_anti')
```

*   **Description**:

```
WinoBias, a Winograd-schema dataset for coreference resolution focused on gender bias.
The corpus contains Winograd-schema style sentences with entities corresponding to people
referred by their occupation (e.g. the nurse, the doctor, the carpenter).
```

*   **License**: MIT License (https://github.com/uclanlp/corefBias/blob/master/LICENSE)
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 396
`'validation'` | 396

*   **Features**:

```json
{
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "part_number": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_number": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
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
            "num_classes": 55,
            "names": [
                "\"",
                "''",
                "#",
                "$",
                "(",
                ")",
                ",",
                ".",
                ":",
                "``",
                "CC",
                "CD",
                "DT",
                "EX",
                "FW",
                "IN",
                "JJ",
                "JJR",
                "JJS",
                "LS",
                "MD",
                "NN",
                "NNP",
                "NNPS",
                "NNS",
                "NN|SYM",
                "PDT",
                "POS",
                "PRP",
                "PRP$",
                "RB",
                "RBR",
                "RBS",
                "RP",
                "SYM",
                "TO",
                "UH",
                "VB",
                "VBD",
                "VBG",
                "VBN",
                "VBP",
                "VBZ",
                "WDT",
                "WP",
                "WP$",
                "WRB",
                "HYPH",
                "XX",
                "NFP",
                "AFX",
                "ADD",
                "-LRB-",
                "-RRB-",
                "-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "parse_bit": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_lemma": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "predicate_framenet_id": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_sense": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "speaker": {
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
            "num_classes": 39,
            "names": [
                "B-PERSON",
                "I-PERSON",
                "B-NORP",
                "I-NORP",
                "B-FAC",
                "I-FAC",
                "B-ORG",
                "I-ORG",
                "B-GPE",
                "I-GPE",
                "B-LOC",
                "I-LOC",
                "B-PRODUCT",
                "I-PRODUCT",
                "B-EVENT",
                "I-EVENT",
                "B-WORK_OF_ART",
                "I-WORK_OF_ART",
                "B-LAW",
                "I-LAW",
                "B-LANGUAGE",
                "I-LANGUAGE",
                "B-DATE",
                "I-DATE",
                "B-TIME",
                "I-TIME",
                "B-PERCENT",
                "I-PERCENT",
                "B-MONEY",
                "I-MONEY",
                "B-QUANTITY",
                "I-QUANTITY",
                "B-ORDINAL",
                "I-ORDINAL",
                "B-CARDINAL",
                "I-CARDINAL",
                "*",
                "0",
                "-"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "verbal_predicates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "coreference_clusters": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


