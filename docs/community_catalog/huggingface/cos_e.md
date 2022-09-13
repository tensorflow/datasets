# cos_e

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cos_e)
*   [Huggingface](https://huggingface.co/datasets/cos_e)


## v1.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cos_e/v1.0')
```

*   **Description**:

```
Common Sense Explanations (CoS-E) allows for training language models to
automatically generate explanations that can be used during training and
inference in a novel Commonsense Auto-Generated Explanation (CAGE) framework.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7610
`'validation'` | 950

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choices": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstractive_explanation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "extractive_explanation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## v1.11


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cos_e/v1.11')
```

*   **Description**:

```
Common Sense Explanations (CoS-E) allows for training language models to
automatically generate explanations that can be used during training and
inference in a novel Commonsense Auto-Generated Explanation (CAGE) framework.
```

*   **License**: No known license
*   **Version**: 1.11.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 9741
`'validation'` | 1221

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choices": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstractive_explanation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "extractive_explanation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


