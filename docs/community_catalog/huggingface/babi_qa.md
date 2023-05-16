# babi_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/babi_qa)
*   [Huggingface](https://huggingface.co/datasets/babi_qa)


## en-qa1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa1')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa2')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa3')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa4')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa5')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa6


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa6')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa7')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa8')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa9


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa9')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa10


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa10')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa11')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa12


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa12')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa13


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa13')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa14


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa14')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa15')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 250

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa16


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa16')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa17')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 125

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa18


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa18')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 199
`'train'` | 198

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa19


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa19')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-qa20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-qa20')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 93
`'train'` | 94

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa1')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa2')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa3')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 167
`'train'` | 167

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa4')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa5')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa6


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa6')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa7')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa8')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa9


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa9')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa10


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa10')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa11')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa12


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa12')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa13


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa13')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 125

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa14


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa14')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa15')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 250

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa16


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa16')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa17')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 125

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa18


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa18')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 198
`'train'` | 198

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa19


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa19')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-qa20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-qa20')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 94
`'train'` | 93

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa1')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa2')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa3')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa4')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa5')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa6


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa6')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa7')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa8')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa9


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa9')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa10


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa10')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa11')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa12


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa12')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa13


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa13')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa14


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa14')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa15')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 2500

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa16


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa16')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa17')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 1250

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa18


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa18')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 199
`'train'` | 1978

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa19


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa19')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-10k-qa20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-10k-qa20')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 93
`'train'` | 933

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa1')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa2')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa3')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa4')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 900
`'validation'` | 100

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa5')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa6


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa6')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa7')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa8')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa9


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa9')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa10


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa10')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa11')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa12


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa12')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa13


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa13')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa14


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa14')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 180
`'validation'` | 20

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa15')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 225
`'validation'` | 25

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa16


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa16')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 900
`'validation'` | 100

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa17')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 113
`'validation'` | 12

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa18


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa18')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 199
`'train'` | 179
`'validation'` | 19

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa19


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa19')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 900
`'validation'` | 100

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-qa20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-qa20')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 93
`'train'` | 85
`'validation'` | 9

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa1')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa2')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa3')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa4')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 9000
`'validation'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa5')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa6


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa6')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa7')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa8')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa9


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa9')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa10


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa10')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa11')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa12


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa12')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa13


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa13')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa14


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa14')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 1800
`'validation'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa15')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 2250
`'validation'` | 250

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa16


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa16')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 9000
`'validation'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa17')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 1125
`'validation'` | 125

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa18


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa18')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 199
`'train'` | 1781
`'validation'` | 197

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa19


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa19')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 9000
`'validation'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-valid-10k-qa20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/en-valid-10k-qa20')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 93
`'train'` | 840
`'validation'` | 93

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa1')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa2')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa3')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 167
`'train'` | 1667

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa4')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa5')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa6


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa6')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa7')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa8')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa9


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa9')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa10


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa10')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa11')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa12


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa12')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa13


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa13')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 1250

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa14


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa14')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa15')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 2500

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa16


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa16')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa17')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 1250

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa18


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa18')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 198
`'train'` | 1977

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa19


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa19')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hn-10k-qa20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/hn-10k-qa20')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 94
`'train'` | 934

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa1')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa2')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa3')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa4')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa5')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa6


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa6')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa7')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa8')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa9


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa9')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa10


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa10')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa11')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa12


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa12')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa13


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa13')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa14


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa14')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 200

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa15')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 250

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa16


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa16')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa17')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 125

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa18


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa18')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 199
`'train'` | 198

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa19


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa19')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 1000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-qa20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-qa20')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 93
`'train'` | 94

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa1')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa2')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa3')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa4')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa5')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa6


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa6')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa7


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa7')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa8


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa8')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa9


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa9')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa10


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa10')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa11')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa12


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa12')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa13


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa13')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa14


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa14')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 200
`'train'` | 2000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa15')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 2500

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa16


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa16')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa17')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 125
`'train'` | 1250

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa18


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa18')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 199
`'train'` | 1978

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa19


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa19')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10000

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## shuffled-10k-qa20


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:babi_qa/shuffled-10k-qa20')
```

*   **Description**:

```
The (20) QA bAbI tasks are a set of proxy tasks that evaluate reading
comprehension via question answering. Our tasks measure understanding
in several ways: whether a system is able to answer questions via chaining facts,
simple induction, deduction and many more. The tasks are designed to be prerequisites
for any system that aims to be capable of conversing with a human.
The aim is to classify these tasks into skill sets,so that researchers
can identify (and then rectify)the failings of their systems.
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 93
`'train'` | 933

*   **Features**:

```json
{
    "story": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 2,
                "names": [
                    "context",
                    "question"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "supporting_ids": {
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


