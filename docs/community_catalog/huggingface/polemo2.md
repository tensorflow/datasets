# polemo2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/polemo2)
*   [Huggingface](https://huggingface.co/datasets/polemo2)


## in


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:polemo2/in')
```

*   **Description**:

```
The PolEmo2.0 is a set of online reviews from medicine and hotels domains. The task is to predict the sentiment of a review. There are two separate test sets, to allow for in-domain (medicine and hotels) as well as out-of-domain (products and university) validation.
```

*   **License**: CC BY-NC-SA 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 722
`'train'` | 5783
`'validation'` | 723

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "num_classes": 4,
        "names": [
            "__label__meta_amb",
            "__label__meta_minus_m",
            "__label__meta_plus_m",
            "__label__meta_zero"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## out


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:polemo2/out')
```

*   **Description**:

```
The PolEmo2.0 is a set of online reviews from medicine and hotels domains. The task is to predict the sentiment of a review. There are two separate test sets, to allow for in-domain (medicine and hotels) as well as out-of-domain (products and university) validation.
```

*   **License**: CC BY-NC-SA 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 494
`'train'` | 5783
`'validation'` | 494

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "num_classes": 4,
        "names": [
            "__label__meta_amb",
            "__label__meta_minus_m",
            "__label__meta_plus_m",
            "__label__meta_zero"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


