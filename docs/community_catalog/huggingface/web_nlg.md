# web_nlg

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/web_nlg)
*   [Huggingface](https://huggingface.co/datasets/web_nlg)


## webnlg_challenge_2017


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_nlg/webnlg_challenge_2017')
```

*   **Description**:

```
The WebNLG challenge consists in mapping data to text. The training data consists
of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation
of these triples. For instance, given the 3 DBpedia triples shown in (a), the aim is to generate a text such as (b).

a. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
b. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 872
`'test'` | 4615
`'train'` | 6940

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lang": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dbpedia_links": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
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



## release_v1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_nlg/release_v1')
```

*   **Description**:

```
The WebNLG challenge consists in mapping data to text. The training data consists
of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation
of these triples. For instance, given the 3 DBpedia triples shown in (a), the aim is to generate a text such as (b).

a. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
b. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'full'` | 14237

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lang": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dbpedia_links": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
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



## release_v2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_nlg/release_v2')
```

*   **Description**:

```
The WebNLG challenge consists in mapping data to text. The training data consists
of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation
of these triples. For instance, given the 3 DBpedia triples shown in (a), the aim is to generate a text such as (b).

a. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
b. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 1619
`'test'` | 1600
`'train'` | 12876

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lang": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dbpedia_links": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
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



## release_v2_constrained


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_nlg/release_v2_constrained')
```

*   **Description**:

```
The WebNLG challenge consists in mapping data to text. The training data consists
of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation
of these triples. For instance, given the 3 DBpedia triples shown in (a), the aim is to generate a text such as (b).

a. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
b. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 1594
`'test'` | 1606
`'train'` | 12895

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lang": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dbpedia_links": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
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



## release_v2.1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_nlg/release_v2.1')
```

*   **Description**:

```
The WebNLG challenge consists in mapping data to text. The training data consists
of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation
of these triples. For instance, given the 3 DBpedia triples shown in (a), the aim is to generate a text such as (b).

a. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
b. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 1619
`'test'` | 1600
`'train'` | 12876

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lang": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dbpedia_links": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
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



## release_v2.1_constrained


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_nlg/release_v2.1_constrained')
```

*   **Description**:

```
The WebNLG challenge consists in mapping data to text. The training data consists
of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation
of these triples. For instance, given the 3 DBpedia triples shown in (a), the aim is to generate a text such as (b).

a. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
b. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 1594
`'test'` | 1606
`'train'` | 12895

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lang": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dbpedia_links": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
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



## release_v3.0_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_nlg/release_v3.0_en')
```

*   **Description**:

```
The WebNLG challenge consists in mapping data to text. The training data consists
of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation
of these triples. For instance, given the 3 DBpedia triples shown in (a), the aim is to generate a text such as (b).

a. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
b. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 1667
`'test'` | 5713
`'train'` | 13211

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lang": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dbpedia_links": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
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



## release_v3.0_ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_nlg/release_v3.0_ru')
```

*   **Description**:

```
The WebNLG challenge consists in mapping data to text. The training data consists
of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation
of these triples. For instance, given the 3 DBpedia triples shown in (a), the aim is to generate a text such as (b).

a. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
b. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 790
`'test'` | 3410
`'train'` | 5573

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "size": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "eid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_triple_sets": {
        "feature": {
            "otriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "modified_triple_sets": {
        "feature": {
            "mtriple_set": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "shape": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "shape_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lex": {
        "feature": {
            "comment": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lang": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dbpedia_links": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "links": {
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


