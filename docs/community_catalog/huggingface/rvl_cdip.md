# rvl_cdip

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/rvl_cdip)
*   [Huggingface](https://huggingface.co/datasets/rvl_cdip)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:rvl_cdip')
```

*   **Description**:

```
The RVL-CDIP (Ryerson Vision Lab Complex Document Information Processing) dataset consists of 400,000 grayscale images in 16 classes, with 25,000 images per class. There are 320,000 training images, 40,000 validation images, and 40,000 test images.
```

*   **License**: https://www.industrydocuments.ucsf.edu/help/copyright/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 40000
`'train'` | 320000
`'validation'` | 40000

*   **Features**:

```json
{
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "label": {
        "num_classes": 16,
        "names": [
            "letter",
            "form",
            "email",
            "handwritten",
            "advertisement",
            "scientific report",
            "scientific publication",
            "specification",
            "file folder",
            "news article",
            "budget",
            "invoice",
            "presentation",
            "questionnaire",
            "resume",
            "memo"
        ],
        "id": null,
        "_type": "ClassLabel"
    }
}
```


