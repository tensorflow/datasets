# opus_dogc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_dogc)
*   [Huggingface](https://huggingface.co/datasets/opus_dogc)


## tmx


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_dogc/tmx')
```

*   **Description**:

```
This is a collection of documents from the Official Journal of the Government of Catalonia, in Catalan and Spanish languages, provided by Antoni Oliver Gonzalez from the Universitat Oberta de Catalunya.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4763575

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "ca",
            "es"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


