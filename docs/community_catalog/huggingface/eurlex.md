# eurlex

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/eurlex)
*   [Huggingface](https://huggingface.co/datasets/eurlex)


## eurlex57k


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:eurlex/eurlex57k')
```

*   **Description**:

```
EURLEX57K contains 57k legislative documents in English from EUR-Lex portal, annotated with EUROVOC concepts.
```

*   **License**: CC BY-SA (Creative Commons / Attribution-ShareAlike)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6000
`'train'` | 45000
`'validation'` | 6000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "eurovoc_concepts": {
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


