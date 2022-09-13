# proto_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/proto_qa)
*   [Huggingface](https://huggingface.co/datasets/proto_qa)


## proto_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:proto_qa/proto_qa')
```

*   **Description**:

```
This dataset is for studying computational models trained to reason about prototypical situations. Using deterministic filtering a sampling from a larger set of all transcriptions was built. It contains 9789 instances where each instance represents a survey question from Family Feud game. Each instance exactly is a question, a set of answers, and a count associated with each answer.
Each line is a json dictionary, in which:
1. question - contains the question (in original and a normalized form)
2. answerstrings - contains the original answers provided by survey respondents (when available), along with the counts for each string. Because the FamilyFeud data has only cluster names rather than strings, those cluster names are included with 0 weight.
3. answer-clusters - lists clusters, with the count of each cluster and the strings included in that cluster. Each cluster is given a unique ID that can be linked to in the assessment files.
```

*   **License**: cc-by-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8782
`'validation'` | 980

*   **Features**:

```json
{
    "normalized-question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer-clusters": {
        "feature": {
            "count": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "clusterid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answers": {
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
    "answerstrings": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "totalcount": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## proto_qa_cs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:proto_qa/proto_qa_cs')
```

*   **Description**:

```
This dataset is for studying computational models trained to reason about prototypical situations. Using deterministic filtering a sampling from a larger set of all transcriptions was built. It contains 9789 instances where each instance represents a survey question from Family Feud game. Each instance exactly is a question, a set of answers, and a count associated with each answer.
Each line is a json dictionary, in which:
1. question - contains the question (in original and a normalized form)
2. answerstrings - contains the original answers provided by survey respondents (when available), along with the counts for each string. Because the FamilyFeud data has only cluster names rather than strings, those cluster names are included with 0 weight.
3. answer-clusters - lists clusters, with the count of each cluster and the strings included in that cluster. Each cluster is given a unique ID that can be linked to in the assessment files.
```

*   **License**: cc-by-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 52

*   **Features**:

```json
{
    "normalized-question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers-cleaned": {
        "feature": {
            "count": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "clusterid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answers": {
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
    "answerstrings": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "totalcount": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## proto_qa_cs_assessments


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:proto_qa/proto_qa_cs_assessments')
```

*   **Description**:

```
This dataset is for studying computational models trained to reason about prototypical situations. Using deterministic filtering a sampling from a larger set of all transcriptions was built. It contains 9789 instances where each instance represents a survey question from Family Feud game. Each instance exactly is a question, a set of answers, and a count associated with each answer.
Each line is a json dictionary, in which:
1. question - contains the question (in original and a normalized form)
2. answerstrings - contains the original answers provided by survey respondents (when available), along with the counts for each string. Because the FamilyFeud data has only cluster names rather than strings, those cluster names are included with 0 weight.
3. answer-clusters - lists clusters, with the count of each cluster and the strings included in that cluster. Each cluster is given a unique ID that can be linked to in the assessment files.
```

*   **License**: cc-by-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 52

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "assessments": {
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


