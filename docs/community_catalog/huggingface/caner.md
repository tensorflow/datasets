# caner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/caner)
*   [Huggingface](https://huggingface.co/datasets/caner)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:caner')
```

*   **Description**:

```
Classical Arabic Named Entity Recognition corpus as a new corpus of tagged data that can be useful for handling the issues in recognition of Arabic named entities.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 258240

*   **Features**:

```json
{
    "token": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ner_tag": {
        "num_classes": 21,
        "names": [
            "Allah",
            "Book",
            "Clan",
            "Crime",
            "Date",
            "Day",
            "Hell",
            "Loc",
            "Meas",
            "Mon",
            "Month",
            "NatOb",
            "Number",
            "O",
            "Org",
            "Para",
            "Pers",
            "Prophet",
            "Rlig",
            "Sect",
            "Time"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


