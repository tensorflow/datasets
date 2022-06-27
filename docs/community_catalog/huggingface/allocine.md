# allocine

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/allocine)
*   [Huggingface](https://huggingface.co/datasets/allocine)


## allocine


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:allocine/allocine')
```

*   **Description**:

```
Allocine Dataset: A Large-Scale French Movie Reviews Dataset.
 This is a dataset for binary sentiment classification, made of user reviews scraped from Allocine.fr.
 It contains 100k positive and 100k negative reviews divided into 3 balanced splits: train (160k reviews), val (20k) and test (20k).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 20000
`'train'` | 160000
`'validation'` | 20000

*   **Features**:

```json
{
    "review": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


