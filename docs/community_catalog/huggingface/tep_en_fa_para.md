# tep_en_fa_para

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tep_en_fa_para)
*   [Huggingface](https://huggingface.co/datasets/tep_en_fa_para)


## en-fa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tep_en_fa_para/en-fa')
```

*   **Description**:

```
TEP: Tehran English-Persian parallel corpus. The first free Eng-Per corpus, provided by the Natural Language and Text Processing Laboratory, University of Tehran.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 612087

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "fa"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


