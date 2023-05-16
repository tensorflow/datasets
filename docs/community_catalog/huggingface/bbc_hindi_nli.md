# bbc_hindi_nli

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bbc_hindi_nli)
*   [Huggingface](https://huggingface.co/datasets/bbc_hindi_nli)


## bbc hindi nli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bbc_hindi_nli/bbc hindi nli')
```

*   **Description**:

```
This dataset is used to train models for Natural Language Inference Tasks in Low-Resource Languages like Hindi.
```

*   **License**: MIT License

*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2592
`'train'` | 15552
`'validation'` | 2580

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "not-entailment",
            "entailment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "topic": {
        "num_classes": 6,
        "names": [
            "india",
            "news",
            "international",
            "entertainment",
            "sport",
            "science"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


