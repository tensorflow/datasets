# hatexplain

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hatexplain)
*   [Huggingface](https://huggingface.co/datasets/hatexplain)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hatexplain/plain_text')
```

*   **Description**:

```
Hatexplain is the first benchmark hate speech dataset covering multiple aspects of the issue. Each post in the dataset is annotated from three different perspectives: the basic, commonly used 3-class classification (i.e., hate, offensive or normal), the target community (i.e., the community that has been the victim of hate speech/offensive speech in the post), and the rationales, i.e., the portions of the post on which their labelling decision (as hate, offensive or normal) is based.
```

*   **License**: cc-by-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1924
`'train'` | 15383
`'validation'` | 1922

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotators": {
        "feature": {
            "label": {
                "num_classes": 3,
                "names": [
                    "hatespeech",
                    "normal",
                    "offensive"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "annotator_id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "target": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "rationales": {
        "feature": {
            "feature": {
                "dtype": "int32",
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
    },
    "post_tokens": {
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


