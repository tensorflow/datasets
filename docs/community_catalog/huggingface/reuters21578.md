# reuters21578

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/reuters21578)
*   [Huggingface](https://huggingface.co/datasets/reuters21578)


## ModHayes


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:reuters21578/ModHayes')
```

*   **Description**:

```
The Reuters-21578 dataset  is one of the most widely used data collections for text
categorization research. It is collected from the Reuters financial newswire service in 1987.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 722
`'train'` | 20856

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topics": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "lewis_split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "cgis_split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "old_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "new_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "places": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "people": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "orgs": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "exchanges": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ModLewis


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:reuters21578/ModLewis')
```

*   **Description**:

```
The Reuters-21578 dataset  is one of the most widely used data collections for text
categorization research. It is collected from the Reuters financial newswire service in 1987.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6188
`'train'` | 13625
`'unused'` | 722

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topics": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "lewis_split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "cgis_split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "old_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "new_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "places": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "people": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "orgs": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "exchanges": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ModApte


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:reuters21578/ModApte')
```

*   **Description**:

```
The Reuters-21578 dataset  is one of the most widely used data collections for text
categorization research. It is collected from the Reuters financial newswire service in 1987.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3299
`'train'` | 9603
`'unused'` | 722

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topics": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "lewis_split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "cgis_split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "old_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "new_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "places": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "people": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "orgs": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "exchanges": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


