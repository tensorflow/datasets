# x_stance

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/x_stance)
*   [Huggingface](https://huggingface.co/datasets/x_stance)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:x_stance')
```

*   **Description**:

```
The x-stance dataset contains more than 150 political questions, and 67k comments written by candidates on those questions.

It can be used to train and evaluate stance detection systems.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 17705
`'train'` | 45640
`'validation'` | 3926

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "comment": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "numerical_label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "author": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


