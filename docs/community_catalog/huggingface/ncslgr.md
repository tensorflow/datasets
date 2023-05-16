# ncslgr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ncslgr)
*   [Huggingface](https://huggingface.co/datasets/ncslgr)


## entire_dataset


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ncslgr/entire_dataset')
```

*   **Description**:

```
A small corpus of American Sign Language (ASL) video data from native signers, annotated with non-manual features.
```

*   **License**: No known license
*   **Version**: 0.7.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 870

*   **Features**:

```json
{
    "eaf": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentences": {
        "feature": {
            "gloss": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "videos": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## annotations


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ncslgr/annotations')
```

*   **Description**:

```
A small corpus of American Sign Language (ASL) video data from native signers, annotated with non-manual features.
```

*   **License**: No known license
*   **Version**: 0.7.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 870

*   **Features**:

```json
{
    "eaf": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentences": {
        "feature": {
            "gloss": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "videos": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


