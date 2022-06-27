# cdt

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cdt)
*   [Huggingface](https://huggingface.co/datasets/cdt)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cdt')
```

*   **Description**:

```
The Cyberbullying Detection task was part of 2019 edition of PolEval competition. The goal is to predict if a given Twitter message contains a cyberbullying (harmful) content.
```

*   **License**: BSD 3-Clause
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10041

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
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


