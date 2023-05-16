# amttl

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/amttl)
*   [Huggingface](https://huggingface.co/datasets/amttl)


## amttl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amttl/amttl')
```

*   **Description**:

```
Chinese word segmentation (CWS) trained from open source corpus faces dramatic performance drop
when dealing with domain text, especially for a domain with lots of special terms and diverse
writing styles, such as the biomedical domain. However, building domain-specific CWS requires
extremely high annotation cost. In this paper, we propose an approach by exploiting domain-invariant
knowledge from high resource to low resource domains. Extensive experiments show that our mode
achieves consistently higher accuracy than the single-task CWS and other transfer learning
baselines, especially when there is a large disparity between source and target domains.

This dataset is the accompanied medical Chinese word segmentation (CWS) dataset.
The tags are in BIES scheme.

For more details see https://www.aclweb.org/anthology/C18-1307/
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 908
`'train'` | 3063
`'validation'` | 822

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "num_classes": 4,
            "names": [
                "B",
                "I",
                "E",
                "S"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


