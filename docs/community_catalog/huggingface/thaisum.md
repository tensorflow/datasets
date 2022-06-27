# thaisum

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/thaisum)
*   [Huggingface](https://huggingface.co/datasets/thaisum)


## thaisum


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:thaisum/thaisum')
```

*   **Description**:

```
ThaiSum is a large-scale corpus for Thai text summarization obtained from several online news websites namely Thairath,
ThaiPBS, Prachathai, and The Standard. This dataset consists of over 350,000 article and summary pairs
written by journalists.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11000
`'train'` | 358868
`'validation'` | 11000

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tags": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


