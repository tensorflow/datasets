# kilt_tasks

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kilt_tasks)
*   [Huggingface](https://huggingface.co/datasets/kilt_tasks)


## triviaqa_support_only


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/triviaqa_support_only')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6586
`'train'` | 61844
`'validation'` | 5359

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## fever


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/fever')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10100
`'train'` | 104966
`'validation'` | 10444

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## aidayago2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/aidayago2')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4463
`'train'` | 18395
`'validation'` | 4784

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## wned


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/wned')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3376
`'validation'` | 3396

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## cweb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/cweb')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5543
`'validation'` | 5599

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## trex


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/trex')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 2284168
`'validation'` | 5000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## structured_zeroshot


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/structured_zeroshot')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4966
`'train'` | 147909
`'validation'` | 3724

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## nq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/nq')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1444
`'train'` | 87372
`'validation'` | 2837

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## hotpotqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/hotpotqa')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5569
`'train'` | 88869
`'validation'` | 5600

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## eli5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/eli5')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 600
`'train'` | 272634
`'validation'` | 1507

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```



## wow


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kilt_tasks/wow')
```

*   **Description**:

```
KILT tasks training and evaluation data.
- [FEVER](https://fever.ai) | Fact Checking | fever
- [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) | Entity Linking | aidayago2
- [WNED-WIKI](https://github.com/U-Alberta/wned) | Entity Linking | wned
- [WNED-CWEB](https://github.com/U-Alberta/wned) | Entity Linking | cweb
- [T-REx](https://hadyelsahar.github.io/t-rex) | Slot Filling | trex
- [Zero-Shot RE](http://nlp.cs.washington.edu/zeroshot) | Slot Filling | structured_zeroshot
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Open Domain QA  | nq
- [HotpotQA](https://hotpotqa.github.io) | Open Domain QA | hotpotqa
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa) | Open Domain QA | triviaqa
- [ELI5](https://facebookresearch.github.io/ELI5/explore.html) | Open Domain QA | eli5
- [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia) | Dialogue | wow

To finish linking TriviaQA questions to the IDs provided, follow the instructions [here](http://github.com/huggingface/datasets/datasets/kilt_tasks/README.md).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2944
`'train'` | 63734
`'validation'` | 3054

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "left_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "mention": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "right_context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "partial_evidence": [
            {
                "start_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "end_paragraph_id": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "section": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "wikipedia_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "meta": {
                    "evidence_span": [
                        {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        }
                    ]
                }
            }
        ],
        "obj_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "sub_surface": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "subj_aliases": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ],
        "template_questions": [
            {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        ]
    },
    "output": [
        {
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meta": {
                "score": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "provenance": [
                {
                    "bleu_score": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "start_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_character": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end_paragraph_id": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "meta": {
                        "fever_page_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "fever_sentence_id": {
                            "dtype": "int32",
                            "id": null,
                            "_type": "Value"
                        },
                        "annotation_id": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "yes_no_answer": {
                            "dtype": "string",
                            "id": null,
                            "_type": "Value"
                        },
                        "evidence_span": [
                            {
                                "dtype": "string",
                                "id": null,
                                "_type": "Value"
                            }
                        ]
                    },
                    "section": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "title": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "wikipedia_id": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                }
            ]
        }
    ]
}
```


