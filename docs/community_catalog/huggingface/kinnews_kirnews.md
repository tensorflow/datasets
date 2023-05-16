# kinnews_kirnews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kinnews_kirnews)
*   [Huggingface](https://huggingface.co/datasets/kinnews_kirnews)


## kinnews_raw


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kinnews_kirnews/kinnews_raw')
```

*   **Description**:

```
Kinyarwanda and Kirundi news classification datasets
```

*   **License**: MIT License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4254
`'train'` | 17014

*   **Features**:

```json
{
    "label": {
        "num_classes": 14,
        "names": [
            "politics",
            "sport",
            "economy",
            "health",
            "entertainment",
            "history",
            "technology",
            "tourism",
            "culture",
            "fashion",
            "religion",
            "environment",
            "education",
            "relationship"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "kin_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "en_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## kinnews_cleaned


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kinnews_kirnews/kinnews_cleaned')
```

*   **Description**:

```
Kinyarwanda and Kirundi news classification datasets
```

*   **License**: MIT License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4254
`'train'` | 17014

*   **Features**:

```json
{
    "label": {
        "num_classes": 14,
        "names": [
            "politics",
            "sport",
            "economy",
            "health",
            "entertainment",
            "history",
            "technology",
            "tourism",
            "culture",
            "fashion",
            "religion",
            "environment",
            "education",
            "relationship"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## kirnews_raw


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kinnews_kirnews/kirnews_raw')
```

*   **Description**:

```
Kinyarwanda and Kirundi news classification datasets
```

*   **License**: MIT License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 923
`'train'` | 3689

*   **Features**:

```json
{
    "label": {
        "num_classes": 14,
        "names": [
            "politics",
            "sport",
            "economy",
            "health",
            "entertainment",
            "history",
            "technology",
            "tourism",
            "culture",
            "fashion",
            "religion",
            "environment",
            "education",
            "relationship"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "kir_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "en_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## kirnews_cleaned


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kinnews_kirnews/kirnews_cleaned')
```

*   **Description**:

```
Kinyarwanda and Kirundi news classification datasets
```

*   **License**: MIT License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 923
`'train'` | 3689

*   **Features**:

```json
{
    "label": {
        "num_classes": 14,
        "names": [
            "politics",
            "sport",
            "economy",
            "health",
            "entertainment",
            "history",
            "technology",
            "tourism",
            "culture",
            "fashion",
            "religion",
            "environment",
            "education",
            "relationship"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


