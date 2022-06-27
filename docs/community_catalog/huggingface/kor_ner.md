# kor_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kor_ner)
*   [Huggingface](https://huggingface.co/datasets/kor_ner)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_ner')
```

*   **Description**:

```
Korean named entity recognition dataset
```

*   **License**: NER License, MIT License for non-commercial use
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 366
`'train'` | 2928
`'validation'` | 366

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annot_text": {
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
            "num_classes": 42,
            "names": [
                "SO",
                "SS",
                "VV",
                "XR",
                "VCP",
                "JC",
                "VCN",
                "JKB",
                "MM",
                "SP",
                "XSN",
                "SL",
                "NNP",
                "NP",
                "EP",
                "JKQ",
                "IC",
                "XSA",
                "EC",
                "EF",
                "SE",
                "XPN",
                "ETN",
                "SH",
                "XSV",
                "MAG",
                "SW",
                "ETM",
                "JKO",
                "NNB",
                "MAJ",
                "NNG",
                "JKV",
                "JKC",
                "VA",
                "NR",
                "JKG",
                "VX",
                "SF",
                "JX",
                "JKS",
                "SN"
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
            "num_classes": 7,
            "names": [
                "I",
                "O",
                "B_OG",
                "B_TI",
                "B_LC",
                "B_DT",
                "B_PS"
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


