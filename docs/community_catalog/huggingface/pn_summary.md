# pn_summary

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/pn_summary)
*   [Huggingface](https://huggingface.co/datasets/pn_summary)


## 1.0.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pn_summary/1.0.0')
```

*   **Description**:

```
A well-structured summarization dataset for the Persian language consists of 93,207 records. It is prepared for Abstractive/Extractive tasks (like cnn_dailymail for English). It can also be used in other scopes like Text Generation, Title Generation, and News Category Classification.
It is imperative to consider that the newlines were replaced with the `[n]` symbol. Please interpret them into normal newlines (for ex. `t.replace("[n]", "
")`) and then use them for your purposes.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5593
`'train'` | 82022
`'validation'` | 5592

*   **Features**:

```json
{
    "id": {
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
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "num_classes": 18,
        "names": [
            "Economy",
            "Roads-Urban",
            "Banking-Insurance",
            "Agriculture",
            "International",
            "Oil-Energy",
            "Industry",
            "Transportation",
            "Science-Technology",
            "Local",
            "Sports",
            "Politics",
            "Art-Culture",
            "Society",
            "Health",
            "Research",
            "Education-University",
            "Tourism"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "categories": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "network": {
        "num_classes": 6,
        "names": [
            "Tahlilbazaar",
            "Imna",
            "Shana",
            "Mehr",
            "Irna",
            "Khabaronline"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "link": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


