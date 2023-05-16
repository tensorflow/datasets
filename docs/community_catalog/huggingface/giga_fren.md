# giga_fren

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/giga_fren)
*   [Huggingface](https://huggingface.co/datasets/giga_fren)


## en-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:giga_fren/en-fr')
```

*   **Description**:

```
Giga-word corpus for French-English from WMT2010 collected by Chris Callison-Burch
2 languages, total number of files: 452
total number of tokens: 1.43G
total number of sentence fragments: 47.55M
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 22519904

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
            "fr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


