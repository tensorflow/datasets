# aquamuse

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/aquamuse)
*   [Huggingface](https://huggingface.co/datasets/aquamuse)


## abstractive


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:aquamuse/abstractive')
```

*   **Description**:

```
AQuaMuSe is a novel scalable approach to automatically mine dual query based multi-document summarization datasets for extractive and abstractive summaries using question answering dataset (Google Natural Questions) and large document corpora (Common Crawl)
```

*   **License**: No known license
*   **Version**: 2.3.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 811
`'train'` | 6253
`'validation'` | 661

*   **Features**:

```json
{
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_urls": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "target": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## extractive


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:aquamuse/extractive')
```

*   **Description**:

```
AQuaMuSe is a novel scalable approach to automatically mine dual query based multi-document summarization datasets for extractive and abstractive summaries using question answering dataset (Google Natural Questions) and large document corpora (Common Crawl)
```

*   **License**: No known license
*   **Version**: 2.3.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 811
`'train'` | 6253
`'validation'` | 661

*   **Features**:

```json
{
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_urls": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "target": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


