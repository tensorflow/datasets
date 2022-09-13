# gap

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/gap)
*   [Huggingface](https://huggingface.co/datasets/gap)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:gap')
```

*   **Description**:

```
GAP is a gender-balanced dataset containing 8,908 coreference-labeled pairs of
(ambiguous pronoun, antecedent name), sampled from Wikipedia and released by
Google AI Language for the evaluation of coreference resolution in practical
applications.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 2000
`'validation'` | 454

*   **Features**:

```json
{
    "ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Pronoun": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Pronoun-offset": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "A": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "A-offset": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "A-coref": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "B": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "B-offset": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "B-coref": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "URL": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


