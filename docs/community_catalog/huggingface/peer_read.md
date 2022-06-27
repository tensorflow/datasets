# peer_read

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/peer_read)
*   [Huggingface](https://huggingface.co/datasets/peer_read)


## parsed_pdfs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:peer_read/parsed_pdfs')
```

*   **Description**:

```
PearRead is a dataset of scientific peer reviews available to help researchers study this important artifact. The dataset consists of over 14K paper drafts and the corresponding accept/reject decisions in top-tier venues including ACL, NIPS and ICLR, as well as over 10K textual peer reviews written by experts for a subset of the papers.
```

*   **License**: Creative Commons Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 637
`'train'` | 11090
`'validation'` | 637

*   **Features**:

```json
{
    "name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "metadata": {
        "source": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "authors": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "emails": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "sections": {
            "feature": {
                "heading": {
                    "dtype": "string",
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
        },
        "references": {
            "feature": {
                "title": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "author": {
                    "feature": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "length": -1,
                    "id": null,
                    "_type": "Sequence"
                },
                "venue": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "citeRegEx": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "shortCiteRegEx": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "year": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "referenceMentions": {
            "feature": {
                "referenceID": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "context": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "startOffset": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "endOffset": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "year": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "abstractText": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "creator": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## reviews


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:peer_read/reviews')
```

*   **Description**:

```
PearRead is a dataset of scientific peer reviews available to help researchers study this important artifact. The dataset consists of over 14K paper drafts and the corresponding accept/reject decisions in top-tier venues including ACL, NIPS and ICLR, as well as over 10K textual peer reviews written by experts for a subset of the papers.
```

*   **License**: Creative Commons Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 637
`'train'` | 11090
`'validation'` | 637

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "conference": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "comments": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subjects": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "version": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date_of_submission": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "authors": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "accepted": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "abstract": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "histories": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "reviews": {
        "feature": {
            "date": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "other_keys": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "originality": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "comments": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "is_meta_review": {
                "dtype": "bool",
                "id": null,
                "_type": "Value"
            },
            "is_annotated": {
                "dtype": "bool",
                "id": null,
                "_type": "Value"
            },
            "recommendation": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "replicability": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "presentation_format": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "clarity": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "meaningful_comparison": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "substance": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "reviewer_confidence": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "soundness_correctness": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "appropriateness": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "impact": {
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


