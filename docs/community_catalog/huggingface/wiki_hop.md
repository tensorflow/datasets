# wiki_hop

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_hop)
*   [Huggingface](https://huggingface.co/datasets/wiki_hop)


## original


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_hop/original')
```

*   **Description**:

```
WikiHop is open-domain and based on Wikipedia articles; the goal is to recover Wikidata information by hopping through documents. The goal is to answer text understanding queries by combining multiple facts that are spread across different documents.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 43738
`'validation'` | 5129

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
    },
    "annotations": {
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
    }
}
```



## masked


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_hop/masked')
```

*   **Description**:

```
WikiHop is open-domain and based on Wikipedia articles; the goal is to recover Wikidata information by hopping through documents. The goal is to answer text understanding queries by combining multiple facts that are spread across different documents.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 43738
`'validation'` | 5129

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
    },
    "annotations": {
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
    }
}
```


