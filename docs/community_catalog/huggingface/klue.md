# klue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/klue)
*   [Huggingface](https://huggingface.co/datasets/klue)


## ynat


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:klue/ynat')
```

*   **Description**:

```
KLUE (Korean Language Understanding Evaluation)
Korean Language Understanding Evaluation (KLUE) benchmark is a series of datasets to evaluate natural language
understanding capability of Korean language models. KLUE consists of 8 diverse and representative tasks, which are accessible
to anyone without any restrictions. With ethical considerations in mind, we deliberately design annotation guidelines to obtain
unambiguous annotations for all datasets. Futhermore, we build an evaluation system and carefully choose evaluations metrics
for every task, thus establishing fair comparison across Korean language models.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 45678
`'validation'` | 9107

*   **Features**:

```json
{
    "guid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 7,
        "names": [
            "IT\uacfc\ud559",
            "\uacbd\uc81c",
            "\uc0ac\ud68c",
            "\uc0dd\ud65c\ubb38\ud654",
            "\uc138\uacc4",
            "\uc2a4\ud3ec\uce20",
            "\uc815\uce58"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## sts


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:klue/sts')
```

*   **Description**:

```
KLUE (Korean Language Understanding Evaluation)
Korean Language Understanding Evaluation (KLUE) benchmark is a series of datasets to evaluate natural language
understanding capability of Korean language models. KLUE consists of 8 diverse and representative tasks, which are accessible
to anyone without any restrictions. With ethical considerations in mind, we deliberately design annotation guidelines to obtain
unambiguous annotations for all datasets. Futhermore, we build an evaluation system and carefully choose evaluations metrics
for every task, thus establishing fair comparison across Korean language models.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 11668
`'validation'` | 519

*   **Features**:

```json
{
    "guid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
    "labels": {
        "label": {
            "dtype": "float64",
            "id": null,
            "_type": "Value"
        },
        "real-label": {
            "dtype": "float64",
            "id": null,
            "_type": "Value"
        },
        "binary-label": {
            "num_classes": 2,
            "names": [
                "negative",
                "positive"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        }
    }
}
```



## nli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:klue/nli')
```

*   **Description**:

```
KLUE (Korean Language Understanding Evaluation)
Korean Language Understanding Evaluation (KLUE) benchmark is a series of datasets to evaluate natural language
understanding capability of Korean language models. KLUE consists of 8 diverse and representative tasks, which are accessible
to anyone without any restrictions. With ethical considerations in mind, we deliberately design annotation guidelines to obtain
unambiguous annotations for all datasets. Futhermore, we build an evaluation system and carefully choose evaluations metrics
for every task, thus establishing fair comparison across Korean language models.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 24998
`'validation'` | 3000

*   **Features**:

```json
{
    "guid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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



## ner


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:klue/ner')
```

*   **Description**:

```
KLUE (Korean Language Understanding Evaluation)
Korean Language Understanding Evaluation (KLUE) benchmark is a series of datasets to evaluate natural language
understanding capability of Korean language models. KLUE consists of 8 diverse and representative tasks, which are accessible
to anyone without any restrictions. With ethical considerations in mind, we deliberately design annotation guidelines to obtain
unambiguous annotations for all datasets. Futhermore, we build an evaluation system and carefully choose evaluations metrics
for every task, thus establishing fair comparison across Korean language models.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 21008
`'validation'` | 5000

*   **Features**:

```json
{
    "sentence": {
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
    "ner_tags": {
        "feature": {
            "num_classes": 13,
            "names": [
                "B-DT",
                "I-DT",
                "B-LC",
                "I-LC",
                "B-OG",
                "I-OG",
                "B-PS",
                "I-PS",
                "B-QT",
                "I-QT",
                "B-TI",
                "I-TI",
                "O"
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



## re


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:klue/re')
```

*   **Description**:

```
KLUE (Korean Language Understanding Evaluation)
Korean Language Understanding Evaluation (KLUE) benchmark is a series of datasets to evaluate natural language
understanding capability of Korean language models. KLUE consists of 8 diverse and representative tasks, which are accessible
to anyone without any restrictions. With ethical considerations in mind, we deliberately design annotation guidelines to obtain
unambiguous annotations for all datasets. Futhermore, we build an evaluation system and carefully choose evaluations metrics
for every task, thus establishing fair comparison across Korean language models.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 32470
`'validation'` | 7765

*   **Features**:

```json
{
    "guid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject_entity": {
        "word": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "start_idx": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "end_idx": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "object_entity": {
        "word": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "start_idx": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "end_idx": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "label": {
        "num_classes": 30,
        "names": [
            "no_relation",
            "org:dissolved",
            "org:founded",
            "org:place_of_headquarters",
            "org:alternate_names",
            "org:member_of",
            "org:members",
            "org:political/religious_affiliation",
            "org:product",
            "org:founded_by",
            "org:top_members/employees",
            "org:number_of_employees/members",
            "per:date_of_birth",
            "per:date_of_death",
            "per:place_of_birth",
            "per:place_of_death",
            "per:place_of_residence",
            "per:origin",
            "per:employee_of",
            "per:schools_attended",
            "per:alternate_names",
            "per:parents",
            "per:children",
            "per:siblings",
            "per:spouse",
            "per:other_family",
            "per:colleagues",
            "per:product",
            "per:religion",
            "per:title"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## dp


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:klue/dp')
```

*   **Description**:

```
KLUE (Korean Language Understanding Evaluation)
Korean Language Understanding Evaluation (KLUE) benchmark is a series of datasets to evaluate natural language
understanding capability of Korean language models. KLUE consists of 8 diverse and representative tasks, which are accessible
to anyone without any restrictions. With ethical considerations in mind, we deliberately design annotation guidelines to obtain
unambiguous annotations for all datasets. Futhermore, we build an evaluation system and carefully choose evaluations metrics
for every task, thus establishing fair comparison across Korean language models.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10000
`'validation'` | 2000

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "index": [
        {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        }
    ],
    "word_form": [
        {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    ],
    "lemma": [
        {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    ],
    "pos": [
        {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    ],
    "head": [
        {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        }
    ],
    "deprel": [
        {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    ]
}
```



## mrc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:klue/mrc')
```

*   **Description**:

```
KLUE (Korean Language Understanding Evaluation)
Korean Language Understanding Evaluation (KLUE) benchmark is a series of datasets to evaluate natural language
understanding capability of Korean language models. KLUE consists of 8 diverse and representative tasks, which are accessible
to anyone without any restrictions. With ethical considerations in mind, we deliberately design annotation guidelines to obtain
unambiguous annotations for all datasets. Futhermore, we build an evaluation system and carefully choose evaluations metrics
for every task, thus establishing fair comparison across Korean language models.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 17554
`'validation'` | 5841

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "news_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "guid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "is_impossible": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "question_type": {
        "dtype": "int32",
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



## wos


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:klue/wos')
```

*   **Description**:

```
KLUE (Korean Language Understanding Evaluation)
Korean Language Understanding Evaluation (KLUE) benchmark is a series of datasets to evaluate natural language
understanding capability of Korean language models. KLUE consists of 8 diverse and representative tasks, which are accessible
to anyone without any restrictions. With ethical considerations in mind, we deliberately design annotation guidelines to obtain
unambiguous annotations for all datasets. Futhermore, we build an evaluation system and carefully choose evaluations metrics
for every task, thus establishing fair comparison across Korean language models.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8000
`'validation'` | 1000

*   **Features**:

```json
{
    "guid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domains": [
        {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    ],
    "dialogue": [
        {
            "role": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "state": [
                {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            ]
        }
    ]
}
```


