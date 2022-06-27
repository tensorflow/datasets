# beans

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/beans)
*   [Huggingface](https://huggingface.co/datasets/beans)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:beans')
```

*   **Description**:

```
Beans is a dataset of images of beans taken in the field using smartphone
cameras. It consists of 3 classes: 2 disease classes and the healthy class.
Diseases depicted include Angular Leaf Spot and Bean Rust. Data was annotated
by experts from the National Crops Resources Research Institute (NaCRRI) in
Uganda and collected by the Makerere AI research lab.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 128
`'train'` | 1034
`'validation'` | 133

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
        "num_classes": 3,
        "names": [
            "angular_leaf_spot",
            "bean_rust",
            "healthy"
        ],
        "id": null,
        "_type": "ClassLabel"
    }
}
```


