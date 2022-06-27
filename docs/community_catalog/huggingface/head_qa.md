# head_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/head_qa)
*   [Huggingface](https://huggingface.co/datasets/head_qa)


## es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:head_qa/es')
```

*   **Description**:

```
HEAD-QA is a multi-choice HEAlthcare Dataset. The questions come from exams to access a specialized position in the
Spanish healthcare system, and are challenging even for highly specialized humans. They are designed by the Ministerio
de Sanidad, Consumo y Bienestar Social.

The dataset contains questions about the following topics: medicine, nursing, psychology, chemistry, pharmacology and biology.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2742
`'train'` | 2657
`'validation'` | 1366

*   **Features**:

```json
{
    "name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "qid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "qtext": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ra": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "image": {
        "id": null,
        "_type": "Image"
    },
    "answers": [
        {
            "aid": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "atext": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```



## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:head_qa/en')
```

*   **Description**:

```
HEAD-QA is a multi-choice HEAlthcare Dataset. The questions come from exams to access a specialized position in the
Spanish healthcare system, and are challenging even for highly specialized humans. They are designed by the Ministerio
de Sanidad, Consumo y Bienestar Social.

The dataset contains questions about the following topics: medicine, nursing, psychology, chemistry, pharmacology and biology.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2742
`'train'` | 2657
`'validation'` | 1366

*   **Features**:

```json
{
    "name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "qid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "qtext": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ra": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "image": {
        "id": null,
        "_type": "Image"
    },
    "answers": [
        {
            "aid": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "atext": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```


