# aeslc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/aeslc)
*   [Huggingface](https://huggingface.co/datasets/aeslc)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:aeslc')
```

*   **Description**:

```
A collection of email messages of employees in the Enron Corporation.

There are two features:
  - email_body: email body text.
  - subject_line: email subject text.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1906
`'train'` | 14436
`'validation'` | 1960

*   **Features**:

```json
{
    "email_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject_line": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


