# scitldr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/scitldr)
*   [Huggingface](https://huggingface.co/datasets/scitldr)


## Abstract


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scitldr/Abstract')
```

*   **Description**:

```
A new multi-target dataset of 5.4K TLDRs over 3.2K papers.
SCITLDR contains both author-written and expert-derived TLDRs,
where the latter are collected using a novel annotation protocol
that produces high-quality summaries while minimizing annotation burden.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 618
`'train'` | 1992
`'validation'` | 619

*   **Features**:

```json
{
    "source": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "source_labels": {
        "feature": {
            "num_classes": 2,
            "names": [
                "non-oracle",
                "oracle"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "rouge_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "paper_id": {
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
}
```



## AIC


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scitldr/AIC')
```

*   **Description**:

```
A new multi-target dataset of 5.4K TLDRs over 3.2K papers.
SCITLDR contains both author-written and expert-derived TLDRs,
where the latter are collected using a novel annotation protocol
that produces high-quality summaries while minimizing annotation burden.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 618
`'train'` | 1992
`'validation'` | 619

*   **Features**:

```json
{
    "source": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "source_labels": {
        "feature": {
            "num_classes": 2,
            "names": [
                0,
                1
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "rouge_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "paper_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ic": {
        "dtype": "bool_",
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
}
```



## FullText


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scitldr/FullText')
```

*   **Description**:

```
A new multi-target dataset of 5.4K TLDRs over 3.2K papers.
SCITLDR contains both author-written and expert-derived TLDRs,
where the latter are collected using a novel annotation protocol
that produces high-quality summaries while minimizing annotation burden.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 618
`'train'` | 1992
`'validation'` | 619

*   **Features**:

```json
{
    "source": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "source_labels": {
        "feature": {
            "num_classes": 2,
            "names": [
                "non-oracle",
                "oracle"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "rouge_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "paper_id": {
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
}
```


