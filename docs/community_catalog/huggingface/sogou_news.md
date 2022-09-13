# sogou_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sogou_news)
*   [Huggingface](https://huggingface.co/datasets/sogou_news)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sogou_news')
```

*   **Description**:

```
The Sogou News dataset is a mixture of 2,909,551 news articles from the SogouCA and SogouCS news corpora, in 5 categories. 
The number of training samples selected for each class is 90,000 and testing 12,000. Note that the Chinese characters have been converted to Pinyin.
classification labels of the news are determined by their domain names in the URL. For example, the news with
URL http://sports.sohu.com is categorized as a sport class.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 60000
`'train'` | 450000

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 5,
        "names": [
            "sports",
            "finance",
            "entertainment",
            "automobile",
            "technology"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


