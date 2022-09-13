# hkcancor

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hkcancor)
*   [Huggingface](https://huggingface.co/datasets/hkcancor)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hkcancor')
```

*   **Description**:

```
The Hong Kong Cantonese Corpus (HKCanCor) comprise transcribed conversations
recorded between March 1997 and August 1998. It contains recordings of
spontaneous speech (51 texts) and radio programmes (42 texts),
which involve 2 to 4 speakers, with 1 text of monologue.

In total, the corpus contains around 230,000 Chinese words.
The text is word-segmented, annotated with part-of-speech (POS) tags and
romanised Cantonese pronunciation.

Romanisation scheme - Linguistic Society of Hong Kong (LSHK)
POS scheme - Peita-Fujitsu-Renmin Ribao (PRF) corpus (Duan et al., 2000),
             with extended tags for Cantonese-specific phenomena added by
             Luke and Wang (see original paper for details).
```

*   **License**: CC BY 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10801

*   **Features**:

```json
{
    "conversation_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "turn_number": {
        "dtype": "int16",
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
    "transcriptions": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pos_tags_prf": {
        "feature": {
            "num_classes": 120,
            "names": [
                "!",
                "\"",
                "#",
                "'",
                ",",
                "-",
                ".",
                "...",
                "?",
                "A",
                "AD",
                "AG",
                "AIRWAYS0",
                "AN",
                "AND",
                "B",
                "BG",
                "BEAN0",
                "C",
                "CENTRE0",
                "CG",
                "D",
                "D1",
                "DG",
                "E",
                "ECHO0",
                "F",
                "G",
                "G1",
                "G2",
                "H",
                "HILL0",
                "I",
                "IG",
                "J",
                "JB",
                "JM",
                "JN",
                "JNS",
                "JNT",
                "JNZ",
                "K",
                "KONG",
                "L",
                "L1",
                "LG",
                "M",
                "MG",
                "MONTY0",
                "MOUNTAIN0",
                "N",
                "N1",
                "NG",
                "NR",
                "NS",
                "NSG",
                "NT",
                "NX",
                "NZ",
                "O",
                "P",
                "PEPPER0",
                "Q",
                "QG",
                "R",
                "RG",
                "S",
                "SOUND0",
                "T",
                "TELECOM0",
                "TG",
                "TOUCH0",
                "U",
                "UG",
                "U0",
                "V",
                "V1",
                "VD",
                "VG",
                "VK",
                "VN",
                "VU",
                "VUG",
                "W",
                "X",
                "XA",
                "XB",
                "XC",
                "XD",
                "XE",
                "XJ",
                "XJB",
                "XJN",
                "XJNT",
                "XJNZ",
                "XJV",
                "XJA",
                "XL1",
                "XM",
                "XN",
                "XNG",
                "XNR",
                "XNS",
                "XNT",
                "XNX",
                "XNZ",
                "XO",
                "XP",
                "XQ",
                "XR",
                "XS",
                "XT",
                "XV",
                "XVG",
                "XVN",
                "XX",
                "Y",
                "YG",
                "Y1",
                "Z"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pos_tags_ud": {
        "feature": {
            "num_classes": 16,
            "names": [
                "DET",
                "PRON",
                "VERB",
                "NOUN",
                "ADJ",
                "PUNCT",
                "INTJ",
                "ADV",
                "V",
                "PART",
                "X",
                "NUM",
                "PROPN",
                "AUX",
                "CCONJ",
                "ADP"
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


