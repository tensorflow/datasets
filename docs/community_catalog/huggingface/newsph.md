# newsph

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/newsph)
*   [Huggingface](https://huggingface.co/datasets/newsph)


## newsph


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:newsph/newsph')
```

*   **Description**:

```
Large-scale dataset of Filipino news articles. Sourced for the NewsPH-NLI Project (Cruz et al., 2020).
```

*   **License**: GPL-3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2190465

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


