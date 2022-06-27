# catalonia_independence

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/catalonia_independence)
*   [Huggingface](https://huggingface.co/datasets/catalonia_independence)


## catalan


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:catalonia_independence/catalan')
```

*   **Description**:

```
This dataset contains two corpora in Spanish and Catalan that consist of annotated Twitter messages for automatic stance detection. The data was collected over 12 days during February and March of 2019 from tweets posted in Barcelona, and during September of 2018 from tweets posted in the town of Terrassa, Catalonia.

Each corpus is annotated with three classes: AGAINST, FAVOR and NEUTRAL, which express the stance towards the target - independence of Catalonia.
```

*   **License**: CC BY-NC-SA 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2010
`'train'` | 6028
`'validation'` | 2010

*   **Features**:

```json
{
    "id_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "TWEET": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "LABEL": {
        "num_classes": 3,
        "names": [
            "AGAINST",
            "FAVOR",
            "NEUTRAL"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## spanish


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:catalonia_independence/spanish')
```

*   **Description**:

```
This dataset contains two corpora in Spanish and Catalan that consist of annotated Twitter messages for automatic stance detection. The data was collected over 12 days during February and March of 2019 from tweets posted in Barcelona, and during September of 2018 from tweets posted in the town of Terrassa, Catalonia.

Each corpus is annotated with three classes: AGAINST, FAVOR and NEUTRAL, which express the stance towards the target - independence of Catalonia.
```

*   **License**: CC BY-NC-SA 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2016
`'train'` | 6046
`'validation'` | 2015

*   **Features**:

```json
{
    "id_str": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "TWEET": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "LABEL": {
        "num_classes": 3,
        "names": [
            "AGAINST",
            "FAVOR",
            "NEUTRAL"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


