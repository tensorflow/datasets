# cats_vs_dogs

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cats_vs_dogs)
*   [Huggingface](https://huggingface.co/datasets/cats_vs_dogs)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cats_vs_dogs')
```

*   **Description**:

```
A large set of images of cats and dogs. There are 1738 corrupted images that are dropped.
```

*   **License**: No known license
*   **Version**: 0.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 23410

*   **Features**:

```json
{
    "image_file_path": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "labels": {
        "num_classes": 2,
        "names": [
            "cat",
            "dog"
        ],
        "id": null,
        "_type": "ClassLabel"
    }
}
```


