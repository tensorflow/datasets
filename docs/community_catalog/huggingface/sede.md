# sede

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sede)
*   [Huggingface](https://huggingface.co/datasets/sede)


## sede


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sede/sede')
```

*   **Description**:

```
SEDE (Stack Exchange Data Explorer) is new dataset for Text-to-SQL tasks with more than 12,000 SQL queries and their
natural language description. It's based on a real usage of users from the Stack Exchange Data Explorer platform,
which brings complexities and challenges never seen before in any other semantic parsing dataset like
including complex nesting, dates manipulation, numeric and text manipulation, parameters, and most
importantly: under-specification and hidden-assumptions.

Paper (NLP4Prog workshop at ACL2021): https://arxiv.org/abs/2106.05006
```

*   **License**: Apache-2.0 License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 857
`'train'` | 10309
`'validation'` | 857

*   **Features**:

```json
{
    "QuerySetId": {
        "dtype": "uint32",
        "id": null,
        "_type": "Value"
    },
    "Title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "QueryBody": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "CreationDate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "validated": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    }
}
```


