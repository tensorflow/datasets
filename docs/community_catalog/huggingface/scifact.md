# scifact

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/scifact)
*   [Huggingface](https://huggingface.co/datasets/scifact)


## corpus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scifact/corpus')
```

*   **Description**:

```
SciFact, a dataset of 1.4K expert-written scientific claims paired with evidence-containing abstracts, and annotated with labels and rationales.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5183

*   **Features**:

```json
{
    "doc_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstract": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "structured": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    }
}
```



## claims


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scifact/claims')
```

*   **Description**:

```
SciFact, a dataset of 1.4K expert-written scientific claims paired with evidence-containing abstracts, and annotated with labels and rationales.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 300
`'train'` | 1261
`'validation'` | 450

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "claim": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "evidence_doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "evidence_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "evidence_sentences": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "cited_doc_ids": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


