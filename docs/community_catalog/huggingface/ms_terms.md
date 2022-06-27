# ms_terms

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ms_terms)
*   [Huggingface](https://huggingface.co/datasets/ms_terms)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ms_terms')
```

*   **Description**:

```
The Microsoft Terminology Collection can be used to develop localized versions of applications that integrate with Microsoft products.
It can also be used to integrate Microsoft terminology into other terminology collections or serve as a base IT glossary
for language development in the nearly 100 languages available. Terminology is provided in .tbx format, an industry standard for terminology exchange.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 33738

*   **Features**:

```json
{
    "entry_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "term_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pos": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "definition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "term_target": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


