# imdb

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/imdb)
*   [Huggingface](https://huggingface.co/datasets/imdb)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imdb/plain_text')
```

*   **Description**:

```
Large Movie Review Dataset.
This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training, and 25,000 for testing. There is additional unlabeled data for use as well.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 25000
`'train'` | 25000
`'unsupervised'` | 50000

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


