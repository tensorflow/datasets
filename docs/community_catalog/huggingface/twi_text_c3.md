# twi_text_c3

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/twi_text_c3)
*   [Huggingface](https://huggingface.co/datasets/twi_text_c3)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:twi_text_c3/plain_text')
```

*   **Description**:

```
Twi Text C3 is the largest Twi texts collected and used to train FastText embeddings in the
YorubaTwi Embedding paper: https://www.aclweb.org/anthology/2020.lrec-1.335/
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 675772

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


