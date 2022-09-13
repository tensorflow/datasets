# wiki_source

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_source)
*   [Huggingface](https://huggingface.co/datasets/wiki_source)


## en-sv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_source/en-sv')
```

*   **Description**:

```
2 languages, total number of files: 132
total number of tokens: 1.80M
total number of sentence fragments: 78.36k
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 33283

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "sv"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


