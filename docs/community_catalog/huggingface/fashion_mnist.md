# fashion_mnist

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/fashion_mnist)
*   [Huggingface](https://huggingface.co/datasets/fashion_mnist)


## fashion_mnist


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:fashion_mnist/fashion_mnist')
```

*   **Description**:

```
Fashion-MNIST is a dataset of Zalando's article images—consisting of a training set of
60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image,
associated with a label from 10 classes. We intend Fashion-MNIST to serve as a direct drop-in
replacement for the original MNIST dataset for benchmarking machine learning algorithms.
It shares the same image size and structure of training and testing splits.
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
            "T - shirt / top",
            "Trouser",
            "Pullover",
            "Dress",
            "Coat",
            "Sandal",
            "Shirt",
            "Sneaker",
            "Bag",
            "Ankle boot"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


