# mt_eng_vietnamese

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mt_eng_vietnamese)
*   [Huggingface](https://huggingface.co/datasets/mt_eng_vietnamese)


## iwslt2015-vi-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mt_eng_vietnamese/iwslt2015-vi-en')
```

*   **Description**:

```
Preprocessed Dataset from IWSLT'15 English-Vietnamese machine translation: English-Vietnamese.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1269
`'train'` | 133318
`'validation'` | 1269

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "vi",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## iwslt2015-en-vi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mt_eng_vietnamese/iwslt2015-en-vi')
```

*   **Description**:

```
Preprocessed Dataset from IWSLT'15 English-Vietnamese machine translation: English-Vietnamese.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1269
`'train'` | 133318
`'validation'` | 1269

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "vi"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


