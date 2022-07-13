# urdu_fake_news

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/urdu_fake_news)
*   [Huggingface](https://huggingface.co/datasets/urdu_fake_news)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:urdu_fake_news')
```

*   **Description**:

```
Urdu fake news datasets that contain news of 5 different news domains.
These domains are Sports, Health, Technology, Entertainment, and Business.
The real news are collected by combining manual approaches.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 262
`'train'` | 638

*   **Features**:

```json
{
    "news": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "Fake",
            "Real"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "category": {
        "num_classes": 5,
        "names": [
            "bus",
            "hlth",
            "sp",
            "tch",
            "sbz"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


