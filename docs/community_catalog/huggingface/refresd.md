# refresd

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/refresd)
*   [Huggingface](https://huggingface.co/datasets/refresd)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:refresd')
```

*   **Description**:

```
The Rationalized English-French Semantic Divergences (REFreSD) dataset consists of 1,039 
English-French sentence-pairs annotated with sentence-level divergence judgments and token-level 
rationales. For any questions, write to ebriakou@cs.umd.edu.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1039

*   **Features**:

```json
{
    "sentence_en": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_fr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "divergent",
            "equivalent"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "all_labels": {
        "num_classes": 3,
        "names": [
            "unrelated",
            "some_meaning_difference",
            "no_meaning_difference"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "rationale_en": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rationale_fr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


