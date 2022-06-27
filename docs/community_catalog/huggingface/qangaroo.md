# qangaroo

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/qangaroo)
*   [Huggingface](https://huggingface.co/datasets/qangaroo)


## medhop


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qangaroo/medhop')
```

*   **Description**:

```
We have created two new Reading Comprehension datasets focussing on multi-hop (alias multi-step) inference.

Several pieces of information often jointly imply another fact. In multi-hop inference, a new fact is derived by combining facts via a chain of multiple steps.

Our aim is to build Reading Comprehension methods that perform multi-hop inference on text, where individual facts are spread out across different documents.

The two QAngaroo datasets provide a training and evaluation resource for such methods.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1620
`'validation'` | 342

*   **Features**:

```json
{
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "supports": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## masked_medhop


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qangaroo/masked_medhop')
```

*   **Description**:

```
We have created two new Reading Comprehension datasets focussing on multi-hop (alias multi-step) inference.

Several pieces of information often jointly imply another fact. In multi-hop inference, a new fact is derived by combining facts via a chain of multiple steps.

Our aim is to build Reading Comprehension methods that perform multi-hop inference on text, where individual facts are spread out across different documents.

The two QAngaroo datasets provide a training and evaluation resource for such methods.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1620
`'validation'` | 342

*   **Features**:

```json
{
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "supports": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wikihop


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qangaroo/wikihop')
```

*   **Description**:

```
We have created two new Reading Comprehension datasets focussing on multi-hop (alias multi-step) inference.

Several pieces of information often jointly imply another fact. In multi-hop inference, a new fact is derived by combining facts via a chain of multiple steps.

Our aim is to build Reading Comprehension methods that perform multi-hop inference on text, where individual facts are spread out across different documents.

The two QAngaroo datasets provide a training and evaluation resource for such methods.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 43738
`'validation'` | 5129

*   **Features**:

```json
{
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "supports": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## masked_wikihop


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:qangaroo/masked_wikihop')
```

*   **Description**:

```
We have created two new Reading Comprehension datasets focussing on multi-hop (alias multi-step) inference.

Several pieces of information often jointly imply another fact. In multi-hop inference, a new fact is derived by combining facts via a chain of multiple steps.

Our aim is to build Reading Comprehension methods that perform multi-hop inference on text, where individual facts are spread out across different documents.

The two QAngaroo datasets provide a training and evaluation resource for such methods.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 43738
`'validation'` | 5129

*   **Features**:

```json
{
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "supports": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


