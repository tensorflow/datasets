# sst

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sst)
*   [Huggingface](https://huggingface.co/datasets/sst)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sst')
```

*   **Description**:

```
The Stanford Sentiment Treebank, the first corpus with fully labeled parse trees that allows for a
complete analysis of the compositional effects of sentiment in language.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2210
`'train'` | 8544
`'validation'` | 1101

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tree": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## dictionary


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sst/dictionary')
```

*   **Description**:

```
The Stanford Sentiment Treebank, the first corpus with fully labeled parse trees that allows for a
complete analysis of the compositional effects of sentiment in language.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dictionary'` | 239232

*   **Features**:

```json
{
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## ptb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sst/ptb')
```

*   **Description**:

```
The Stanford Sentiment Treebank, the first corpus with fully labeled parse trees that allows for a
complete analysis of the compositional effects of sentiment in language.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2210
`'train'` | 8544
`'validation'` | 1101

*   **Features**:

```json
{
    "ptb_tree": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


