# billsum

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/billsum)
*   [Huggingface](https://huggingface.co/datasets/billsum)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:billsum')
```

*   **Description**:

```
BillSum, summarization of US Congressional and California state bills.

There are several features:
  - text: bill text.
  - summary: summary of the bills.
  - title: title of the bills.
features for us bills. ca bills does not have.
  - text_len: number of chars in text.
  - sum_len: number of chars in summary.
```

*   **License**: No known license
*   **Version**: 3.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'ca_test'` | 1237
`'test'` | 3269
`'train'` | 18949

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


