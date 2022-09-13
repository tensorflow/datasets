# opus_xhosanavy

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_xhosanavy)
*   [Huggingface](https://huggingface.co/datasets/opus_xhosanavy)


## en-xh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_xhosanavy/en-xh')
```

*   **Description**:

```
This dataset is designed for machine translation from English to Xhosa.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 49982

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "xh"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


