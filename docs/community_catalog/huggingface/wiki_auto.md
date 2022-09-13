# wiki_auto

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_auto)
*   [Huggingface](https://huggingface.co/datasets/wiki_auto)


## manual


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_auto/manual')
```

*   **Description**:

```
WikiAuto provides a set of aligned sentences from English Wikipedia and Simple English Wikipedia
as a resource to train sentence simplification systems. The authors first crowd-sourced a set of manual alignments
between sentences in a subset of the Simple English Wikipedia and their corresponding versions in English Wikipedia
(this corresponds to the `manual` config), then trained a neural CRF system to predict these alignments.
The trained model was then applied to the other articles in Simple English Wikipedia with an English counterpart to
create a larger corpus of aligned sentences (corresponding to the `auto`, `auto_acl`, `auto_full_no_split`, and `auto_full_with_split`  configs here).
```

*   **License**: CC-BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 73249
`'test'` | 118074
`'train'` | 373801

*   **Features**:

```json
{
    "alignment_label": {
        "num_classes": 3,
        "names": [
            "notAligned",
            "aligned",
            "partialAligned"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "normal_sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simple_sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "normal_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simple_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gleu_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## auto_acl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_auto/auto_acl')
```

*   **Description**:

```
WikiAuto provides a set of aligned sentences from English Wikipedia and Simple English Wikipedia
as a resource to train sentence simplification systems. The authors first crowd-sourced a set of manual alignments
between sentences in a subset of the Simple English Wikipedia and their corresponding versions in English Wikipedia
(this corresponds to the `manual` config), then trained a neural CRF system to predict these alignments.
The trained model was then applied to the other articles in Simple English Wikipedia with an English counterpart to
create a larger corpus of aligned sentences (corresponding to the `auto`, `auto_acl`, `auto_full_no_split`, and `auto_full_with_split`  configs here).
```

*   **License**: CC-BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'full'` | 488332

*   **Features**:

```json
{
    "normal_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simple_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## auto


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_auto/auto')
```

*   **Description**:

```
WikiAuto provides a set of aligned sentences from English Wikipedia and Simple English Wikipedia
as a resource to train sentence simplification systems. The authors first crowd-sourced a set of manual alignments
between sentences in a subset of the Simple English Wikipedia and their corresponding versions in English Wikipedia
(this corresponds to the `manual` config), then trained a neural CRF system to predict these alignments.
The trained model was then applied to the other articles in Simple English Wikipedia with an English counterpart to
create a larger corpus of aligned sentences (corresponding to the `auto`, `auto_acl`, `auto_full_no_split`, and `auto_full_with_split`  configs here).
```

*   **License**: CC-BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'part_1'` | 125059
`'part_2'` | 13036

*   **Features**:

```json
{
    "example_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "normal": {
        "normal_article_id": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "normal_article_title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normal_article_url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "normal_article_content": {
            "feature": {
                "normal_sentence_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "normal_sentence": {
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
    "simple": {
        "simple_article_id": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "simple_article_title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "simple_article_url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "simple_article_content": {
            "feature": {
                "simple_sentence_id": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "simple_sentence": {
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
    "paragraph_alignment": {
        "feature": {
            "normal_paragraph_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "simple_paragraph_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "sentence_alignment": {
        "feature": {
            "normal_sentence_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "simple_sentence_id": {
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



## auto_full_no_split


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_auto/auto_full_no_split')
```

*   **Description**:

```
WikiAuto provides a set of aligned sentences from English Wikipedia and Simple English Wikipedia
as a resource to train sentence simplification systems. The authors first crowd-sourced a set of manual alignments
between sentences in a subset of the Simple English Wikipedia and their corresponding versions in English Wikipedia
(this corresponds to the `manual` config), then trained a neural CRF system to predict these alignments.
The trained model was then applied to the other articles in Simple English Wikipedia with an English counterpart to
create a larger corpus of aligned sentences (corresponding to the `auto`, `auto_acl`, `auto_full_no_split`, and `auto_full_with_split`  configs here).
```

*   **License**: CC-BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'full'` | 591994

*   **Features**:

```json
{
    "normal_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simple_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## auto_full_with_split


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_auto/auto_full_with_split')
```

*   **Description**:

```
WikiAuto provides a set of aligned sentences from English Wikipedia and Simple English Wikipedia
as a resource to train sentence simplification systems. The authors first crowd-sourced a set of manual alignments
between sentences in a subset of the Simple English Wikipedia and their corresponding versions in English Wikipedia
(this corresponds to the `manual` config), then trained a neural CRF system to predict these alignments.
The trained model was then applied to the other articles in Simple English Wikipedia with an English counterpart to
create a larger corpus of aligned sentences (corresponding to the `auto`, `auto_acl`, `auto_full_no_split`, and `auto_full_with_split`  configs here).
```

*   **License**: CC-BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'full'` | 483801

*   **Features**:

```json
{
    "normal_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simple_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


