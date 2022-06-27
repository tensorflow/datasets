# web_of_science

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/web_of_science)
*   [Huggingface](https://huggingface.co/datasets/web_of_science)


## WOS5736


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_of_science/WOS5736')
```

*   **Description**:

```
The Web Of Science (WOS) dataset is a collection of data  of published papers
available from the Web of Science. WOS has been released in three versions: WOS-46985, WOS-11967 and WOS-5736. WOS-46985 is the
full dataset. WOS-11967 and WOS-5736 are two subsets of WOS-46985.

Web of Science Dataset WOS-5736: This dataset contains 5,736 documents with 11 categories which include 3 parents categories.
```

*   **License**: No known license
*   **Version**: 6.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5736

*   **Features**:

```json
{
    "input_data": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label_level_1": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label_level_2": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## WOS11967


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_of_science/WOS11967')
```

*   **Description**:

```
The Web Of Science (WOS) dataset is a collection of data  of published papers
available from the Web of Science. WOS has been released in three versions: WOS-46985, WOS-11967 and WOS-5736. WOS-46985 is the
full dataset. WOS-11967 and WOS-5736 are two subsets of WOS-46985.

Web of Science Dataset WOS-11967: This dataset contains 11,967 documents with 35 categories which include 7 parents categories.
```

*   **License**: No known license
*   **Version**: 6.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 11967

*   **Features**:

```json
{
    "input_data": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label_level_1": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label_level_2": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## WOS46985


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_of_science/WOS46985')
```

*   **Description**:

```
The Web Of Science (WOS) dataset is a collection of data  of published papers
available from the Web of Science. WOS has been released in three versions: WOS-46985, WOS-11967 and WOS-5736. WOS-46985 is the
full dataset. WOS-11967 and WOS-5736 are two subsets of WOS-46985.

Web of Science Dataset WOS-46985: This dataset contains 46,985 documents with 134 categories which include 7 parents categories.
```

*   **License**: No known license
*   **Version**: 6.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 46985

*   **Features**:

```json
{
    "input_data": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label_level_1": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label_level_2": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


