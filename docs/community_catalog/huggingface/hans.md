# hans

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hans)
*   [Huggingface](https://huggingface.co/datasets/hans)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hans/plain_text')
```

*   **Description**:

```
The HANS dataset is an NLI evaluation set that tests specific hypotheses about invalid heuristics that NLI models are likely to learn.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 30000
`'validation'` | 30000

*   **Features**:

```json
{
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
        "num_classes": 2,
        "names": [
            "entailment",
            "non-entailment"
        ],
        "id": null,
        "_type": "ClassLabel"
    },
    "parse_premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "parse_hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "binary_parse_premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "binary_parse_hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "heuristic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subcase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "template": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


