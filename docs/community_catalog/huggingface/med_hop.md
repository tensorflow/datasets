# med_hop

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/med_hop)
*   [Huggingface](https://huggingface.co/datasets/med_hop)


## original


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:med_hop/original')
```

*   **Description**:

```
MedHop is based on research paper abstracts from PubMed, and the queries are about interactions between pairs of drugs. The correct answer has to be inferred by combining information from a chain of reactions of drugs and proteins.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1620
`'validation'` | 342

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "supports": {
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



## masked


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:med_hop/masked')
```

*   **Description**:

```
MedHop iss based on research paper abstracts from PubMed, and the queries are about interactions between pairs of drugs. The correct answer has to be inferred by combining information from a chain of reactions of drugs and proteins.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1620
`'validation'` | 342

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "supports": {
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


