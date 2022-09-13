# squad_it

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/squad_it)
*   [Huggingface](https://huggingface.co/datasets/squad_it)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_it')
```

*   **Description**:

```
SQuAD-it is derived from the SQuAD dataset and it is obtained through semi-automatic translation of the SQuAD dataset
into Italian. It represents a large-scale dataset for open question answering processes on factoid questions in Italian.
 The dataset contains more than 60,000 question/answer pairs derived from the original English dataset. The dataset is
 split into training and test sets to support the replicability of the benchmarking of QA systems:
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7609
`'train'` | 54159

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
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


