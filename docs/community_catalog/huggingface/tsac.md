# tsac

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tsac)
*   [Huggingface](https://huggingface.co/datasets/tsac)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tsac')
```

*   **Description**:

```
Tunisian Sentiment Analysis Corpus.

About 17k user comments manually annotated to positive and negative polarities. This corpus is collected from Facebook users comments written on official pages of Tunisian radios and TV channels namely Mosaique FM, JawhraFM, Shemes FM, HiwarElttounsi TV and Nessma TV. The corpus is collected from a period spanning January 2015 until June 2016.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3400
`'train'` | 13669

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "num_classes": 2,
        "names": [
            "1",
            "-1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


