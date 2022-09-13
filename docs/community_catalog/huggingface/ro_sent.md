# ro_sent

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ro_sent)
*   [Huggingface](https://huggingface.co/datasets/ro_sent)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ro_sent')
```

*   **Description**:

```
This dataset is a Romanian Sentiment Analysis dataset.
It is present in a processed form, as used by the authors of `Romanian Transformers`
in their examples and based on the original data present in
`https://github.com/katakonst/sentiment-analysis-tensorflow`.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11005
`'train'` | 17941

*   **Features**:

```json
{
    "original_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "negative",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


