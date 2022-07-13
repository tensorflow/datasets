# kor_qpair

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kor_qpair)
*   [Huggingface](https://huggingface.co/datasets/kor_qpair)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_qpair')
```

*   **Description**:

```
This is a Korean paired question dateset containing labels that denote whether two questions in a given pair are semantically identical.
```

*   **License**: The MIT License (MIT)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 758
`'train'` | 6136
`'validation'` | 682

*   **Features**:

```json
{
    "question1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "is_duplicate": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


