# pass

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/pass)
*   [Huggingface](https://huggingface.co/datasets/pass)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pass')
```

*   **Description**:

```
PASS (Pictures without humAns for Self-Supervision) is a large-scale dataset of 1,440,191 images that does not include any humans
and which can be used for high-quality pretraining while significantly reducing privacy concerns.
The PASS images are sourced from the YFCC-100M dataset.
```

*   **License**: Creative Commons Attribution 4.0 International
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1439719

*   **Features**:

```json
{
    "image": {
        "id": null,
        "_type": "Image"
    },
    "creator_username": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hash": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gps_latitude": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "gps_longitude": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "date_taken": {
        "dtype": "timestamp[us]",
        "id": null,
        "_type": "Value"
    }
}
```


