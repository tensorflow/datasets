# hope_edi

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hope_edi)
*   [Huggingface](https://huggingface.co/datasets/hope_edi)


## english


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hope_edi/english')
```

*   **Description**:

```
A Hope Speech dataset for Equality, Diversity and Inclusion (HopeEDI) containing user-generated comments from the social media platform YouTube with 28,451, 20,198 and 10,705 comments in English, Tamil and Malayalam, respectively, manually labelled as containing hope speech or not.
```

*   **License**: Creative Commons Attribution 4.0 International Licence
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 22762
`'validation'` | 2843

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "Hope_speech",
            "Non_hope_speech",
            "not-English"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## tamil


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hope_edi/tamil')
```

*   **Description**:

```
A Hope Speech dataset for Equality, Diversity and Inclusion (HopeEDI) containing user-generated comments from the social media platform YouTube with 28,451, 20,198 and 10,705 comments in English, Tamil and Malayalam, respectively, manually labelled as containing hope speech or not.
```

*   **License**: Creative Commons Attribution 4.0 International Licence
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 16160
`'validation'` | 2018

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "Hope_speech",
            "Non_hope_speech",
            "not-Tamil"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## malayalam


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hope_edi/malayalam')
```

*   **Description**:

```
A Hope Speech dataset for Equality, Diversity and Inclusion (HopeEDI) containing user-generated comments from the social media platform YouTube with 28,451, 20,198 and 10,705 comments in English, Tamil and Malayalam, respectively, manually labelled as containing hope speech or not.
```

*   **License**: Creative Commons Attribution 4.0 International Licence
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8564
`'validation'` | 1070

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "Hope_speech",
            "Non_hope_speech",
            "not-malayalam"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


