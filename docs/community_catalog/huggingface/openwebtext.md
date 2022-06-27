# openwebtext

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/openwebtext)
*   [Huggingface](https://huggingface.co/datasets/openwebtext)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:openwebtext/plain_text')
```

*   **Description**:

```
An open-source replication of the WebText dataset from OpenAI.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8013769

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


