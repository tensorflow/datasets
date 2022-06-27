# app_reviews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/app_reviews)
*   [Huggingface](https://huggingface.co/datasets/app_reviews)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:app_reviews')
```

*   **Description**:

```
It is a large dataset of Android applications belonging to 23 differentapps categories, which provides an overview of the types of feedback users report on the apps and documents the evolution of the related code metrics. The dataset contains about 395 applications of the F-Droid repository, including around 600 versions, 280,000 user reviews (extracted with specific text mining approaches)
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 288065

*   **Features**:

```json
{
    "package_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "star": {
        "dtype": "int8",
        "id": null,
        "_type": "Value"
    }
}
```


