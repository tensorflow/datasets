# cosmos_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cosmos_qa)
*   [Huggingface](https://huggingface.co/datasets/cosmos_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cosmos_qa')
```

*   **Description**:

```
Cosmos QA is a large-scale dataset of 35.6K problems that require commonsense-based reading comprehension, formulated as multiple-choice questions. It focuses on reading between the lines over a diverse collection of people's everyday narratives, asking questions concerning on the likely causes or effects of events that require reasoning beyond the exact text spans in the context
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6963
`'train'` | 25262
`'validation'` | 2985

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer0": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


