# coarse_discourse

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/coarse_discourse)
*   [Huggingface](https://huggingface.co/datasets/coarse_discourse)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:coarse_discourse')
```

*   **Description**:

```
dataset contains discourse annotation and relation on threads from reddit during 2016
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 116357

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "is_self_post": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "subreddit": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "majority_link": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "is_first_post": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "majority_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id_post": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "post_depth": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "in_reply_to": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotations": {
        "feature": {
            "annotator": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "link_to_post": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "main_type": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


