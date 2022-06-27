# metashift

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/metashift)
*   [Huggingface](https://huggingface.co/datasets/metashift)


## metashift


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:metashift/metashift')
```

*   **Description**:

```
The MetaShift is a dataset of datasets for evaluating distribution shifts and training conflicts.
The MetaShift dataset is a collection of 12,868 sets of natural images across 410 classes.
It was created for understanding the performance of a machine learning model across diverse data distributions.
```

*   **License**: https://github.com/Weixin-Liang/MetaShift/blob/main/LICENSE
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 86808

*   **Features**:

```json
{
    "image_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "label": {
        "num_classes": 8,
        "names": [
            "cat",
            "dog",
            "bus",
            "truck",
            "elephant",
            "horse",
            "bowl",
            "cup"
        ],
        "id": null,
        "_type": "ClassLabel"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


