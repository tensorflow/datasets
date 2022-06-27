# wiqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiqa)
*   [Huggingface](https://huggingface.co/datasets/wiqa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiqa')
```

*   **Description**:

```
The WIQA dataset V1 has 39705 questions containing a perturbation and a possible effect in the context of a paragraph. 
The dataset is split into 29808 train questions, 6894 dev questions and 3003 test questions.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3003
`'train'` | 29808
`'validation'` | 6894

*   **Features**:

```json
{
    "question_stem": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_para_step": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_label_as_choice": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choices": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "label": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "metadata_question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "metadata_graph_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "metadata_para_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "metadata_question_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "metadata_path_len": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


