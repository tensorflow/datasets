# esnli

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/esnli)
*   [Huggingface](https://huggingface.co/datasets/esnli)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:esnli/plain_text')
```

*   **Description**:

```
The e-SNLI dataset extends the Stanford Natural Language Inference Dataset to
include human-annotated natural language explanations of the entailment
relations.
```

*   **License**: No known license
*   **Version**: 0.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9824
`'train'` | 549367
`'validation'` | 9842

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
    "explanation_1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "explanation_2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "explanation_3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


