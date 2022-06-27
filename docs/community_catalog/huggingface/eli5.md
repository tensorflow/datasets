# eli5

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/eli5)
*   [Huggingface](https://huggingface.co/datasets/eli5)


## LFQA_reddit


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:eli5/LFQA_reddit')
```

*   **Description**:

```
Explain Like I'm 5 long form QA dataset
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test_askh'` | 9764
`'test_asks'` | 4462
`'test_eli5'` | 24512
`'train_askh'` | 98525
`'train_asks'` | 131778
`'train_eli5'` | 272634
`'validation_askh'` | 4901
`'validation_asks'` | 2281
`'validation_eli5'` | 9812

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
    "document": {
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
        "feature": {
            "a_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "score": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "title_urls": {
        "feature": {
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "selftext_urls": {
        "feature": {
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answers_urls": {
        "feature": {
            "url": {
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


