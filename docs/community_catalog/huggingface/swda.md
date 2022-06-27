# swda

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/swda)
*   [Huggingface](https://huggingface.co/datasets/swda)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swda')
```

*   **Description**:

```
The Switchboard Dialog Act Corpus (SwDA) extends the Switchboard-1 Telephone Speech Corpus, Release 2 with
turn/utterance-level dialog-act tags. The tags summarize syntactic, semantic, and pragmatic information about the
associated turn. The SwDA project was undertaken at UC Boulder in the late 1990s.
The SwDA is not inherently linked to the Penn Treebank 3 parses of Switchboard, and it is far from straightforward to
align the two resources. In addition, the SwDA is not distributed with the Switchboard's tables of metadata about the
conversations and their participants.
```

*   **License**: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4514
`'train'` | 213543
`'validation'` | 56729

*   **Features**:

```json
{
    "swda_filename": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ptb_basename": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "conversation_no": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "transcript_index": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "act_tag": {
        "num_classes": 217,
        "names": [
            "b^m^r",
            "qw^r^t",
            "aa^h",
            "br^m",
            "fa^r",
            "aa,ar",
            "sd^e(^q)^r",
            "^2",
            "sd;qy^d",
            "oo",
            "bk^m",
            "aa^t",
            "cc^t",
            "qy^d^c",
            "qo^t",
            "ng^m",
            "qw^h",
            "qo^r",
            "aa",
            "qy^d^t",
            "qrr^d",
            "br^r",
            "fx",
            "sd,qy^g",
            "ny^e",
            "^h^t",
            "fc^m",
            "qw(^q)",
            "co",
            "o^t",
            "b^m^t",
            "qr^d",
            "qw^g",
            "ad(^q)",
            "qy(^q)",
            "na^r",
            "am^r",
            "qr^t",
            "ad^c",
            "qw^c",
            "bh^r",
            "h^t",
            "ft^m",
            "ba^r",
            "qw^d^t",
            "%",
            "t3",
            "nn",
            "bd",
            "h^m",
            "h^r",
            "sd^r",
            "qh^m",
            "^q^t",
            "sv^2",
            "ft",
            "ar^m",
            "qy^h",
            "sd^e^m",
            "qh^r",
            "cc",
            "fp^m",
            "ad",
            "qo",
            "na^m^t",
            "fo^c",
            "qy",
            "sv^e^r",
            "aap",
            "no",
            "aa^2",
            "sv(^q)",
            "sv^e",
            "nd",
            "\"",
            "bf^2",
            "bk",
            "fp",
            "nn^r^t",
            "fa^c",
            "ny^t",
            "ny^c^r",
            "qw",
            "qy^t",
            "b",
            "fo",
            "qw^r",
            "am",
            "bf^t",
            "^2^t",
            "b^2",
            "x",
            "fc",
            "qr",
            "no^t",
            "bk^t",
            "bd^r",
            "bf",
            "^2^g",
            "qh^c",
            "ny^c",
            "sd^e^r",
            "br",
            "fe",
            "by",
            "^2^r",
            "fc^r",
            "b^m",
            "sd,sv",
            "fa^t",
            "sv^m",
            "qrr",
            "^h^r",
            "na",
            "fp^r",
            "o",
            "h,sd",
            "t1^t",
            "nn^r",
            "cc^r",
            "sv^c",
            "co^t",
            "qy^r",
            "sv^r",
            "qy^d^h",
            "sd",
            "nn^e",
            "ny^r",
            "b^t",
            "ba^m",
            "ar",
            "bf^r",
            "sv",
            "bh^m",
            "qy^g^t",
            "qo^d^c",
            "qo^d",
            "nd^t",
            "aa^r",
            "sd^2",
            "sv;sd",
            "qy^c^r",
            "qw^m",
            "qy^g^r",
            "no^r",
            "qh(^q)",
            "sd;sv",
            "bf(^q)",
            "+",
            "qy^2",
            "qw^d",
            "qy^g",
            "qh^g",
            "nn^t",
            "ad^r",
            "oo^t",
            "co^c",
            "ng",
            "^q",
            "qw^d^c",
            "qrr^t",
            "^h",
            "aap^r",
            "bc^r",
            "sd^m",
            "bk^r",
            "qy^g^c",
            "qr(^q)",
            "ng^t",
            "arp",
            "h",
            "bh",
            "sd^c",
            "^g",
            "o^r",
            "qy^c",
            "sd^e",
            "fw",
            "ar^r",
            "qy^m",
            "bc",
            "sv^t",
            "aap^m",
            "sd;no",
            "ng^r",
            "bf^g",
            "sd^e^t",
            "o^c",
            "b^r",
            "b^m^g",
            "ba",
            "t1",
            "qy^d(^q)",
            "nn^m",
            "ny",
            "ba,fe",
            "aa^m",
            "qh",
            "na^m",
            "oo(^q)",
            "qw^t",
            "na^t",
            "qh^h",
            "qy^d^m",
            "ny^m",
            "fa",
            "qy^d",
            "fc^t",
            "sd(^q)",
            "qy^d^r",
            "bf^m",
            "sd(^q)^t",
            "ft^t",
            "^q^r",
            "sd^t",
            "sd(^q)^r",
            "ad^t"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "damsl_act_tag": {
        "num_classes": 43,
        "names": [
            "ad",
            "qo",
            "qy",
            "arp_nd",
            "sd",
            "h",
            "bh",
            "no",
            "^2",
            "^g",
            "ar",
            "aa",
            "sv",
            "bk",
            "fp",
            "qw",
            "b",
            "ba",
            "t1",
            "oo_co_cc",
            "+",
            "ny",
            "qw^d",
            "x",
            "qh",
            "fc",
            "fo_o_fw_\"_by_bc",
            "aap_am",
            "%",
            "bf",
            "t3",
            "nn",
            "bd",
            "ng",
            "^q",
            "br",
            "qy^d",
            "fa",
            "^h",
            "b^m",
            "ft",
            "qrr",
            "na"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "caller": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance_index": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "subutterance_index": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pos": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trees": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ptb_treenumbers": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "talk_day": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "length": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "topic_description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "prompt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "from_caller": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "from_caller_sex": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "from_caller_education": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "from_caller_birth_year": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "from_caller_dialect_area": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "to_caller": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "to_caller_sex": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "to_caller_education": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "to_caller_birth_year": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "to_caller_dialect_area": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


