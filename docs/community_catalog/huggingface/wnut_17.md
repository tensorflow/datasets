# wnut_17

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wnut_17)
*   [Huggingface](https://huggingface.co/datasets/wnut_17)


## wnut_17


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wnut_17/wnut_17')
```

*   **Description**:

```
WNUT 17: Emerging and Rare entity recognition

This shared task focuses on identifying unusual, previously-unseen entities in the context of emerging discussions.
Named entities form the basis of many modern approaches to other tasks (like event clustering and summarisation),
but recall on them is a real problem in noisy text - even among annotators. This drop tends to be due to novel entities and surface forms.
Take for example the tweet “so.. kktny in 30 mins?” - even human experts find entity kktny hard to detect and resolve.
This task will evaluate the ability to detect and classify novel, emerging, singleton named entities in noisy text.

The goal of this task is to provide a definition of emerging and of rare entities, and based on that, also datasets for detecting these entities.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1287
`'train'` | 3394
`'validation'` | 1009

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 13,
            "names": [
                "O",
                "B-corporation",
                "I-corporation",
                "B-creative-work",
                "I-creative-work",
                "B-group",
                "I-group",
                "B-location",
                "I-location",
                "B-person",
                "I-person",
                "B-product",
                "I-product"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


