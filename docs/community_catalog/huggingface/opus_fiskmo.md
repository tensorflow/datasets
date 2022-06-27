# opus_fiskmo

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_fiskmo)
*   [Huggingface](https://huggingface.co/datasets/opus_fiskmo)


## fi-sv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_fiskmo/fi-sv')
```

*   **Description**:

```
fiskmo, a massive parallel corpus for Finnish and Swedish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2100001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "fi",
            "sv"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


