# interpress_news_category_tr_lite

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/interpress_news_category_tr_lite)
*   [Huggingface](https://huggingface.co/datasets/interpress_news_category_tr_lite)


## 270k_10class


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:interpress_news_category_tr_lite/270k_10class')
```

*   **Description**:

```
It is a Turkish news data set consisting of 273601 news in 10 categories, compiled from print media and news websites between 2010 and 2017 by the Interpress (https://www.interpress.com/) media monitoring company. It has been rearranged as easily separable and with fewer classes.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 54721
`'train'` | 218880

*   **Features**:

```json
{
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "num_classes": 10,
        "names": [
            "k\u00fclt\u00fcrsanat",
            "ekonomi",
            "siyaset",
            "e\u011fitim",
            "d\u00fcnya",
            "spor",
            "teknoloji",
            "magazin",
            "sa\u011fl\u0131k",
            "g\u00fcndem"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


