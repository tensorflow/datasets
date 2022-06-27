# arxiv_dataset

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/arxiv_dataset)
*   [Huggingface](https://huggingface.co/datasets/arxiv_dataset)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:arxiv_dataset')
```

*   **Description**:

```
A dataset of 1.7 million arXiv articles for applications like trend analysis, paper recommender engines, category prediction, co-citation networks, knowledge graph construction and semantic search interfaces.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1796911

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "submitter": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "authors": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "comments": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "journal-ref": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "doi": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "report-no": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "categories": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "license": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstract": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "update_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


