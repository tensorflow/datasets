# farsi_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/farsi_news)
*   [Huggingface](https://huggingface.co/datasets/farsi_news)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:farsi_news')
```

*   **Description**:

```

```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'hamshahri'` | 2203
`'radiofarda'` | 284

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "link": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


