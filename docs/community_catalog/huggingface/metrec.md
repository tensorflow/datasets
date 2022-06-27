# metrec

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/metrec)
*   [Huggingface](https://huggingface.co/datasets/metrec)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:metrec/plain_text')
```

*   **Description**:

```
Arabic Poetry Metric Classification.
The dataset contains the verses and their corresponding meter classes.Meter classes are represented as numbers from 0 to 13. The dataset can be highly useful for further research in order to improve the field of Arabic poems’ meter classification.The train dataset contains 47,124 records and the test dataset contains 8316 records.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8316
`'train'` | 47124

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 14,
        "names": [
            "saree",
            "kamel",
            "mutakareb",
            "mutadarak",
            "munsareh",
            "madeed",
            "mujtath",
            "ramal",
            "baseet",
            "khafeef",
            "taweel",
            "wafer",
            "hazaj",
            "rajaz"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


