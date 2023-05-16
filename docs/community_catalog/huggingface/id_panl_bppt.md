# id_panl_bppt

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/id_panl_bppt)
*   [Huggingface](https://huggingface.co/datasets/id_panl_bppt)


## id_panl_bppt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:id_panl_bppt/id_panl_bppt')
```

*   **Description**:

```
Parallel Text Corpora for Multi-Domain Translation System created by BPPT (Indonesian Agency for the Assessment and
Application of Technology) for PAN Localization Project (A Regional Initiative to Develop Local Language Computing
Capacity in Asia). The dataset contains around 24K sentences divided in 4 difference topics (Economic, international,
Science and Technology and Sport).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 24021

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
            "id"
        ],
        "id": null,
        "_type": "Translation"
    },
    "topic": {
        "num_classes": 4,
        "names": [
            "Economy",
            "International",
            "Science",
            "Sport"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


