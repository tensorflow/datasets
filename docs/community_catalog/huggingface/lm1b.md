# lm1b

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lm1b)
*   [Huggingface](https://huggingface.co/datasets/lm1b)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lm1b/plain_text')
```

*   **Description**:

```
A benchmark corpus to be used for measuring progress in statistical language modeling. This has almost one billion words in the training data.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 306688
`'train'` | 30301028

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


