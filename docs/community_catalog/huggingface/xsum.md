# xsum

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/xsum)
*   [Huggingface](https://huggingface.co/datasets/xsum)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xsum')
```

*   **Description**:

```
Extreme Summarization (XSum) Dataset.

There are three features:
  - document: Input news article.
  - summary: One sentence summary of the article.
  - id: BBC ID of the article.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11334
`'train'` | 204045
`'validation'` | 11332

*   **Features**:

```json
{
    "document": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


