# scielo

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/scielo)
*   [Huggingface](https://huggingface.co/datasets/scielo)


## en-es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scielo/en-es')
```

*   **Description**:

```
A parallel corpus of full-text scientific articles collected from Scielo database in the following languages: English, Portuguese and Spanish. The corpus is sentence aligned for all language pairs, as well as trilingual aligned for a small subset of sentences. Alignment was carried out using the Hunalign algorithm.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 177782

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "es"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scielo/en-pt')
```

*   **Description**:

```
A parallel corpus of full-text scientific articles collected from Scielo database in the following languages: English, Portuguese and Spanish. The corpus is sentence aligned for all language pairs, as well as trilingual aligned for a small subset of sentences. Alignment was carried out using the Hunalign algorithm.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2828917

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-pt-es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scielo/en-pt-es')
```

*   **Description**:

```
A parallel corpus of full-text scientific articles collected from Scielo database in the following languages: English, Portuguese and Spanish. The corpus is sentence aligned for all language pairs, as well as trilingual aligned for a small subset of sentences. Alignment was carried out using the Hunalign algorithm.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 255915

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "pt",
            "es"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


