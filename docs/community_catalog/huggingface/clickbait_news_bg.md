# clickbait_news_bg

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/clickbait_news_bg)
*   [Huggingface](https://huggingface.co/datasets/clickbait_news_bg)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clickbait_news_bg')
```

*   **Description**:

```
Dataset with clickbait and fake news in Bulgarian. Introduced for the Hack the Fake News 2017.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2815
`'validation'` | 761

*   **Features**:

```json
{
    "fake_news_score": {
        "num_classes": 2,
        "names": [
            "legitimate",
            "fake"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "click_bait_score": {
        "num_classes": 2,
        "names": [
            "normal",
            "clickbait"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "content_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content_published_time": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


