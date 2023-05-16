# ofis_publik

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ofis_publik)
*   [Huggingface](https://huggingface.co/datasets/ofis_publik)


## br-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ofis_publik/br-fr')
```

*   **Description**:

```
Texts from the Ofis Publik ar Brezhoneg (Breton Language Board) provided by Francis Tyers
2 languages, total number of files: 278
total number of tokens: 2.12M
total number of sentence fragments: 0.13M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 63422

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
            "br",
            "fr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


