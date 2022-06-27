# kor_sarcasm

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kor_sarcasm)
*   [Huggingface](https://huggingface.co/datasets/kor_sarcasm)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_sarcasm')
```

*   **Description**:

```
This is a dataset designed to detect sarcasm in Korean because it distorts the literal meaning of a sentence
and is highly related to sentiment classification.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 301
`'train'` | 9000

*   **Features**:

```json
{
    "tokens": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "no_sarcasm",
            "sarcasm"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


