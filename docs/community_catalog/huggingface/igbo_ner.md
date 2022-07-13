# igbo_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/igbo_ner)
*   [Huggingface](https://huggingface.co/datasets/igbo_ner)


## ner_data


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:igbo_ner/ner_data')
```

*   **Description**:

```
Igbo Named Entity Recognition Dataset
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 30715

*   **Features**:

```json
{
    "content_n": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "named_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentences": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## free_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:igbo_ner/free_text')
```

*   **Description**:

```
Igbo Named Entity Recognition Dataset
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10000

*   **Features**:

```json
{
    "sentences": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


