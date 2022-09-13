# exams

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/exams)
*   [Huggingface](https://huggingface.co/datasets/exams)


## alignments


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/alignments')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'full'` | 10834

*   **Features**:

```json
{
    "source_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target_id_list": {
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



## multilingual


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/multilingual')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 13510
`'train'` | 7961
`'validation'` | 2672

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## multilingual_with_para


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/multilingual_with_para')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 13510
`'train'` | 7961
`'validation'` | 2672

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_test


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_test')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 19736

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_test


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_test')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 19736

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_bg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_bg')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2344
`'validation'` | 593

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_bg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_bg')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2344
`'validation'` | 593

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_hr')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2341
`'validation'` | 538

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_hr')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2341
`'validation'` | 538

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_hu')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1731
`'validation'` | 536

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_hu')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1731
`'validation'` | 536

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_it')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1010
`'validation'` | 246

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_it')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1010
`'validation'` | 246

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_mk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_mk')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1665
`'validation'` | 410

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_mk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_mk')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1665
`'validation'` | 410

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_pl')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1577
`'validation'` | 394

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_pl')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1577
`'validation'` | 394

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_pt')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 740
`'validation'` | 184

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_pt')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 740
`'validation'` | 184

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_sq')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1194
`'validation'` | 311

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_sq')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1194
`'validation'` | 311

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_sr')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1323
`'validation'` | 314

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_sr')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1323
`'validation'` | 314

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_tr')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1571
`'validation'` | 393

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_tr')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1571
`'validation'` | 393

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_vi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_vi')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1955
`'validation'` | 488

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## crosslingual_with_para_vi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:exams/crosslingual_with_para_vi')
```

*   **Description**:

```
EXAMS is a benchmark dataset for multilingual and cross-lingual question answering from high school examinations.
It consists of more than 24,000 high-quality high school exam questions in 16 languages,
covering 8 language families and 24 school subjects from Natural Sciences and Social Sciences, among others.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1955
`'validation'` | 488

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "stem": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "choices": {
            "feature": {
                "text": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "label": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "para": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "info": {
        "grade": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "subject": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "language": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```


