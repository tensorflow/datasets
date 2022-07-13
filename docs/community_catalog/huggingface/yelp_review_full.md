# yelp_review_full

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/yelp_review_full)
*   [Huggingface](https://huggingface.co/datasets/yelp_review_full)


## yelp_review_full


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:yelp_review_full/yelp_review_full')
```

*   **Description**:

```
The Yelp reviews dataset consists of reviews from Yelp. It is extracted from the Yelp Dataset Challenge 2015 data.
The Yelp reviews full star dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the above dataset.
It is first used as a text classification benchmark in the following paper: Xiang Zhang, Junbo Zhao, Yann LeCun.
Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).
```

*   **License**: https://s3-media3.fl.yelpcdn.com/assets/srv0/engineering_pages/bea5c1e92bf3/assets/vendor/yelp-dataset-agreement.pdf
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 50000
`'train'` | 650000

*   **Features**:

```json
{
    "label": {
        "num_classes": 5,
        "names": [
            "1 star",
            "2 star",
            "3 stars",
            "4 stars",
            "5 stars"
        ],
        "id": null,
        "_type": "ClassLabel"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


