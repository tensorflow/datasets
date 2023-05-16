# laroseda

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/laroseda)
*   [Huggingface](https://huggingface.co/datasets/laroseda)


## laroseda


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:laroseda/laroseda')
```

*   **Description**:

```
LaRoSeDa (A Large Romanian Sentiment Data Set) contains 15,000 reviews written in Romanian, of which 7,500 are positive and 7,500 negative.
        Star ratings of 1 and 2 and of 4 and 5 are provided for negative and positive reviews respectively.
        The current dataset uses star rating as the label for multi-class classification.
```

*   **License**: CC BY-SA 4.0 License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3000
`'train'` | 12000

*   **Features**:

```json
{
    "index": {
        "dtype": "string",
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
    "starRating": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    }
}
```


