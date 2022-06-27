# opus_finlex

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_finlex)
*   [Huggingface](https://huggingface.co/datasets/opus_finlex)


## fi-sv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_finlex/fi-sv')
```

*   **Description**:

```
The Finlex Data Base is a comprehensive collection of legislative and other judicial information of Finland, which is available in Finnish, Swedish and partially in English. This corpus is taken from the Semantic Finlex serice that provides the Finnish and Swedish data as linked open data and also raw XML files.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3114141

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "fi",
            "sv"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


