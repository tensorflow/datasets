# squadshifts

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/squadshifts)
*   [Huggingface](https://huggingface.co/datasets/squadshifts)


## new_wiki


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squadshifts/new_wiki')
```

*   **Description**:

```
SquadShifts consists of four new test sets for the Stanford Question Answering Dataset (SQuAD) from four different domains: Wikipedia articles, New York \ 
Times articles, Reddit comments, and Amazon product reviews. Each dataset was generated using the same data generating pipeline, Amazon Mechanical Turk interface, and data cleaning code as the original SQuAD v1.1 dataset. The "new-wikipedia" dataset measures overfitting on the original SQuAD v1.1 dataset.  The "new-york-times", "reddit", and "amazon" datasets measure robustness to natural distribution shifts. We encourage SQuAD model developers to also evaluate their methods on these new datasets!
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7938

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



## nyt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squadshifts/nyt')
```

*   **Description**:

```
SquadShifts consists of four new test sets for the Stanford Question Answering Dataset (SQuAD) from four different domains: Wikipedia articles, New York \ 
Times articles, Reddit comments, and Amazon product reviews. Each dataset was generated using the same data generating pipeline, Amazon Mechanical Turk interface, and data cleaning code as the original SQuAD v1.1 dataset. The "new-wikipedia" dataset measures overfitting on the original SQuAD v1.1 dataset.  The "new-york-times", "reddit", and "amazon" datasets measure robustness to natural distribution shifts. We encourage SQuAD model developers to also evaluate their methods on these new datasets!
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10065

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



## reddit


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squadshifts/reddit')
```

*   **Description**:

```
SquadShifts consists of four new test sets for the Stanford Question Answering Dataset (SQuAD) from four different domains: Wikipedia articles, New York \ 
Times articles, Reddit comments, and Amazon product reviews. Each dataset was generated using the same data generating pipeline, Amazon Mechanical Turk interface, and data cleaning code as the original SQuAD v1.1 dataset. The "new-wikipedia" dataset measures overfitting on the original SQuAD v1.1 dataset.  The "new-york-times", "reddit", and "amazon" datasets measure robustness to natural distribution shifts. We encourage SQuAD model developers to also evaluate their methods on these new datasets!
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9803

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



## amazon


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squadshifts/amazon')
```

*   **Description**:

```
SquadShifts consists of four new test sets for the Stanford Question Answering Dataset (SQuAD) from four different domains: Wikipedia articles, New York \ 
Times articles, Reddit comments, and Amazon product reviews. Each dataset was generated using the same data generating pipeline, Amazon Mechanical Turk interface, and data cleaning code as the original SQuAD v1.1 dataset. The "new-wikipedia" dataset measures overfitting on the original SQuAD v1.1 dataset.  The "new-york-times", "reddit", and "amazon" datasets measure robustness to natural distribution shifts. We encourage SQuAD model developers to also evaluate their methods on these new datasets!
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9885

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


