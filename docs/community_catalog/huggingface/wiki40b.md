# wiki40b

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki40b)
*   [Huggingface](https://huggingface.co/datasets/wiki40b)


## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki40b/en')
```

*   **Description**:

```
Clean-up text for 40+ Wikipedia languages editions of pages
correspond to entities. The datasets have train/dev/test splits per language.
The dataset is cleaned up by page filtering to remove disambiguation pages,
redirect pages, deleted pages, and non-entity pages. Each example contains the
wikidata id of the entity, and the full Wikipedia article after page processing
that removes non-content sections and structured objects.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 162274
`'train'` | 2926536
`'validation'` | 163597

*   **Features**:

```json
{
    "wikidata_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "version_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


