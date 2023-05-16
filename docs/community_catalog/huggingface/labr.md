# labr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/labr)
*   [Huggingface](https://huggingface.co/datasets/labr)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:labr/plain_text')
```

*   **Description**:

```
This dataset contains over 63,000 book reviews in Arabic.It is the largest sentiment analysis dataset for Arabic to-date.The book reviews were harvested from the website Goodreads during the month or March 2013.Each book review comes with the goodreads review id, the user id, the book id, the rating (1 to 5) and the text of the review.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2935
`'train'` | 11760

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 5,
        "names": [
            "1",
            "2",
            "3",
            "4",
            "5"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


