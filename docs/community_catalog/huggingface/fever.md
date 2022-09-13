# fever

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/fever)
*   [Huggingface](https://huggingface.co/datasets/fever)


## v1.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:fever/v1.0')
```

*   **Description**:

```
With billions of individual pages on the web providing information on almost every conceivable topic, we should have the ability to collect facts that answer almost every conceivable question. However, only a small fraction of this information is contained in structured sources (Wikidata, Freebase, etc.) – we are therefore limited by our ability to transform free-form text to structured knowledge. There is, however, another problem that has become the focus of a lot of recent research and media coverage: false information coming from unreliable sources. [1] [2]

The FEVER workshops are a venue for work in verifiable knowledge extraction and to stimulate progress in this direction.

FEVER  V1.0
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'labelled_dev'` | 37566
`'paper_dev'` | 18999
`'paper_test'` | 18567
`'train'` | 311431
`'unlabelled_dev'` | 19998
`'unlabelled_test'` | 19998

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "evidence_annotation_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "evidence_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "evidence_wiki_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "evidence_sentence_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## v2.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:fever/v2.0')
```

*   **Description**:

```
With billions of individual pages on the web providing information on almost every conceivable topic, we should have the ability to collect facts that answer almost every conceivable question. However, only a small fraction of this information is contained in structured sources (Wikidata, Freebase, etc.) – we are therefore limited by our ability to transform free-form text to structured knowledge. There is, however, another problem that has become the focus of a lot of recent research and media coverage: false information coming from unreliable sources. [1] [2]

The FEVER workshops are a venue for work in verifiable knowledge extraction and to stimulate progress in this direction.

FEVER  V2.0
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 2384

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "evidence_annotation_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "evidence_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "evidence_wiki_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "evidence_sentence_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## wiki_pages


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:fever/wiki_pages')
```

*   **Description**:

```
With billions of individual pages on the web providing information on almost every conceivable topic, we should have the ability to collect facts that answer almost every conceivable question. However, only a small fraction of this information is contained in structured sources (Wikidata, Freebase, etc.) – we are therefore limited by our ability to transform free-form text to structured knowledge. There is, however, another problem that has become the focus of a lot of recent research and media coverage: false information coming from unreliable sources. [1] [2]

The FEVER workshops are a venue for work in verifiable knowledge extraction and to stimulate progress in this direction.

Wikipedia pages
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'wikipedia_pages'` | 5416537

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lines": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


