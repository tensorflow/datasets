# stsb_mt_sv

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/stsb_mt_sv)
*   [Huggingface](https://huggingface.co/datasets/stsb_mt_sv)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:stsb_mt_sv/plain_text')
```

*   **Description**:

```
Machine translated Swedish version of the original STS-B (http://ixa2.si.ehu.eus/stswiki)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1379
`'train'` | 5749
`'validation'` | 1500

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


