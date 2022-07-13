# imdb_urdu_reviews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/imdb_urdu_reviews)
*   [Huggingface](https://huggingface.co/datasets/imdb_urdu_reviews)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imdb_urdu_reviews')
```

*   **Description**:

```
Large Movie translated Urdu Reviews Dataset.
This is a dataset for binary sentiment classification containing substantially more data than previous
benchmark datasets. We provide a set of 40,000 highly polar movie reviews for training, and 10,000 for testing.
To increase the availability of sentiment analysis dataset for a low recourse language like Urdu,
we opted to use the already available IMDB Dataset. we have translated this dataset using google translator.
This is a binary classification dataset having two classes as positive and negative.
The reason behind using this dataset is high polarity for each class.
It contains 50k samples equally divided in two classes.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 50000

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentiment": {
        "num_classes": 2,
        "names": [
            "positive",
            "negative"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


