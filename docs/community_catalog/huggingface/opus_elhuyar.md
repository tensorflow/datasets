# opus_elhuyar

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_elhuyar)
*   [Huggingface](https://huggingface.co/datasets/opus_elhuyar)


## es-eu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_elhuyar/es-eu')
```

*   **Description**:

```
Dataset provided by the foundation Elhuyar, which is having data in languages Spanish to Basque.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 642348

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "es",
            "eu"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


