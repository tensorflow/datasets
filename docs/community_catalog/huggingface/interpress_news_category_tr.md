# interpress_news_category_tr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/interpress_news_category_tr)
*   [Huggingface](https://huggingface.co/datasets/interpress_news_category_tr)


## 270k


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:interpress_news_category_tr/270k')
```

*   **Description**:

```
It is a Turkish news data set consisting of 273601 news in 17 categories, compiled from print media and news websites between 2010 and 2017 by the Interpress (https://www.interpress.com/) media monitoring company.
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
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
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
    "category": {
        "num_classes": 17,
        "names": [
            "aktuel",
            "bilisim",
            "egitim",
            "ekonomi",
            "gida",
            "iletisim",
            "kultursanat",
            "magazin",
            "saglik",
            "savunma",
            "seyahat",
            "siyasi",
            "spor",
            "teknoloji",
            "ticaret",
            "turizm",
            "yasam"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "categorycode": {
        "num_classes": 17,
        "names": [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "publishdatetime": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


