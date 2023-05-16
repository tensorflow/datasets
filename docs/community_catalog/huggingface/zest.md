# zest

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/zest)
*   [Huggingface](https://huggingface.co/datasets/zest)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:zest')
```

*   **Description**:

```
ZEST tests whether NLP systems can perform unseen tasks in a zero-shot way, given a natural language description of
the task. It is an instantiation of our proposed framework "learning from task descriptions". The tasks include
classification, typed entity extraction and relationship extraction, and each task is paired with 20 different
annotated (input, output) examples. ZEST's structure allows us to systematically test whether models can generalize
in five different ways.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11980
`'train'` | 10766
`'validation'` | 2280

*   **Features**:

```json
{
    "task_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "generalization_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "derives_from": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
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
    },
    "all_answers": {
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


