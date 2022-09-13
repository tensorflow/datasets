# gigaword

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/gigaword)
*   [Huggingface](https://huggingface.co/datasets/gigaword)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:gigaword')
```

*   **Description**:

```
Headline-generation on a corpus of article pairs from Gigaword consisting of
around 4 million articles. Use the 'org_data' provided by
https://github.com/microsoft/unilm/ which is identical to
https://github.com/harvardnlp/sent-summary but with better format.

There are two features:
  - document: article.
  - summary: headline.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1951
`'train'` | 3803957
`'validation'` | 189651

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
    }
}
```


