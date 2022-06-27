# turkish_movie_sentiment

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/turkish_movie_sentiment)
*   [Huggingface](https://huggingface.co/datasets/turkish_movie_sentiment)


## turkishmoviesentiment


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:turkish_movie_sentiment/turkishmoviesentiment')
```

*   **Description**:

```
This data set is a dataset from kaggle consisting of Turkish movie reviews and scored between 0-5.
```

*   **License**: CC0: Public Domain
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 83227

*   **Features**:

```json
{
    "point": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "comment": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "film_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


