# opus_memat

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_memat)
*   [Huggingface](https://huggingface.co/datasets/opus_memat)


## xh-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_memat/xh-en')
```

*   **Description**:

```
Xhosa-English parallel corpora, funded by EPSRC, the Medical Machine Translation project worked on machine translation between ixiXhosa and English, with a focus on the medical domain.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 154764

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "xh",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


