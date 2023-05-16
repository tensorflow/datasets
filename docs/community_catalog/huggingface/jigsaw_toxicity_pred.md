# jigsaw_toxicity_pred

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/jigsaw_toxicity_pred)
*   [Huggingface](https://huggingface.co/datasets/jigsaw_toxicity_pred)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:jigsaw_toxicity_pred')
```

*   **Description**:

```
This dataset consists of a large number of Wikipedia comments which have been labeled by human raters for toxic behavior.
```

*   **License**: The "Toxic Comment Classification" dataset is released under CC0, with the underlying comment text being governed by Wikipedia's CC-SA-3.0.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 63978
`'train'` | 159571

*   **Features**:

```json
{
    "comment_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "toxic": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "severe_toxic": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "obscene": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "threat": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "insult": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "identity_hate": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


