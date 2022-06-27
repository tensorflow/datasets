# scientific_papers

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/scientific_papers)
*   [Huggingface](https://huggingface.co/datasets/scientific_papers)


## arxiv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scientific_papers/arxiv')
```

*   **Description**:

```
Scientific papers datasets contains two sets of long and structured documents.
The datasets are obtained from ArXiv and PubMed OpenAccess repositories.

Both "arxiv" and "pubmed" have two features:
  - article: the body of the document, pagragraphs seperated by "/n".
  - abstract: the abstract of the document, pagragraphs seperated by "/n".
  - section_names: titles of sections, seperated by "/n".
```

*   **License**: No known license
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6440
`'train'` | 203037
`'validation'` | 6436

*   **Features**:

```json
{
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstract": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "section_names": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## pubmed


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scientific_papers/pubmed')
```

*   **Description**:

```
Scientific papers datasets contains two sets of long and structured documents.
The datasets are obtained from ArXiv and PubMed OpenAccess repositories.

Both "arxiv" and "pubmed" have two features:
  - article: the body of the document, pagragraphs seperated by "/n".
  - abstract: the abstract of the document, pagragraphs seperated by "/n".
  - section_names: titles of sections, seperated by "/n".
```

*   **License**: No known license
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6658
`'train'` | 119924
`'validation'` | 6633

*   **Features**:

```json
{
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstract": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "section_names": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


