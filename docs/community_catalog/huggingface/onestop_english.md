# onestop_english

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/onestop_english)
*   [Huggingface](https://huggingface.co/datasets/onestop_english)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:onestop_english')
```

*   **Description**:

```
This dataset is a compilation of the OneStopEnglish corpus of texts written at three reading levels into one file.
Text documents are classified into three reading levels - ele, int, adv (Elementary, Intermediate and Advance).
This dataset demonstrates its usefulness for through two applica-tions - automatic  readability  assessment  and automatic text simplification.
The corpus consists of 189 texts, each in three versions/reading levels (567 in total).
```

*   **License**: Creative Commons Attribution-ShareAlike 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 567

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "ele",
            "int",
            "adv"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


