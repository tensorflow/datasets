# ade_corpus_v2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ade_corpus_v2)
*   [Huggingface](https://huggingface.co/datasets/ade_corpus_v2)


## Ade_corpus_v2_classification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ade_corpus_v2/Ade_corpus_v2_classification')
```

*   **Description**:

```
ADE-Corpus-V2  Dataset: Adverse Drug Reaction Data.
 This is a dataset for Classification if a sentence is ADE-related (True) or not (False) and Relation Extraction between Adverse Drug Event and Drug.
 DRUG-AE.rel provides relations between drugs and adverse effects.
 DRUG-DOSE.rel provides relations between drugs and dosages.
 ADE-NEG.txt provides all sentences in the ADE corpus that DO NOT contain any drug-related adverse effects.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 23516

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "Not-Related",
            "Related"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## Ade_corpus_v2_drug_ade_relation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ade_corpus_v2/Ade_corpus_v2_drug_ade_relation')
```

*   **Description**:

```
ADE-Corpus-V2  Dataset: Adverse Drug Reaction Data.
 This is a dataset for Classification if a sentence is ADE-related (True) or not (False) and Relation Extraction between Adverse Drug Event and Drug.
 DRUG-AE.rel provides relations between drugs and adverse effects.
 DRUG-DOSE.rel provides relations between drugs and dosages.
 ADE-NEG.txt provides all sentences in the ADE corpus that DO NOT contain any drug-related adverse effects.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6821

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "drug": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "effect": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "indexes": {
        "drug": {
            "feature": {
                "start_char": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_char": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "effect": {
            "feature": {
                "start_char": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_char": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    }
}
```



## Ade_corpus_v2_drug_dosage_relation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ade_corpus_v2/Ade_corpus_v2_drug_dosage_relation')
```

*   **Description**:

```
ADE-Corpus-V2  Dataset: Adverse Drug Reaction Data.
 This is a dataset for Classification if a sentence is ADE-related (True) or not (False) and Relation Extraction between Adverse Drug Event and Drug.
 DRUG-AE.rel provides relations between drugs and adverse effects.
 DRUG-DOSE.rel provides relations between drugs and dosages.
 ADE-NEG.txt provides all sentences in the ADE corpus that DO NOT contain any drug-related adverse effects.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 279

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "drug": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dosage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "indexes": {
        "drug": {
            "feature": {
                "start_char": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_char": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "dosage": {
            "feature": {
                "start_char": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_char": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    }
}
```


