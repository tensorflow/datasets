# anli

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/anli)
*   [Huggingface](https://huggingface.co/datasets/anli)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:anli/plain_text')
```

*   **Description**:

```
The Adversarial Natural Language Inference (ANLI) is a new large-scale NLI benchmark dataset, 
The dataset is collected via an iterative, adversarial human-and-model-in-the-loop procedure.
ANLI is much more difficult than its predecessors including SNLI and MNLI.
It contains three rounds. Each round has train/dev/test splits.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev_r1'` | 1000
`'dev_r2'` | 1000
`'dev_r3'` | 1200
`'test_r1'` | 1000
`'test_r2'` | 1000
`'test_r3'` | 1200
`'train_r1'` | 16946
`'train_r2'` | 45460
`'train_r3'` | 100459

*   **Features**:

```json
{
    "uid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "reason": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


