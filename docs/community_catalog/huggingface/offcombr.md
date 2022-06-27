# offcombr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/offcombr)
*   [Huggingface](https://huggingface.co/datasets/offcombr)


## offcombr-2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:offcombr/offcombr-2')
```

*   **Description**:

```
OffComBR: an annotated dataset containing for hate speech detection in Portuguese composed of news comments on the Brazilian Web.
```

*   **License**: Unknown
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1250

*   **Features**:

```json
{
    "label": {
        "num_classes": 2,
        "names": [
            "no",
            "yes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## offcombr-3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:offcombr/offcombr-3')
```

*   **Description**:

```
OffComBR: an annotated dataset containing for hate speech detection in Portuguese composed of news comments on the Brazilian Web.
```

*   **License**: Unknown
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1033

*   **Features**:

```json
{
    "label": {
        "num_classes": 2,
        "names": [
            "no",
            "yes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


