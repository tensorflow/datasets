# nq_open

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/nq_open)
*   [Huggingface](https://huggingface.co/datasets/nq_open)


## nq_open


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nq_open/nq_open')
```

*   **Description**:

```
The NQ-Open task, introduced by Lee et.al. 2019,
is an open domain question answering benchmark that is derived from Natural Questions.
The goal is to predict an English answer string for an input English question.
All questions can be answered using the contents of English Wikipedia.
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 87925
`'validation'` | 3610

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


