# mnist

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mnist)
*   [Huggingface](https://huggingface.co/datasets/mnist)


## mnist


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mnist/mnist')
```

*   **Description**:

```
The MNIST dataset consists of 70,000 28x28 black-and-white images in 10 classes (one for each digits), with 7,000
images per class. There are 60,000 training images and 10,000 test images.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 60000

*   **Features**:

```json
{
    "image": {
        "id": null,
        "_type": "Image"
    },
    "label": {
        "num_classes": 10,
        "names": [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


