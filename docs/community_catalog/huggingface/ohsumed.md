# ohsumed

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ohsumed)
*   [Huggingface](https://huggingface.co/datasets/ohsumed)


## ohsumed


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ohsumed/ohsumed')
```

*   **Description**:

```
The OHSUMED test collection is a set of 348,566 references from
MEDLINE, the on-line medical information database, consisting of
titles and/or abstracts from 270 medical journals over a five-year
period (1987-1991). The available fields are title, abstract, MeSH
indexing terms, author, source, and publication type.
```

*   **License**: CC BY-NC 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 293855
`'train'` | 54709

*   **Features**:

```json
{
    "seq_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "medline_ui": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "mesh_terms": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "publication_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstract": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "author": {
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


