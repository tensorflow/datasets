# qanta

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/qanta)
*   [Huggingface](https://huggingface.co/datasets/qanta)


## mode=first,char_skip=25


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qanta/mode=first,char_skip=25')
```

*   **Description**:

```
The Qanta dataset is a question answering dataset based on the academic trivia game Quizbowl.
```

*   **License**: No known license
*   **Version**: 2018.04.18
*   **Splits**:

Split  | Examples
:----- | -------:
`'adversarial'` | 1145
`'buzzdev'` | 1161
`'buzztest'` | 1953
`'buzztrain'` | 16706
`'guessdev'` | 1055
`'guesstest'` | 2151
`'guesstrain'` | 96221

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "qanta_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "proto_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "qdb_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dataset": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "full_question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "first_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "char_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "sentence_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "tokenizations": {
        "feature": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": 2,
            "id": null,
            "_type": "Sequence"
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
    "page": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "raw_answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fold": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gameplay": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subcategory": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tournament": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "difficulty": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


