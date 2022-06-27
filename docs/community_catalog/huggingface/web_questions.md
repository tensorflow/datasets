# web_questions

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/web_questions)
*   [Huggingface](https://huggingface.co/datasets/web_questions)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:web_questions')
```

*   **Description**:

```
This dataset consists of 6,642 question/answer pairs.
The questions are supposed to be answerable by Freebase, a large knowledge graph.
The questions are mostly centered around a single named entity.
The questions are popular ones asked on the web (at least in 2013).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2032
`'train'` | 3778

*   **Features**:

```json
{
    "url": {
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


