# few_rel

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/few_rel)
*   [Huggingface](https://huggingface.co/datasets/few_rel)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:few_rel')
```

*   **Description**:

```
FewRel is a large-scale few-shot relation extraction dataset, which contains more than one hundred relations and tens of thousands of annotated instances cross different domains.
```

*   **License**: https://raw.githubusercontent.com/thunlp/FewRel/master/LICENSE
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'pubmed_unsupervised'` | 2500
`'train_wiki'` | 44800
`'val_nyt'` | 2500
`'val_pubmed'` | 1000
`'val_semeval'` | 8851
`'val_wiki'` | 11200

*   **Features**:

```json
{
    "relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "head": {
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "indices": {
            "feature": {
                "feature": {
                    "dtype": "int64",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "tail": {
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "indices": {
            "feature": {
                "feature": {
                    "dtype": "int64",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "names": {
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



## pid2name


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:few_rel/pid2name')
```

*   **Description**:

```
FewRel is a large-scale few-shot relation extraction dataset, which contains more than one hundred relations and tens of thousands of annotated instances cross different domains.
```

*   **License**: https://raw.githubusercontent.com/thunlp/FewRel/master/LICENSE
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'pid2name'` | 744

*   **Features**:

```json
{
    "relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "names": {
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


