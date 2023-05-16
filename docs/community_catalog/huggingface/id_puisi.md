# id_puisi

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/id_puisi)
*   [Huggingface](https://huggingface.co/datasets/id_puisi)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:id_puisi')
```

*   **Description**:

```
Puisi (poem) is an Indonesian poetic form. The dataset contains 7223 Indonesian puisi with its title and author.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7223

*   **Features**:

```json
{
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
    "puisi": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "puisi_with_header": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


