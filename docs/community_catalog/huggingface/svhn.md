# svhn

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/svhn)
*   [Huggingface](https://huggingface.co/datasets/svhn)


## full_numbers


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:svhn/full_numbers')
```

*   **Description**:

```
SVHN is a real-world image dataset for developing machine learning and object recognition algorithms with minimal requirement on data preprocessing and formatting.
It can be seen as similar in flavor to MNIST (e.g., the images are of small cropped digits), but incorporates an order of magnitude more labeled data (over 600,000 digit images)
and comes from a significantly harder, unsolved, real world problem (recognizing digits and numbers in natural scene images). SVHN is obtained from house numbers in Google Street View images.
```

*   **License**: Custom (non-commercial)
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'extra'` | 202353
`'test'` | 13068
`'train'` | 33402

*   **Features**:

```json
{
    "image": {
        "id": null,
        "_type": "Image"
    },
    "digits": {
        "feature": {
            "bbox": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": 4,
                "id": null,
                "_type": "Sequence"
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
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## cropped_digits


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:svhn/cropped_digits')
```

*   **Description**:

```
SVHN is a real-world image dataset for developing machine learning and object recognition algorithms with minimal requirement on data preprocessing and formatting.
It can be seen as similar in flavor to MNIST (e.g., the images are of small cropped digits), but incorporates an order of magnitude more labeled data (over 600,000 digit images)
and comes from a significantly harder, unsolved, real world problem (recognizing digits and numbers in natural scene images). SVHN is obtained from house numbers in Google Street View images.
```

*   **License**: Custom (non-commercial)
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'extra'` | 531131
`'test'` | 26032
`'train'` | 73257

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


