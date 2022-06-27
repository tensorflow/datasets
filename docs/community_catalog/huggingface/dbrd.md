# dbrd

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/dbrd)
*   [Huggingface](https://huggingface.co/datasets/dbrd)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:dbrd/plain_text')
```

*   **Description**:

```
The Dutch Book Review Dataset (DBRD) contains over 110k book reviews of which 22k have associated binary sentiment polarity labels. It is intended as a benchmark for sentiment classification in Dutch and created due to a lack of annotated datasets in Dutch that are suitable for this task.
```

*   **License**: No known license
*   **Version**: 3.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2224
`'train'` | 20028
`'unsupervised'` | 96264

*   **Features**:

```json
{
    "text": {
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


