# cc_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cc_news)
*   [Huggingface](https://huggingface.co/datasets/cc_news)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cc_news/plain_text')
```

*   **Description**:

```
CC-News containing news articles from news sites all over the world The data is available on AWS S3 in the Common Crawl bucket at /crawl-data/CC-NEWS/. This version of the dataset has 708241 articles. It represents a small portion of English  language subset of the CC-News dataset created using news-please(Hamborg et al.,2017) to collect and extract English language portion of CC-News.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 708241

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "image_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


