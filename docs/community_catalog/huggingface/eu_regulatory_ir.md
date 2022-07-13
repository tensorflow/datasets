# eu_regulatory_ir

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/eu_regulatory_ir)
*   [Huggingface](https://huggingface.co/datasets/eu_regulatory_ir)


## eu2uk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:eu_regulatory_ir/eu2uk')
```

*   **Description**:

```
EURegIR: Regulatory Compliance IR (EU/UK)
```

*   **License**: CC BY-SA (Creative Commons / Attribution-ShareAlike)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 300
`'train'` | 1400
`'uk_corpus'` | 52515
`'validation'` | 300

*   **Features**:

```json
{
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "publication_year": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relevant_documents": {
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



## uk2eu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:eu_regulatory_ir/uk2eu')
```

*   **Description**:

```
EURegIR: Regulatory Compliance IR (EU/UK)
```

*   **License**: CC BY-SA (Creative Commons / Attribution-ShareAlike)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'eu_corpus'` | 3930
`'test'` | 300
`'train'` | 1500
`'validation'` | 300

*   **Features**:

```json
{
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "publication_year": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relevant_documents": {
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


