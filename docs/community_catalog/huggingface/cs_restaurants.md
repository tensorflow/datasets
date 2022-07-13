# cs_restaurants

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cs_restaurants)
*   [Huggingface](https://huggingface.co/datasets/cs_restaurants)


## CSRestaurants


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cs_restaurants/CSRestaurants')
```

*   **Description**:

```
This is a dataset for NLG in task-oriented spoken dialogue systems with Czech as the target language. It originated as 
a translation of the English San Francisco Restaurants dataset by Wen et al. (2015).
```

*   **License**: Creative Commons 4.0 BY-SA
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 842
`'train'` | 3569
`'validation'` | 781

*   **Features**:

```json
{
    "dialogue_act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "delexicalized_dialogue_act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "delexicalized_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


