# race

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/race)
*   [Huggingface](https://huggingface.co/datasets/race)


## high


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:race/high')
```

*   **Description**:

```
Race is a large-scale reading comprehension dataset with more than 28,000 passages and nearly 100,000 questions. The
 dataset is collected from English examinations in China, which are designed for middle school and high school students.
The dataset can be served as the training and test sets for machine comprehension.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3498
`'train'` | 62445
`'validation'` | 3451

*   **Features**:

```json
{
    "example_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
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



## middle


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:race/middle')
```

*   **Description**:

```
Race is a large-scale reading comprehension dataset with more than 28,000 passages and nearly 100,000 questions. The
 dataset is collected from English examinations in China, which are designed for middle school and high school students.
The dataset can be served as the training and test sets for machine comprehension.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1436
`'train'` | 25421
`'validation'` | 1436

*   **Features**:

```json
{
    "example_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
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



## all


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:race/all')
```

*   **Description**:

```
Race is a large-scale reading comprehension dataset with more than 28,000 passages and nearly 100,000 questions. The
 dataset is collected from English examinations in China, which are designed for middle school and high school students.
The dataset can be served as the training and test sets for machine comprehension.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4934
`'train'` | 87866
`'validation'` | 4887

*   **Features**:

```json
{
    "example_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
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


