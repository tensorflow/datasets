# spider

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/spider)
*   [Huggingface](https://huggingface.co/datasets/spider)


## spider


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:spider/spider')
```

*   **Description**:

```
Spider is a large-scale complex and cross-domain semantic parsing and text-toSQL dataset annotated by 11 college students
```

*   **License**: CC BY-SA 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7000
`'validation'` | 1034

*   **Features**:

```json
{
    "db_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_toks": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "query_toks_no_value": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "question_toks": {
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


