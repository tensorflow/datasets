# newsroom

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/newsroom)
*   [Huggingface](https://huggingface.co/datasets/newsroom)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:newsroom')
```

*   **Description**:

```
NEWSROOM is a large dataset for training and evaluating summarization systems.
It contains 1.3 million articles and summaries written by authors and
editors in the newsrooms of 38 major publications.

Dataset features includes:
  - text: Input news text.
  - summary: Summary for the news.
And additional features:
  - title: news title.
  - url: url of the news.
  - date: date of the article.
  - density: extractive density.
  - coverage: extractive coverage.
  - compression: compression ratio.
  - density_bin: low, medium, high.
  - coverage_bin: extractive, abstractive.
  - compression_bin: low, medium, high.

This dataset can be downloaded upon requests. Unzip all the contents
"train.jsonl, dev.josnl, test.jsonl" to the tfds folder.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 108862
`'train'` | 995041
`'validation'` | 108837

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "density_bin": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "coverage_bin": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "compression_bin": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "density": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "coverage": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "compression": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


