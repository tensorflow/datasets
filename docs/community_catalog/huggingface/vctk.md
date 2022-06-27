# vctk

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/vctk)
*   [Huggingface](https://huggingface.co/datasets/vctk)


## main


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:vctk/main')
```

*   **Description**:

```

```

*   **License**: No known license
*   **Version**: 0.9.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 88156

*   **Features**:

```json
{
    "speaker_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 48000,
        "mono": true,
        "_storage_dtype": "string",
        "id": null,
        "_type": "Audio"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "age": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gender": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "accent": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "region": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "comment": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


