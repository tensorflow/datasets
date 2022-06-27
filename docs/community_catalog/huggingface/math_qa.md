# math_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/math_qa)
*   [Huggingface](https://huggingface.co/datasets/math_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:math_qa')
```

*   **Description**:

```
Our dataset is gathered by using a new representation language to annotate over the AQuA-RAT dataset. AQuA-RAT has provided the questions, options, rationale, and the correct options.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2985
`'train'` | 29837
`'validation'` | 4475

*   **Features**:

```json
{
    "Problem": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Rationale": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotated_formula": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "linear_formula": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


