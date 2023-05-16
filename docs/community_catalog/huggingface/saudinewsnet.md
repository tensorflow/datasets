# saudinewsnet

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/saudinewsnet)
*   [Huggingface](https://huggingface.co/datasets/saudinewsnet)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:saudinewsnet')
```

*   **Description**:

```
The dataset contains a set of 31,030 Arabic newspaper articles alongwith metadata, extracted from various online Saudi newspapers and written in MSA.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 31030

*   **Features**:

```json
{
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date_extracted": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "author": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


