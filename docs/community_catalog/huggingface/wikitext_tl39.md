# wikitext_tl39

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wikitext_tl39)
*   [Huggingface](https://huggingface.co/datasets/wikitext_tl39)


## wikitext-tl-39


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikitext_tl39/wikitext-tl-39')
```

*   **Description**:

```
Large scale, unlabeled text dataset with 39 Million tokens in the training set. Inspired by the original WikiText Long Term Dependency dataset (Merity et al., 2016). TL means "Tagalog." Originally published in Cruz & Cheng (2019).
```

*   **License**: GPL-3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 376737
`'train'` | 1766072
`'validation'` | 381763

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


