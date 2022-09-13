# hausa_voa_topics

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hausa_voa_topics)
*   [Huggingface](https://huggingface.co/datasets/hausa_voa_topics)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hausa_voa_topics')
```

*   **Description**:

```
A collection of news article headlines in Hausa from VOA Hausa.
Each headline is labeled with one of the following classes: Nigeria,
Africa, World, Health or Politics.

The dataset was presented in the paper:
Hedderich, Adelani, Zhu, Alabi, Markus, Klakow: Transfer Learning and
Distant Supervision for Multilingual Transformer Models: A Study on
African Languages (EMNLP 2020).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 582
`'train'` | 2045
`'validation'` | 290

*   **Features**:

```json
{
    "news_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 5,
        "names": [
            "Africa",
            "Health",
            "Nigeria",
            "Politics",
            "World"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


