# wisesight1000

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wisesight1000)
*   [Huggingface](https://huggingface.co/datasets/wisesight1000)


## wisesight1000


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wisesight1000/wisesight1000')
```

*   **Description**:

```

```

*   **License**: CC-0 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 993

*   **Features**:

```json
{
    "char": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "char_type": {
        "feature": {
            "num_classes": 12,
            "names": [
                "b_e",
                "c",
                "d",
                "n",
                "o",
                "p",
                "q",
                "s",
                "s_e",
                "t",
                "v",
                "w"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "is_beginning": {
        "feature": {
            "num_classes": 2,
            "names": [
                "neg",
                "pos"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


