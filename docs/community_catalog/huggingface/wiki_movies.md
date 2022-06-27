# wiki_movies

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_movies)
*   [Huggingface](https://huggingface.co/datasets/wiki_movies)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_movies')
```

*   **Description**:

```
The WikiMovies dataset consists of roughly 100k (templated) questions over 75k entities based on questions with answers in the open movie database (OMDb).
```

*   **License**: Creative Commons Public License (CCPL)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9952
`'train'` | 96185
`'validation'` | 10000

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


