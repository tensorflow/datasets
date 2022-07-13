# poem_sentiment

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/poem_sentiment)
*   [Huggingface](https://huggingface.co/datasets/poem_sentiment)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:poem_sentiment')
```

*   **Description**:

```
Poem Sentiment is a sentiment dataset of poem verses from Project Gutenberg. This dataset can be used for tasks such as sentiment classification or style transfer for poems.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 104
`'train'` | 892
`'validation'` | 105

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "verse_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "negative",
            "positive",
            "no_impact"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


