# ro_sts_parallel

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ro_sts_parallel)
*   [Huggingface](https://huggingface.co/datasets/ro_sts_parallel)


## ro_sts_parallel


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ro_sts_parallel/ro_sts_parallel')
```

*   **Description**:

```
The RO-STS-Parallel (a Parallel Romanian English dataset - translation of the Semantic Textual Similarity) contains 17256 sentences in Romanian and English. It is a high-quality translation of the English STS benchmark dataset into Romanian.
```

*   **License**: CC BY-SA 4.0 License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2759
`'train'` | 11499
`'validation'` | 3001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "ro",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## rosts-parallel-en-ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ro_sts_parallel/rosts-parallel-en-ro')
```

*   **Description**:

```
The RO-STS-Parallel (a Parallel Romanian English dataset - translation of the Semantic Textual Similarity) contains 17256 sentences in Romanian and English. It is a high-quality translation of the English STS benchmark dataset into Romanian.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2759
`'train'` | 11499
`'validation'` | 3001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "ro"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


