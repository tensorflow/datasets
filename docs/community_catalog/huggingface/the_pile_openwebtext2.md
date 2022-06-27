# the_pile_openwebtext2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/the_pile_openwebtext2)
*   [Huggingface](https://huggingface.co/datasets/the_pile_openwebtext2)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:the_pile_openwebtext2/plain_text')
```

*   **Description**:

```
OpenWebText2 is an enhanced version of the original OpenWebTextCorpus covering all Reddit submissions from 2005 up until April 2020, with further months becoming available after the corresponding PushShift dump files are released.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 17103059

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


