# wiki_summary

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_summary)
*   [Huggingface](https://huggingface.co/datasets/wiki_summary)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_summary')
```

*   **Description**:

```
The dataset extracted from Persian Wikipedia into the form of articles and highlights and cleaned the dataset into pairs of articles and highlights and reduced the articles' length (only version 1.0.0) and highlights' length to a maximum of 512 and 128, respectively, suitable for parsBERT.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5638
`'train'` | 45654
`'validation'` | 5074

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "link": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "highlights": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


