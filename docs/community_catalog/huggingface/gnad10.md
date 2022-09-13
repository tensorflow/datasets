# gnad10

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/gnad10)
*   [Huggingface](https://huggingface.co/datasets/gnad10)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:gnad10')
```

*   **Description**:

```
This dataset is intended to advance topic classification for German texts. A classifier that is efffective in
English may not be effective in German dataset because it has a higher inflection and longer compound words.
The 10kGNAD dataset contains 10273 German news articles from an Austrian online newspaper categorized into
9 categories. Article titles and text are concatenated together and authors are removed to avoid a keyword-like
classification on authors that write frequently about one category. This dataset can be used as a benchmark
for German topic classification.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1028
`'train'` | 9245

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 9,
        "names": [
            "Web",
            "Panorama",
            "International",
            "Wirtschaft",
            "Sport",
            "Inland",
            "Etat",
            "Wissenschaft",
            "Kultur"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


