# datacommons_factcheck

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/datacommons_factcheck)
*   [Huggingface](https://huggingface.co/datasets/datacommons_factcheck)


## fctchk_politifact_wapo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:datacommons_factcheck/fctchk_politifact_wapo')
```

*   **Description**:

```
A dataset of fact checked claims by news media maintained by datacommons.org
```

*   **License**: CC-BY-NC-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5632

*   **Features**:

```json
{
    "reviewer_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_rating": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim_author_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## weekly_standard


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:datacommons_factcheck/weekly_standard')
```

*   **Description**:

```
A dataset of fact checked claims by news media maintained by datacommons.org
```

*   **License**: CC-BY-NC-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 132

*   **Features**:

```json
{
    "reviewer_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_rating": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim_author_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


