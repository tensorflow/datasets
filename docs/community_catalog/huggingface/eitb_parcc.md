# eitb_parcc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/eitb_parcc)
*   [Huggingface](https://huggingface.co/datasets/eitb_parcc)


## es-eu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:eitb_parcc/es-eu')
```

*   **Description**:

```
EiTB-ParCC: Parallel Corpus of Comparable News. A Basque-Spanish parallel corpus provided by Vicomtech (https://www.vicomtech.org), extracted from comparable news produced by the Basque public broadcasting group Euskal Irrati Telebista.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 637183

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


