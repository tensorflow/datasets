# myanmar_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/myanmar_news)
*   [Huggingface](https://huggingface.co/datasets/myanmar_news)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:myanmar_news')
```

*   **Description**:

```
The Myanmar news dataset contains article snippets in four categories:
Business, Entertainment, Politics, and Sport.

These were collected in October 2017 by Aye Hninn Khine
```

*   **License**: GPL-3.0
*   **Version**: 1.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8116

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "num_classes": 4,
        "names": [
            "Sport",
            "Politic",
            "Business",
            "Entertainment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


