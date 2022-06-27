# trivia_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/trivia_qa)
*   [Huggingface](https://huggingface.co/datasets/trivia_qa)


## rc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/rc')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 17210
`'train'` | 138384
`'validation'` | 17944

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## rc.nocontext


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/rc.nocontext')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 17210
`'train'` | 138384
`'validation'` | 17944

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## unfiltered


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/unfiltered')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10832
`'train'` | 87622
`'validation'` | 11313

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## unfiltered.nocontext


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/unfiltered.nocontext')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10832
`'train'` | 87622
`'validation'` | 11313

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## rc.web


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/rc.web')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9509
`'train'` | 76496
`'validation'` | 9951

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## rc.web.nocontext


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/rc.web.nocontext')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9509
`'train'` | 76496
`'validation'` | 9951

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## unfiltered.web


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/unfiltered.web')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 0
`'train'` | 0
`'validation'` | 0

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## unfiltered.web.nocontext


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/unfiltered.web.nocontext')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 0
`'train'` | 0
`'validation'` | 0

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## rc.wikipedia


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/rc.wikipedia')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7701
`'train'` | 61888
`'validation'` | 7993

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## rc.wikipedia.nocontext


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/rc.wikipedia.nocontext')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7701
`'train'` | 61888
`'validation'` | 7993

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## unfiltered.wikipedia


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/unfiltered.wikipedia')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 0
`'train'` | 0
`'validation'` | 0

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## unfiltered.wikipedia.nocontext


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trivia_qa/unfiltered.wikipedia.nocontext')
```

*   **Description**:

```
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 0
`'train'` | 0
`'validation'` | 0

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_pages": {
        "feature": {
            "doc_source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "wiki_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "search_results": {
        "feature": {
            "description": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "filename": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rank": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "search_context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "normalized_aliases": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_matched_wiki_entity_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normalized_value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "value": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```


