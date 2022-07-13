# kor_hate

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kor_hate)
*   [Huggingface](https://huggingface.co/datasets/kor_hate)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_hate')
```

*   **Description**:

```
Human-annotated Korean corpus collected from a popular domestic entertainment news aggregation platform
for toxic speech detection. Comments are annotated for gender bias, social bias and hate speech.
```

*   **License**: Creative Commons
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 471
`'train'` | 7896

*   **Features**:

```json
{
    "comments": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "contain_gender_bias": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "bias": {
        "num_classes": 3,
        "names": [
            "none",
            "gender",
            "others"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "hate": {
        "num_classes": 3,
        "names": [
            "hate",
            "offensive",
            "none"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


