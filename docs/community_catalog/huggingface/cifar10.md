# cifar10

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cifar10)
*   [Huggingface](https://huggingface.co/datasets/cifar10)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cifar10/plain_text')
```

*   **Description**:

```
The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images
per class. There are 50000 training images and 10000 test images.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 50000

*   **Features**:

```json
{
    "img": {
        "id": null,
        "_type": "Image"
    },
    "label": {
        "num_classes": 10,
        "names": [
            "airplane",
            "automobile",
            "bird",
            "cat",
            "deer",
            "dog",
            "frog",
            "horse",
            "ship",
            "truck"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


