# kannada_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kannada_news)
*   [Huggingface](https://huggingface.co/datasets/kannada_news)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kannada_news')
```

*   **Description**:

```
The Kannada news dataset contains only the headlines of news article in three categories:
Entertainment, Tech, and Sports.

The data set contains around 6300 news article headlines which collected from Kannada news websites.
The data set has been cleaned and contains train and test set using which can be used to benchmark
classification models in Kannada.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5167
`'validation'` | 1293

*   **Features**:

```json
{
    "headline": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "sports",
            "tech",
            "entertainment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


