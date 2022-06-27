# neural_code_search

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/neural_code_search)
*   [Huggingface](https://huggingface.co/datasets/neural_code_search)


## evaluation_dataset


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:neural_code_search/evaluation_dataset')
```

*   **Description**:

```
Neural-Code-Search-Evaluation-Dataset presents an evaluation dataset consisting of natural language query and code snippet pairs and a search corpus consisting of code snippets collected from the most popular Android repositories on GitHub.
```

*   **License**: CC-BY-NC 4.0 (Attr Non-Commercial Inter.)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 287

*   **Features**:

```json
{
    "stackoverflow_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_author": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_author_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_author": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_author_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "examples": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "examples_url": {
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



## search_corpus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:neural_code_search/search_corpus')
```

*   **Description**:

```
Neural-Code-Search-Evaluation-Dataset presents an evaluation dataset consisting of natural language query and code snippet pairs and a search corpus consisting of code snippets collected from the most popular Android repositories on GitHub.
```

*   **License**: CC-BY-NC 4.0 (Attr Non-Commercial Inter.)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4716814

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "filepath": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "method_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "start_line": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end_line": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


