# wrbsc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wrbsc)
*   [Huggingface](https://huggingface.co/datasets/wrbsc)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wrbsc')
```

*   **Description**:

```
WUT Relations Between Sentences Corpus contains 2827 pairs of related sentences.
Relationships are derived from Cross-document Structure Theory (CST), which enables multi-document summarization through identification of cross-document rhetorical relationships within a cluster of related documents.
Every relation was marked by at least 3 annotators.
```

*   **License**: Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2827

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relationship": {
        "num_classes": 16,
        "names": [
            "Krzy\u017cowanie_si\u0119",
            "T\u0142o_historyczne",
            "\u0179r\u00f3d\u0142o",
            "Dalsze_informacje",
            "Zawieranie",
            "Opis",
            "Uszczeg\u00f3\u0142owienie",
            "Parafraza",
            "Spe\u0142nienie",
            "Mowa_zale\u017cna",
            "Zmiana_pogl\u0105du",
            "Streszczenie",
            "To\u017csamo\u015b\u0107",
            "Sprzeczno\u015b\u0107",
            "Modalno\u015b\u0107",
            "Cytowanie"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


