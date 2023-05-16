# ccaligned_multilingual

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ccaligned_multilingual)
*   [Huggingface](https://huggingface.co/datasets/ccaligned_multilingual)


## documents-zz_TR


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ccaligned_multilingual/documents-zz_TR')
```

*   **Description**:

```
CCAligned consists of parallel or comparable web-document pairs in 137 languages aligned with English. These web-document pairs were constructed by performing language identification on raw web-documents, and ensuring corresponding language codes were corresponding in the URLs of web documents. This pattern matching approach yielded more than 100 million aligned documents paired with English. Recognizing that each English document was often aligned to mulitple documents in different target language, we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 41

*   **Features**:

```json
{
    "Domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Source_URL": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Target_URL": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en_XX",
            "zz_TR"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## sentences-zz_TR


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ccaligned_multilingual/sentences-zz_TR')
```

*   **Description**:

```
CCAligned consists of parallel or comparable web-document pairs in 137 languages aligned with English. These web-document pairs were constructed by performing language identification on raw web-documents, and ensuring corresponding language codes were corresponding in the URLs of web documents. This pattern matching approach yielded more than 100 million aligned documents paired with English. Recognizing that each English document was often aligned to mulitple documents in different target language, we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 34

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en_XX",
            "zz_TR"
        ],
        "id": null,
        "_type": "Translation"
    },
    "LASER_similarity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## documents-tz_MA


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ccaligned_multilingual/documents-tz_MA')
```

*   **Description**:

```
CCAligned consists of parallel or comparable web-document pairs in 137 languages aligned with English. These web-document pairs were constructed by performing language identification on raw web-documents, and ensuring corresponding language codes were corresponding in the URLs of web documents. This pattern matching approach yielded more than 100 million aligned documents paired with English. Recognizing that each English document was often aligned to mulitple documents in different target language, we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4

*   **Features**:

```json
{
    "Domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Source_URL": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Target_URL": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en_XX",
            "tz_MA"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## sentences-tz_MA


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ccaligned_multilingual/sentences-tz_MA')
```

*   **Description**:

```
CCAligned consists of parallel or comparable web-document pairs in 137 languages aligned with English. These web-document pairs were constructed by performing language identification on raw web-documents, and ensuring corresponding language codes were corresponding in the URLs of web documents. This pattern matching approach yielded more than 100 million aligned documents paired with English. Recognizing that each English document was often aligned to mulitple documents in different target language, we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 33

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en_XX",
            "tz_MA"
        ],
        "id": null,
        "_type": "Translation"
    },
    "LASER_similarity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## documents-ak_GH


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ccaligned_multilingual/documents-ak_GH')
```

*   **Description**:

```
CCAligned consists of parallel or comparable web-document pairs in 137 languages aligned with English. These web-document pairs were constructed by performing language identification on raw web-documents, and ensuring corresponding language codes were corresponding in the URLs of web documents. This pattern matching approach yielded more than 100 million aligned documents paired with English. Recognizing that each English document was often aligned to mulitple documents in different target language, we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 249

*   **Features**:

```json
{
    "Domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Source_URL": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Target_URL": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en_XX",
            "ak_GH"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## sentences-ak_GH


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ccaligned_multilingual/sentences-ak_GH')
```

*   **Description**:

```
CCAligned consists of parallel or comparable web-document pairs in 137 languages aligned with English. These web-document pairs were constructed by performing language identification on raw web-documents, and ensuring corresponding language codes were corresponding in the URLs of web documents. This pattern matching approach yielded more than 100 million aligned documents paired with English. Recognizing that each English document was often aligned to mulitple documents in different target language, we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 478

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en_XX",
            "ak_GH"
        ],
        "id": null,
        "_type": "Translation"
    },
    "LASER_similarity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


