# reddit

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/reddit)
*   [Huggingface](https://huggingface.co/datasets/reddit)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:reddit')
```

*   **Description**:

```
This corpus contains preprocessed posts from the Reddit dataset.
The dataset consists of 3,848,330 posts with an average length of 270 words for content,
and 28 words for the summary.

Features includes strings: author, body, normalizedBody, content, summary, subreddit, subreddit_id.
Content is used as document and summary is used as summary.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3848330

*   **Features**:

```json
{
    "author": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "normalizedBody": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subreddit": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subreddit_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


