# tuple_ie

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tuple_ie)
*   [Huggingface](https://huggingface.co/datasets/tuple_ie)


## all


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tuple_ie/all')
```

*   **Description**:

```
The TupleInf Open IE dataset contains Open IE tuples extracted from 263K sentences that were used by the solver in “Answering Complex Questions Using Open Information Extraction” (referred as Tuple KB, T). These sentences were collected from a large Web corpus using training questions from 4th and 8th grade as queries. This dataset contains 156K sentences collected for 4th grade questions and 107K sentences for 8th grade questions. Each sentence is followed by the Open IE v4 tuples using their simple format.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 267719

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tuples": {
        "feature": {
            "score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "tuple_text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
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
            "arg2s": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## 4th_grade


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tuple_ie/4th_grade')
```

*   **Description**:

```
The TupleInf Open IE dataset contains Open IE tuples extracted from 263K sentences that were used by the solver in “Answering Complex Questions Using Open Information Extraction” (referred as Tuple KB, T). These sentences were collected from a large Web corpus using training questions from 4th and 8th grade as queries. This dataset contains 156K sentences collected for 4th grade questions and 107K sentences for 8th grade questions. Each sentence is followed by the Open IE v4 tuples using their simple format.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 158910

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tuples": {
        "feature": {
            "score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "tuple_text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
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
            "arg2s": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## 8th_grade


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tuple_ie/8th_grade')
```

*   **Description**:

```
The TupleInf Open IE dataset contains Open IE tuples extracted from 263K sentences that were used by the solver in “Answering Complex Questions Using Open Information Extraction” (referred as Tuple KB, T). These sentences were collected from a large Web corpus using training questions from 4th and 8th grade as queries. This dataset contains 156K sentences collected for 4th grade questions and 107K sentences for 8th grade questions. Each sentence is followed by the Open IE v4 tuples using their simple format.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 108809

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tuples": {
        "feature": {
            "score": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "tuple_text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "context": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
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
            "arg2s": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


