# per_sent

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/per_sent)
*   [Huggingface](https://huggingface.co/datasets/per_sent)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:per_sent')
```

*   **Description**:

```
Person SenTiment (PerSenT) is a crowd-sourced dataset that captures the sentiment of an author towards the main entity in a news article. This dataset contains annotation for 5.3k documents and 38k paragraphs covering 3.2k unique entities.

The dataset consists of sentiment annotations on news articles about people. For each article, annotators judge what the author’s sentiment is towards the main (target) entity of the article. The annotations also include similar judgments on paragraphs within the article.

To split the dataset, entities into 4 mutually exclusive sets. Due to the nature of news collections, some entities tend to dominate the collection. In the collection, there were four entities which were the main entity in nearly 800 articles. To avoid these entities from dominating the train or test splits, we moved them to a separate test collection. We split the remaining into a training, dev, and test sets at random. Thus our collection includes one standard test set consisting of articles drawn at random (Test Standard -- `test_random`), while the other is a test set which contains multiple articles about a small number of popular entities (Test Frequent -- `test_fixed`).
```

*   **License**: Creative Commons Attribution 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test_fixed'` | 827
`'test_random'` | 579
`'train'` | 3355
`'validation'` | 578

*   **Features**:

```json
{
    "DOCUMENT_INDEX": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "TITLE": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "TARGET_ENTITY": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "DOCUMENT": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "MASKED_DOCUMENT": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "TRUE_SENTIMENT": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph0": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph1": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph2": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph3": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph4": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph5": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph6": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph7": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph8": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph9": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph10": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph11": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph12": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph13": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph14": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Paragraph15": {
        "num_classes": 3,
        "names": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


