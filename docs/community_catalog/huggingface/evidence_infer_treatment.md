# evidence_infer_treatment

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/evidence_infer_treatment)
*   [Huggingface](https://huggingface.co/datasets/evidence_infer_treatment)


## 2.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:evidence_infer_treatment/2.0')
```

*   **Description**:

```
Data and code from our "Inferring Which Medical Treatments Work from Reports of Clinical Trials", NAACL 2019. This work concerns inferring the results reported in clinical trials from text.

The dataset consists of biomedical articles describing randomized control trials (RCTs) that compare multiple treatments. Each of these articles will have multiple questions, or 'prompts' associated with them. These prompts will ask about the relationship between an intervention and comparator with respect to an outcome, as reported in the trial. For example, a prompt may ask about the reported effects of aspirin as compared to placebo on the duration of headaches. For the sake of this task, we assume that a particular article will report that the intervention of interest either significantly increased, significantly decreased or had significant effect on the outcome, relative to the comparator.

The dataset could be used for automatic data extraction of the results of a given RCT. This would enable readers to discover the effectiveness of different treatments without needing to read the paper.
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 334
`'train'` | 2690
`'validation'` | 340

*   **Features**:

```json
{
    "Text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "PMCID": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Prompts": {
        "feature": {
            "PromptID": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "PMCID": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "Outcome": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Intervention": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Comparator": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Annotations": {
                "feature": {
                    "UserID": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "PromptID": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "PMCID": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "Valid Label": {
                        "dtype": "bool",
                        "id": null,
                        "_type": "Value"
                    },
                    "Valid Reasoning": {
                        "dtype": "bool",
                        "id": null,
                        "_type": "Value"
                    },
                    "Label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Annotations": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Label Code": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "In Abstract": {
                        "dtype": "bool",
                        "id": null,
                        "_type": "Value"
                    },
                    "Evidence Start": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "Evidence End": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    }
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



## 1.1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:evidence_infer_treatment/1.1')
```

*   **Description**:

```
Data and code from our "Inferring Which Medical Treatments Work from Reports of Clinical Trials", NAACL 2019. This work concerns inferring the results reported in clinical trials from text.

The dataset consists of biomedical articles describing randomized control trials (RCTs) that compare multiple treatments. Each of these articles will have multiple questions, or 'prompts' associated with them. These prompts will ask about the relationship between an intervention and comparator with respect to an outcome, as reported in the trial. For example, a prompt may ask about the reported effects of aspirin as compared to placebo on the duration of headaches. For the sake of this task, we assume that a particular article will report that the intervention of interest either significantly increased, significantly decreased or had significant effect on the outcome, relative to the comparator.

The dataset could be used for automatic data extraction of the results of a given RCT. This would enable readers to discover the effectiveness of different treatments without needing to read the paper.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 240
`'train'` | 1931
`'validation'` | 248

*   **Features**:

```json
{
    "Text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "PMCID": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Prompts": {
        "feature": {
            "PromptID": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "PMCID": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "Outcome": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Intervention": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Comparator": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "Annotations": {
                "feature": {
                    "UserID": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "PromptID": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "PMCID": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "Valid Label": {
                        "dtype": "bool",
                        "id": null,
                        "_type": "Value"
                    },
                    "Valid Reasoning": {
                        "dtype": "bool",
                        "id": null,
                        "_type": "Value"
                    },
                    "Label": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Annotations": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Label Code": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "In Abstract": {
                        "dtype": "bool",
                        "id": null,
                        "_type": "Value"
                    },
                    "Evidence Start": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "Evidence End": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    }
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


