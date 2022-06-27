# cnn_dailymail

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cnn_dailymail)
*   [Huggingface](https://huggingface.co/datasets/cnn_dailymail)


## 3.0.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cnn_dailymail/3.0.0')
```

*   **Description**:

```
CNN/DailyMail non-anonymized summarization dataset.

There are two features:
  - article: text of news article, used as the document to be summarized
  - highlights: joined text of highlights with <s> and </s> around each
    highlight, which is the target summary
```

*   **License**: No known license
*   **Version**: 3.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11490
`'train'` | 287113
`'validation'` | 13368

*   **Features**:

```json
{
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "highlights": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 1.0.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cnn_dailymail/1.0.0')
```

*   **Description**:

```
CNN/DailyMail non-anonymized summarization dataset.

There are two features:
  - article: text of news article, used as the document to be summarized
  - highlights: joined text of highlights with <s> and </s> around each
    highlight, which is the target summary
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11490
`'train'` | 287113
`'validation'` | 13368

*   **Features**:

```json
{
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "highlights": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## 2.0.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cnn_dailymail/2.0.0')
```

*   **Description**:

```
CNN/DailyMail non-anonymized summarization dataset.

There are two features:
  - article: text of news article, used as the document to be summarized
  - highlights: joined text of highlights with <s> and </s> around each
    highlight, which is the target summary
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11490
`'train'` | 287113
`'validation'` | 13368

*   **Features**:

```json
{
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "highlights": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


