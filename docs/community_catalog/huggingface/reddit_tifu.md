# reddit_tifu

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/reddit_tifu)
*   [Huggingface](https://huggingface.co/datasets/reddit_tifu)


## short


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:reddit_tifu/short')
```

*   **Description**:

```
Reddit dataset, where TIFU denotes the name of subbreddit /r/tifu.
As defined in the publication, styel "short" uses title as summary and
"long" uses tldr as summary.

Features includes:
  - document: post text without tldr.
  - tldr: tldr line.
  - title: trimmed title without tldr.
  - ups: upvotes.
  - score: score.
  - num_comments: number of comments.
  - upvote_ratio: upvote ratio.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 79740

*   **Features**:

```json
{
    "ups": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "num_comments": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "upvote_ratio": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "documents": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tldr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## long


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:reddit_tifu/long')
```

*   **Description**:

```
Reddit dataset, where TIFU denotes the name of subbreddit /r/tifu.
As defined in the publication, styel "short" uses title as summary and
"long" uses tldr as summary.

Features includes:
  - document: post text without tldr.
  - tldr: tldr line.
  - title: trimmed title without tldr.
  - ups: upvotes.
  - score: score.
  - num_comments: number of comments.
  - upvote_ratio: upvote ratio.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 42139

*   **Features**:

```json
{
    "ups": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "num_comments": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "upvote_ratio": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "documents": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tldr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


