# hard

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hard)
*   [Huggingface](https://huggingface.co/datasets/hard)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hard/plain_text')
```

*   **Description**:

```
This dataset contains 93700 hotel reviews in Arabic language.The hotel reviews were collected from Booking.com website during June/July 2016.The reviews are expressed in Modern Standard Arabic as well as dialectal Arabic.The following table summarize some tatistics on the HARD Dataset.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 105698

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 5,
        "names": [
            "1",
            "2",
            "3",
            "4",
            "5"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


