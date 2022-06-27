# qa4mre

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/qa4mre)
*   [Huggingface](https://huggingface.co/datasets/qa4mre)


## 2011.main.DE


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2011.main.DE')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 120

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2011.main.EN


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2011.main.EN')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 120

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2011.main.ES


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2011.main.ES')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 120

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2011.main.IT


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2011.main.IT')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 120

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2011.main.RO


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2011.main.RO')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 120

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2012.main.AR


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2012.main.AR')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 160

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2012.main.BG


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2012.main.BG')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 160

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2012.main.DE


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2012.main.DE')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 160

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2012.main.EN


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2012.main.EN')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 160

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2012.main.ES


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2012.main.ES')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 160

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2012.main.IT


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2012.main.IT')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 160

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2012.main.RO


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2012.main.RO')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 160

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2012.alzheimers.EN


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2012.alzheimers.EN')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 40

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2013.main.AR


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2013.main.AR')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 284

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2013.main.BG


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2013.main.BG')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 284

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2013.main.EN


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2013.main.EN')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 284

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2013.main.ES


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2013.main.ES')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 284

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2013.main.RO


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2013.main.RO')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 284

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2013.alzheimers.EN


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2013.alzheimers.EN')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 40

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2013.entrance_exam.EN


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qa4mre/2013.entrance_exam.EN')
```

*   **Description**:

```
QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in 
question answering and reading comprehension. The dataset contains a supporting 
passage and a set of questions corresponding to the passage. Multiple options 
for answers are provided for each question, of which only one is correct. The 
training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on 
alzheimers data, and the other on entrance exams data.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 46

*   **Features**:

```json
{
    "topic_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_options": {
        "feature": {
            "answer_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_str": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


