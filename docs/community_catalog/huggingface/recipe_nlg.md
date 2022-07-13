# recipe_nlg

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/recipe_nlg)
*   [Huggingface](https://huggingface.co/datasets/recipe_nlg)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:recipe_nlg')
```

*   **Description**:

```
The dataset contains 2231142 cooking recipes (>2 millions). It's processed in more careful way and provides more samples than any other dataset in the area.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2231142

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ingredients": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "directions": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "link": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "num_classes": 2,
        "names": [
            "Gathered",
            "Recipes1M"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "ner": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


