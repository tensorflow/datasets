# pec

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/pec)
*   [Huggingface](https://huggingface.co/datasets/pec)


## happy


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pec/happy')
```

*   **Description**:

```
A dataset of around 350K persona-based empathetic conversations. 
Each speaker is associated with a persona, which comprises multiple persona sentences. 
The response of each conversation is empathetic.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 22730
`'train'` | 157195
`'validation'` | 19829

*   **Features**:

```json
{
    "personas": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "context": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "context_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "response": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## offmychest


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pec/offmychest')
```

*   **Description**:

```
A dataset of around 350K persona-based empathetic conversations. 
Each speaker is associated with a persona, which comprises multiple persona sentences. 
The response of each conversation is empathetic.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15324
`'train'` | 123968
`'validation'` | 16004

*   **Features**:

```json
{
    "personas": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "context": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "context_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "response": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## all


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pec/all')
```

*   **Description**:

```
A dataset of around 350K persona-based empathetic conversations. 
Each speaker is associated with a persona, which comprises multiple persona sentences. 
The response of each conversation is empathetic.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 38054
`'train'` | 281163
`'validation'` | 35833

*   **Features**:

```json
{
    "personas": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "context": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "context_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "response": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


