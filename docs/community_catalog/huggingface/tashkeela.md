# tashkeela

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tashkeela)
*   [Huggingface](https://huggingface.co/datasets/tashkeela)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tashkeela/plain_text')
```

*   **Description**:

```
Arabic vocalized texts.
it contains 75 million of fully vocalized words mainly97 books from classical and modern Arabic language.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 97

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "book": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


