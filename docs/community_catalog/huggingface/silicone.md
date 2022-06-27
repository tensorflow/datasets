# silicone

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/silicone)
*   [Huggingface](https://huggingface.co/datasets/silicone)


## dyda_da


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/dyda_da')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7740
`'train'` | 87170
`'validation'` | 8069

*   **Features**:

```json
{
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 4,
        "names": [
            "commissive",
            "directive",
            "inform",
            "question"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## dyda_e


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/dyda_e')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7740
`'train'` | 87170
`'validation'` | 8069

*   **Features**:

```json
{
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Emotion": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 7,
        "names": [
            "anger",
            "disgust",
            "fear",
            "happiness",
            "no emotion",
            "sadness",
            "surprise"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## iemocap


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/iemocap')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2021
`'train'` | 7213
`'validation'` | 805

*   **Features**:

```json
{
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Emotion": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 11,
        "names": [
            "ang",
            "dis",
            "exc",
            "fea",
            "fru",
            "hap",
            "neu",
            "oth",
            "sad",
            "sur",
            "xxx"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## maptask


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/maptask')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2894
`'train'` | 20905
`'validation'` | 2963

*   **Features**:

```json
{
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 12,
        "names": [
            "acknowledge",
            "align",
            "check",
            "clarify",
            "explain",
            "instruct",
            "query_w",
            "query_yn",
            "ready",
            "reply_n",
            "reply_w",
            "reply_y"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## meld_e


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/meld_e')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2610
`'train'` | 9989
`'validation'` | 1109

*   **Features**:

```json
{
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Emotion": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 7,
        "names": [
            "anger",
            "disgust",
            "fear",
            "joy",
            "neutral",
            "sadness",
            "surprise"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## meld_s


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/meld_s')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2610
`'train'` | 9989
`'validation'` | 1109

*   **Features**:

```json
{
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Sentiment": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## mrda


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/mrda')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15470
`'train'` | 83943
`'validation'` | 9815

*   **Features**:

```json
{
    "Utterance_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Channel_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 5,
        "names": [
            "s",
            "d",
            "b",
            "f",
            "q"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## oasis


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/oasis')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1478
`'train'` | 12076
`'validation'` | 1513

*   **Features**:

```json
{
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 42,
        "names": [
            "accept",
            "ackn",
            "answ",
            "answElab",
            "appreciate",
            "backch",
            "bye",
            "complete",
            "confirm",
            "correct",
            "direct",
            "directElab",
            "echo",
            "exclaim",
            "expressOpinion",
            "expressPossibility",
            "expressRegret",
            "expressWish",
            "greet",
            "hold",
            "identifySelf",
            "inform",
            "informCont",
            "informDisc",
            "informIntent",
            "init",
            "negate",
            "offer",
            "pardon",
            "raiseIssue",
            "refer",
            "refuse",
            "reqDirect",
            "reqInfo",
            "reqModal",
            "selfTalk",
            "suggest",
            "thank",
            "informIntent-hold",
            "correctSelf",
            "expressRegret-inform",
            "thank-identifySelf"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## sem


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/sem')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 878
`'train'` | 4264
`'validation'` | 485

*   **Features**:

```json
{
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "NbPairInSession": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "SpeechTurn": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Sentiment": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## swda


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:silicone/swda')
```

*   **Description**:

```
The Sequence labellIng evaLuatIon benChmark fOr spoken laNguagE (SILICONE) benchmark is a collection
 of resources for training, evaluating, and analyzing natural language understanding systems
 specifically designed for spoken language. All datasets are in the English language and cover a
 variety of domains including daily life, scripted scenarios, joint task completion, phone call
 conversations, and televsion dialogue. Some datasets additionally include emotion and/or sentimant
 labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2714
`'train'` | 190709
`'validation'` | 21203

*   **Features**:

```json
{
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "From_Caller": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "To_Caller": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Topic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Conv_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 46,
        "names": [
            "sd",
            "b",
            "sv",
            "%",
            "aa",
            "ba",
            "fc",
            "qw",
            "nn",
            "bk",
            "h",
            "qy^d",
            "bh",
            "^q",
            "bf",
            "fo_o_fw_\"_by_bc",
            "fo_o_fw_by_bc_\"",
            "na",
            "ad",
            "^2",
            "b^m",
            "qo",
            "qh",
            "^h",
            "ar",
            "ng",
            "br",
            "no",
            "fp",
            "qrr",
            "arp_nd",
            "t3",
            "oo_co_cc",
            "aap_am",
            "t1",
            "bd",
            "^g",
            "qw^d",
            "fa",
            "ft",
            "+",
            "x",
            "ny",
            "sv_fx",
            "qy_qr",
            "ba_fe"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


