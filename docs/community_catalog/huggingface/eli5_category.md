# eli5_category

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/eli5_category)
*   [Huggingface](https://huggingface.co/datasets/eli5_category)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:eli5_category')
```

*   **Description**:

```
The ELI5-Category dataset is a smaller but newer and categorized version of the original ELI5 dataset. After 2017, a tagging system was introduced to this subreddit so that the questions can be categorized into different topics according to their tags. Since the training and validation set is built by questions in different topics, the dataset is expected to alleviate the train/validation overlapping issue in the original ELI5 dataset.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5411
`'train'` | 91772
`'validation1'` | 5446
`'validation2'` | 2375

*   **Features**:

```json
{
    "q_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "selftext": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subreddit": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "a_id": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "text": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "score": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "text_urls": {
            "feature": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "title_urls": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "selftext_urls": {
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


