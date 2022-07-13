# ptb_text_only

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ptb_text_only)
*   [Huggingface](https://huggingface.co/datasets/ptb_text_only)


## penn_treebank


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ptb_text_only/penn_treebank')
```

*   **Description**:

```
This is the Penn Treebank Project: Release 2 CDROM, featuring a million words of 1989 Wall Street Journal material. This corpus has been annotated for part-of-speech (POS) information. In addition, over half of it has been annotated for skeletal syntactic structure.
```

*   **License**: LDC User Agreement for Non-Members
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3761
`'train'` | 42068
`'validation'` | 3370

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


