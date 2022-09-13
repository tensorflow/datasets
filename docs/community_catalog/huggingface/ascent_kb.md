# ascent_kb

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ascent_kb)
*   [Huggingface](https://huggingface.co/datasets/ascent_kb)


## canonical


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ascent_kb/canonical')
```

*   **Description**:

```
This dataset contains 8.9M commonsense assertions extracted by the Ascent pipeline (https://ascent.mpi-inf.mpg.de/).
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8904060

*   **Features**:

```json
{
    "arg1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rel": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "arg2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "support": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "facets": [
        {
            "value": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "support": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "source_sentences": [
        {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```



## open


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ascent_kb/open')
```

*   **Description**:

```
This dataset contains 8.9M commonsense assertions extracted by the Ascent pipeline (https://ascent.mpi-inf.mpg.de/).
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8904060

*   **Features**:

```json
{
    "subject": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "predicate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "object": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "support": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "facets": [
        {
            "value": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "support": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "source_sentences": [
        {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "source": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```


