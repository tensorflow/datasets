# squad_v2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/squad_v2)
*   [Huggingface](https://huggingface.co/datasets/squad_v2)


## squad_v2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_v2/squad_v2')
```

*   **Description**:

```
combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers
 to look similar to answerable ones. To do well on SQuAD2.0, systems must not only answer questions when possible, but
 also determine when no answer is supported by the paragraph and abstain from answering.
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 130319
`'validation'` | 11873

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
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


