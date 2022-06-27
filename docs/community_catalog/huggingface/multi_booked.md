# multi_booked

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multi_booked)
*   [Huggingface](https://huggingface.co/datasets/multi_booked)


## ca


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_booked/ca')
```

*   **Description**:

```
MultiBooked is a corpus of Basque and Catalan Hotel Reviews Annotated for Aspect-level Sentiment Classification.

The corpora are compiled from hotel reviews taken mainly from booking.com. The corpora are in Kaf/Naf format, which is
an xml-style stand-off format that allows for multiple layers of annotation. Each review was sentence- and
word-tokenized and lemmatized using Freeling for Catalan and ixa-pipes for Basque. Finally, for each language two
annotators annotated opinion holders, opinion targets, and opinion expressions for each review, following the
guidelines set out in the OpeNER project.
```

*   **License**: CC-BY 3.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 567

*   **Features**:

```json
{
    "text": {
        "feature": {
            "wid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "sent": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "para": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "word": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "terms": {
        "feature": {
            "tid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lemma": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "morphofeat": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "pos": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "target": {
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
    "opinions": {
        "feature": {
            "oid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "opinion_holder_target": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "opinion_target_target": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "opinion_expression_polarity": {
                "num_classes": 4,
                "names": [
                    "StrongNegative",
                    "Negative",
                    "Positive",
                    "StrongPositive"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "opinion_expression_target": {
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
    }
}
```



## eu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_booked/eu')
```

*   **Description**:

```
MultiBooked is a corpus of Basque and Catalan Hotel Reviews Annotated for Aspect-level Sentiment Classification.

The corpora are compiled from hotel reviews taken mainly from booking.com. The corpora are in Kaf/Naf format, which is
an xml-style stand-off format that allows for multiple layers of annotation. Each review was sentence- and
word-tokenized and lemmatized using Freeling for Catalan and ixa-pipes for Basque. Finally, for each language two
annotators annotated opinion holders, opinion targets, and opinion expressions for each review, following the
guidelines set out in the OpeNER project.
```

*   **License**: CC-BY 3.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 343

*   **Features**:

```json
{
    "text": {
        "feature": {
            "wid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "sent": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "para": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "word": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "terms": {
        "feature": {
            "tid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "lemma": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "morphofeat": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "pos": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "target": {
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
    "opinions": {
        "feature": {
            "oid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "opinion_holder_target": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "opinion_target_target": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "opinion_expression_polarity": {
                "num_classes": 4,
                "names": [
                    "StrongNegative",
                    "Negative",
                    "Positive",
                    "StrongPositive"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "opinion_expression_target": {
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
    }
}
```


