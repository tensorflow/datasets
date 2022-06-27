# igbo_english_machine_translation

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/igbo_english_machine_translation)
*   [Huggingface](https://huggingface.co/datasets/igbo_english_machine_translation)


## ig-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:igbo_english_machine_translation/ig-en')
```

*   **Description**:

```
Parallel Igbo-English Dataset
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 552
`'train'` | 10000
`'validation'` | 200

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
            "ig",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


