# opus_montenegrinsubs

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_montenegrinsubs)
*   [Huggingface](https://huggingface.co/datasets/opus_montenegrinsubs)


## en-me


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_montenegrinsubs/en-me')
```

*   **Description**:

```
Opus MontenegrinSubs dataset for machine translation task, for language pair en-me: english and montenegrin
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 65043

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "me"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


