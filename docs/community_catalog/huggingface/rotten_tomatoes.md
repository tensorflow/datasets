# rotten_tomatoes

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/rotten_tomatoes)
*   [Huggingface](https://huggingface.co/datasets/rotten_tomatoes)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:rotten_tomatoes')
```

*   **Description**:

```
Movie Review Dataset.
This is a dataset of containing 5,331 positive and 5,331 negative processed
sentences from Rotten Tomatoes movie reviews. This data was first used in Bo
Pang and Lillian Lee, ``Seeing stars: Exploiting class relationships for
sentiment categorization with respect to rating scales.'', Proceedings of the
ACL, 2005.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1066
`'train'` | 8530
`'validation'` | 1066

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


