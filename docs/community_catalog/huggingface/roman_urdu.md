# roman_urdu

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/roman_urdu)
*   [Huggingface](https://huggingface.co/datasets/roman_urdu)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:roman_urdu')
```

*   **Description**:

```
This is an extensive compilation of Roman Urdu Dataset (Urdu written in Latin/Roman script) tagged for sentiment analysis.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 20229

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentiment": {
        "num_classes": 3,
        "names": [
            "Positive",
            "Negative",
            "Neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


