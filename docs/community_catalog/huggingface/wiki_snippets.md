# wiki_snippets

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_snippets)
*   [Huggingface](https://huggingface.co/datasets/wiki_snippets)


## wiki40b_en_100_0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_snippets/wiki40b_en_100_0')
```

*   **Description**:

```
Wikipedia version split into plain text snippets for dense semantic indexing.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 17553713

*   **Features**:

```json
{
    "_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "datasets_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "wiki_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "start_paragraph": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "start_character": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end_paragraph": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end_character": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "article_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "section_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "passage_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wikipedia_en_100_0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_snippets/wikipedia_en_100_0')
```

*   **Description**:

```
Wikipedia version split into plain text snippets for dense semantic indexing.
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 33849898

*   **Features**:

```json
{
    "_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "datasets_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "wiki_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "start_paragraph": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "start_character": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end_paragraph": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end_character": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "article_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "section_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "passage_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


