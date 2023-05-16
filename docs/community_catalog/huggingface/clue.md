# clue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/clue)
*   [Huggingface](https://huggingface.co/datasets/clue)


## afqmc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/afqmc')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3861
`'train'` | 34334
`'validation'` | 4316

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
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## tnews


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/tnews')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 53360
`'validation'` | 10000

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 15,
        "names": [
            "100",
            "101",
            "102",
            "103",
            "104",
            "106",
            "107",
            "108",
            "109",
            "110",
            "112",
            "113",
            "114",
            "115",
            "116"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## iflytek


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/iflytek')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2600
`'train'` | 12133
`'validation'` | 2599

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 119,
        "names": [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "40",
            "41",
            "42",
            "43",
            "44",
            "45",
            "46",
            "47",
            "48",
            "49",
            "50",
            "51",
            "52",
            "53",
            "54",
            "55",
            "56",
            "57",
            "58",
            "59",
            "60",
            "61",
            "62",
            "63",
            "64",
            "65",
            "66",
            "67",
            "68",
            "69",
            "70",
            "71",
            "72",
            "73",
            "74",
            "75",
            "76",
            "77",
            "78",
            "79",
            "80",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "89",
            "90",
            "91",
            "92",
            "93",
            "94",
            "95",
            "96",
            "97",
            "98",
            "99",
            "100",
            "101",
            "102",
            "103",
            "104",
            "105",
            "106",
            "107",
            "108",
            "109",
            "110",
            "111",
            "112",
            "113",
            "114",
            "115",
            "116",
            "117",
            "118"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## cmnli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/cmnli')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 13880
`'train'` | 391783
`'validation'` | 12241

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
        "num_classes": 3,
        "names": [
            "neutral",
            "entailment",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## cluewsc2020


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/cluewsc2020')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2574
`'train'` | 1244
`'validation'` | 304

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "true",
            "false"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "target": {
        "span1_text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "span2_text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "span1_index": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "span2_index": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## csl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/csl')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3000
`'train'` | 20000
`'validation'` | 3000

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "corpus_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "abst": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "keyword": {
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



## cmrc2018


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/cmrc2018')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 10142
`'trial'` | 1002
`'validation'` | 3219

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
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
```



## drcd


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/drcd')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3493
`'train'` | 26936
`'validation'` | 3524

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
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
```



## chid


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/chid')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3447
`'train'` | 84709
`'validation'` | 3218

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "content": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "candidate_id": {
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
```



## c3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/c3')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1625
`'train'` | 11869
`'validation'` | 3816

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ocnli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/ocnli')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3000
`'train'` | 50437
`'validation'` | 2950

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
        "num_classes": 3,
        "names": [
            "neutral",
            "entailment",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## diagnostics


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clue/diagnostics')
```

*   **Description**:

```
CLUE, A Chinese Language Understanding Evaluation Benchmark
(https://www.cluebenchmarks.com/) is a collection of resources for training,
evaluating, and analyzing Chinese language understanding systems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 514

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
        "num_classes": 3,
        "names": [
            "neutral",
            "entailment",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


