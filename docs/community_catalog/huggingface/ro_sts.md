# ro_sts

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ro_sts)
*   [Huggingface](https://huggingface.co/datasets/ro_sts)


## ro_sts


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ro_sts/ro_sts')
```

*   **Description**:

```
The RO-STS (Romanian Semantic Textual Similarity) dataset contains 8628 pairs of sentences with their similarity score. It is a high-quality translation of the STS benchmark dataset.
```

*   **License**: CC BY-SA 4.0 License
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
    "score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


