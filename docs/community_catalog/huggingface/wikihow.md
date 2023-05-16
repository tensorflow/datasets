# wikihow

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wikihow)
*   [Huggingface](https://huggingface.co/datasets/wikihow)


## all


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikihow/all')
```

*   **Description**:

```
WikiHow is a new large-scale dataset using the online WikiHow
(http://www.wikihow.com/) knowledge base.

There are two features:
  - text: wikihow answers texts.
  - headline: bold lines as summary.

There are two separate versions:
  - all: consisting of the concatenation of all paragraphs as the articles and
         the bold lines as the reference summaries.
  - sep: consisting of each paragraph and its summary.

Download "wikihowAll.csv" and "wikihowSep.csv" from
https://github.com/mahnazkoupaee/WikiHow-Dataset and place them in manual folder
https://www.tensorflow.org/datasets/api_docs/python/tfds/download/DownloadConfig.
Train/validation/test splits are provided by the authors.
Preprocessing is applied to remove short articles
(abstract length < 0.75 article length) and clean up extra commas.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5577
`'train'` | 157252
`'validation'` | 5599

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "headline": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## sep


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikihow/sep')
```

*   **Description**:

```
WikiHow is a new large-scale dataset using the online WikiHow
(http://www.wikihow.com/) knowledge base.

There are two features:
  - text: wikihow answers texts.
  - headline: bold lines as summary.

There are two separate versions:
  - all: consisting of the concatenation of all paragraphs as the articles and
         the bold lines as the reference summaries.
  - sep: consisting of each paragraph and its summary.

Download "wikihowAll.csv" and "wikihowSep.csv" from
https://github.com/mahnazkoupaee/WikiHow-Dataset and place them in manual folder
https://www.tensorflow.org/datasets/api_docs/python/tfds/download/DownloadConfig.
Train/validation/test splits are provided by the authors.
Preprocessing is applied to remove short articles
(abstract length < 0.75 article length) and clean up extra commas.
```

*   **License**: No known license
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 37800
`'train'` | 1060732
`'validation'` | 37932

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "headline": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "overview": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sectionLabel": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


