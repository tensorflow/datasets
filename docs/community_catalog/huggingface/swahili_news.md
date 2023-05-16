# swahili_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/swahili_news)
*   [Huggingface](https://huggingface.co/datasets/swahili_news)


## swahili_news


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swahili_news/swahili_news')
```

*   **Description**:

```
Swahili is spoken by 100-150 million people across East Africa. In Tanzania, it is one of two national languages (the other is English) and it is the official language of instruction in all schools. News in Swahili is an important part of the media sphere in Tanzania.

News contributes to education, technology, and the economic growth of a country, and news in local languages plays an important cultural role in many Africa countries. In the modern age, African languages in news and other spheres are at risk of being lost as English becomes the dominant language in online spaces.

The Swahili news dataset was created to reduce the gap of using the Swahili language to create NLP technologies and help AI practitioners in Tanzania and across Africa continent to practice their NLP skills to solve different problems in organizations or societies related to Swahili language. Swahili News were collected from different websites that provide news in the Swahili language. I was able to find some websites that provide news in Swahili only and others in different languages including Swahili.

The dataset was created for a specific task of text classification, this means each news content can be categorized into six different topics (Local news, International news , Finance news, Health news, Sports news, and Entertainment news). The dataset comes with a specified train/test split. The train set contains 75% of the dataset and test set contains 25% of the dataset.
```

*   **License**: Creative Commons Attribution 4.0 International
*   **Version**: 0.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7338
`'train'` | 22207

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 6,
        "names": [
            "uchumi",
            "kitaifa",
            "michezo",
            "kimataifa",
            "burudani",
            "afya"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


