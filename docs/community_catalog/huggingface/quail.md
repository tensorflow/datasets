# quail

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/quail)
*   [Huggingface](https://huggingface.co/datasets/quail)


## quail


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:quail/quail')
```

*   **Description**:

```
QuAIL is a  reading comprehension dataset. QuAIL contains 15K multi-choice questions in texts 300-350 tokens long 4 domains (news, user stories, fiction, blogs).QuAIL is balanced and annotated for question types.
```

*   **License**: No known license
*   **Version**: 1.3.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'challenge'` | 556
`'train'` | 10246
`'validation'` | 2164

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "metadata": {
        "author": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "title": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
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
    "question_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


