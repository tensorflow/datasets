# multi_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multi_news)
*   [Huggingface](https://huggingface.co/datasets/multi_news)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_news')
```

*   **Description**:

```
Multi-News, consists of news articles and human-written summaries
of these articles from the site newser.com.
Each summary is professionally written by editors and
includes links to the original articles cited.

There are two features:
  - document: text of news articles seperated by special token "|||||".
  - summary: news summary.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5622
`'train'` | 44972
`'validation'` | 5622

*   **Features**:

```json
{
    "document": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


