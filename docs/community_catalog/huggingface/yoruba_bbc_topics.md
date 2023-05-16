# yoruba_bbc_topics

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/yoruba_bbc_topics)
*   [Huggingface](https://huggingface.co/datasets/yoruba_bbc_topics)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:yoruba_bbc_topics')
```

*   **Description**:

```
A collection of news article headlines in Yoruba from BBC Yoruba.
Each headline is labeled with one of the following classes: africa,
entertainment, health, nigeria, politics, sport or world.

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
`'test'` | 379
`'train'` | 1340
`'validation'` | 189

*   **Features**:

```json
{
    "news_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 7,
        "names": [
            "africa",
            "entertainment",
            "health",
            "nigeria",
            "politics",
            "sport",
            "world"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bbc_url_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


