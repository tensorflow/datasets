# m_lama

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/m_lama)
*   [Huggingface](https://huggingface.co/datasets/m_lama)


## all


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:m_lama/all')
```

*   **Description**:

```
mLAMA: a multilingual version of the LAMA benchmark (T-REx and GoogleRE) covering 53 languages.
```

*   **License**: The Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). https://creativecommons.org/licenses/by-nc-sa/4.0/
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 843143

*   **Features**:

```json
{
    "uuid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lineid": {
        "dtype": "uint32",
        "id": null,
        "_type": "Value"
    },
    "obj_uri": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_uri": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "template": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "predicate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


