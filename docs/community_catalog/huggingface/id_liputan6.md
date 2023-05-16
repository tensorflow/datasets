# id_liputan6

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/id_liputan6)
*   [Huggingface](https://huggingface.co/datasets/id_liputan6)


## canonical


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:id_liputan6/canonical')
```

*   **Description**:

```
In this paper, we introduce a large-scale Indonesian summarization dataset. We harvest articles from this http URL,
an online news portal, and obtain 215,827 document-summary pairs. We leverage pre-trained language models to develop
benchmark extractive and abstractive summarization methods over the dataset with multilingual and monolingual
BERT-based models. We include a thorough error analysis by examining machine-generated summaries that have
low ROUGE scores, and expose both issues with ROUGE it-self, as well as with extractive and abstractive
summarization models.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10972
`'train'` | 193883
`'validation'` | 10972

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "clean_article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "clean_summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "extractive_summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## xtreme


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:id_liputan6/xtreme')
```

*   **Description**:

```
In this paper, we introduce a large-scale Indonesian summarization dataset. We harvest articles from this http URL,
an online news portal, and obtain 215,827 document-summary pairs. We leverage pre-trained language models to develop
benchmark extractive and abstractive summarization methods over the dataset with multilingual and monolingual
BERT-based models. We include a thorough error analysis by examining machine-generated summaries that have
low ROUGE scores, and expose both issues with ROUGE it-self, as well as with extractive and abstractive
summarization models.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3862
`'validation'` | 4948

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "clean_article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "clean_summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "extractive_summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


