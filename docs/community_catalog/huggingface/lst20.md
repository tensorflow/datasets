# lst20

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lst20)
*   [Huggingface](https://huggingface.co/datasets/lst20)


## lst20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lst20/lst20')
```

*   **Description**:

```
LST20 Corpus is a dataset for Thai language processing developed by National Electronics and Computer Technology Center (NECTEC), Thailand.
It offers five layers of linguistic annotation: word boundaries, POS tagging, named entities, clause boundaries, and sentence boundaries.
At a large scale, it consists of 3,164,002 words, 288,020 named entities, 248,181 clauses, and 74,180 sentences, while it is annotated with
16 distinct POS tags. All 3,745 documents are also annotated with one of 15 news genres. Regarding its sheer size, this dataset is
considered large enough for developing joint neural models for NLP.
Manually download at https://aiforthai.in.th/corpus.php
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5250
`'train'` | 63310
`'validation'` | 5620

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fname": {
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
    "pos_tags": {
        "feature": {
            "num_classes": 16,
            "names": [
                "NN",
                "VV",
                "PU",
                "CC",
                "PS",
                "AX",
                "AV",
                "FX",
                "NU",
                "AJ",
                "CL",
                "PR",
                "NG",
                "PA",
                "XX",
                "IJ"
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
            "num_classes": 31,
            "names": [
                "O",
                "B_BRN",
                "B_DES",
                "B_DTM",
                "B_LOC",
                "B_MEA",
                "B_NUM",
                "B_ORG",
                "B_PER",
                "B_TRM",
                "B_TTL",
                "I_BRN",
                "I_DES",
                "I_DTM",
                "I_LOC",
                "I_MEA",
                "I_NUM",
                "I_ORG",
                "I_PER",
                "I_TRM",
                "I_TTL",
                "E_BRN",
                "E_DES",
                "E_DTM",
                "E_LOC",
                "E_MEA",
                "E_NUM",
                "E_ORG",
                "E_PER",
                "E_TRM",
                "E_TTL"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "clause_tags": {
        "feature": {
            "num_classes": 4,
            "names": [
                "O",
                "B_CLS",
                "I_CLS",
                "E_CLS"
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


