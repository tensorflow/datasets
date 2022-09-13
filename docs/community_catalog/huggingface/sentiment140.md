# sentiment140

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sentiment140)
*   [Huggingface](https://huggingface.co/datasets/sentiment140)


## sentiment140


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sentiment140/sentiment140')
```

*   **Description**:

```
Sentiment140 consists of Twitter messages with emoticons, which are used as noisy labels for
sentiment classification. For more detailed information please refer to the paper.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 498
`'train'` | 1600000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "user": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentiment": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


