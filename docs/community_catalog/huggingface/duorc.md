# duorc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/duorc)
*   [Huggingface](https://huggingface.co/datasets/duorc)


## SelfRC


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:duorc/SelfRC')
```

*   **Description**:

```
DuoRC contains 186,089 unique question-answer pairs created from a collection of 7680 pairs of movie plots where each pair in the collection reflects two versions of the same movie.
```

*   **License**: https://raw.githubusercontent.com/duorc/duorc/master/LICENSE
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 12559
`'train'` | 60721
`'validation'` | 12961

*   **Features**:

```json
{
    "plot_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "plot": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
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
    },
    "no_answer": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    }
}
```



## ParaphraseRC


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:duorc/ParaphraseRC')
```

*   **Description**:

```
DuoRC contains 186,089 unique question-answer pairs created from a collection of 7680 pairs of movie plots where each pair in the collection reflects two versions of the same movie.
```

*   **License**: https://raw.githubusercontent.com/duorc/duorc/master/LICENSE
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15857
`'train'` | 69524
`'validation'` | 15591

*   **Features**:

```json
{
    "plot_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "plot": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
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
    },
    "no_answer": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    }
}
```


