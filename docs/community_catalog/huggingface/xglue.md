# xglue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/xglue)
*   [Huggingface](https://huggingface.co/datasets/xglue)


## ner


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/ner')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.de'` | 3007
`'test.en'` | 3454
`'test.es'` | 1523
`'test.nl'` | 5202
`'train'` | 14042
`'validation.de'` | 2874
`'validation.en'` | 3252
`'validation.es'` | 1923
`'validation.nl'` | 2895

*   **Features**:

```json
{
    "words": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner": {
        "feature": {
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
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



## pos


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/pos')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.ar'` | 679
`'test.bg'` | 1115
`'test.de'` | 976
`'test.el'` | 455
`'test.en'` | 2076
`'test.es'` | 425
`'test.fr'` | 415
`'test.hi'` | 1683
`'test.it'` | 481
`'test.nl'` | 595
`'test.pl'` | 2214
`'test.ru'` | 600
`'test.th'` | 497
`'test.tr'` | 982
`'test.ur'` | 534
`'test.vi'` | 799
`'test.zh'` | 499
`'train'` | 25376
`'validation.ar'` | 908
`'validation.bg'` | 1114
`'validation.de'` | 798
`'validation.el'` | 402
`'validation.en'` | 2001
`'validation.es'` | 1399
`'validation.fr'` | 1475
`'validation.hi'` | 1658
`'validation.it'` | 563
`'validation.nl'` | 717
`'validation.pl'` | 2214
`'validation.ru'` | 578
`'validation.th'` | 497
`'validation.tr'` | 987
`'validation.ur'` | 551
`'validation.vi'` | 799
`'validation.zh'` | 499

*   **Features**:

```json
{
    "words": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pos": {
        "feature": {
            "num_classes": 17,
            "names": [
                "ADJ",
                "ADP",
                "ADV",
                "AUX",
                "CCONJ",
                "DET",
                "INTJ",
                "NOUN",
                "NUM",
                "PART",
                "PRON",
                "PROPN",
                "PUNCT",
                "SCONJ",
                "SYM",
                "VERB",
                "X"
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



## mlqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/mlqa')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.ar'` | 5335
`'test.de'` | 4517
`'test.en'` | 11590
`'test.es'` | 5253
`'test.hi'` | 4918
`'test.vi'` | 5495
`'test.zh'` | 5137
`'train'` | 87599
`'validation.ar'` | 517
`'validation.de'` | 512
`'validation.en'` | 1148
`'validation.es'` | 500
`'validation.hi'` | 507
`'validation.vi'` | 511
`'validation.zh'` | 504

*   **Features**:

```json
{
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## nc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/nc')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.de'` | 10000
`'test.en'` | 10000
`'test.es'` | 10000
`'test.fr'` | 10000
`'test.ru'` | 10000
`'train'` | 100000
`'validation.de'` | 10000
`'validation.en'` | 10000
`'validation.es'` | 10000
`'validation.fr'` | 10000
`'validation.ru'` | 10000

*   **Features**:

```json
{
    "news_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "news_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "news_category": {
        "num_classes": 10,
        "names": [
            "foodanddrink",
            "sports",
            "travel",
            "finance",
            "lifestyle",
            "news",
            "entertainment",
            "health",
            "video",
            "autos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## xnli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/xnli')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.ar'` | 5010
`'test.bg'` | 5010
`'test.de'` | 5010
`'test.el'` | 5010
`'test.en'` | 5010
`'test.es'` | 5010
`'test.fr'` | 5010
`'test.hi'` | 5010
`'test.ru'` | 5010
`'test.sw'` | 5010
`'test.th'` | 5010
`'test.tr'` | 5010
`'test.ur'` | 5010
`'test.vi'` | 5010
`'test.zh'` | 5010
`'train'` | 392702
`'validation.ar'` | 2490
`'validation.bg'` | 2490
`'validation.de'` | 2490
`'validation.el'` | 2490
`'validation.en'` | 2490
`'validation.es'` | 2490
`'validation.fr'` | 2490
`'validation.hi'` | 2490
`'validation.ru'` | 2490
`'validation.sw'` | 2490
`'validation.th'` | 2490
`'validation.tr'` | 2490
`'validation.ur'` | 2490
`'validation.vi'` | 2490
`'validation.zh'` | 2490

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## paws-x


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/paws-x')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.de'` | 2000
`'test.en'` | 2000
`'test.es'` | 2000
`'test.fr'` | 2000
`'train'` | 49401
`'validation.de'` | 2000
`'validation.en'` | 2000
`'validation.es'` | 2000
`'validation.fr'` | 2000

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "different",
            "same"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## qadsm


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/qadsm')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.de'` | 10000
`'test.en'` | 10000
`'test.fr'` | 10000
`'train'` | 100000
`'validation.de'` | 10000
`'validation.en'` | 10000
`'validation.fr'` | 10000

*   **Features**:

```json
{
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ad_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ad_description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relevance_label": {
        "num_classes": 2,
        "names": [
            "Bad",
            "Good"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## wpr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/wpr')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.de'` | 9997
`'test.en'` | 10004
`'test.es'` | 10006
`'test.fr'` | 10020
`'test.it'` | 10001
`'test.pt'` | 10015
`'test.zh'` | 9999
`'train'` | 99997
`'validation.de'` | 10004
`'validation.en'` | 10008
`'validation.es'` | 10004
`'validation.fr'` | 10005
`'validation.it'` | 10003
`'validation.pt'` | 10001
`'validation.zh'` | 10002

*   **Features**:

```json
{
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "web_page_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "web_page_snippet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relavance_label": {
        "num_classes": 5,
        "names": [
            "Bad",
            "Fair",
            "Good",
            "Excellent",
            "Perfect"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## qam


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/qam')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.de'` | 10000
`'test.en'` | 10000
`'test.fr'` | 10000
`'train'` | 100000
`'validation.de'` | 10000
`'validation.en'` | 10000
`'validation.fr'` | 10000

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## qg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/qg')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.de'` | 10000
`'test.en'` | 10000
`'test.es'` | 10000
`'test.fr'` | 10000
`'test.it'` | 10000
`'test.pt'` | 10000
`'train'` | 100000
`'validation.de'` | 10000
`'validation.en'` | 10000
`'validation.es'` | 10000
`'validation.fr'` | 10000
`'validation.it'` | 10000
`'validation.pt'` | 10000

*   **Features**:

```json
{
    "answer_passage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ntg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xglue/ntg')
```

*   **Description**:

```
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.de'` | 10000
`'test.en'` | 10000
`'test.es'` | 10000
`'test.fr'` | 10000
`'test.ru'` | 10000
`'train'` | 300000
`'validation.de'` | 10000
`'validation.en'` | 10000
`'validation.es'` | 10000
`'validation.fr'` | 10000
`'validation.ru'` | 10000

*   **Features**:

```json
{
    "news_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "news_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


