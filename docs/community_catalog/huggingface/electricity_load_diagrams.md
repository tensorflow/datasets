# electricity_load_diagrams

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/electricity_load_diagrams)
*   [Huggingface](https://huggingface.co/datasets/electricity_load_diagrams)


## uci


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:electricity_load_diagrams/uci')
```

*   **Description**:

```
This new dataset contains hourly kW electricity consumption time series of 370 Portuguese clients from 2011 to 2014.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2590
`'train'` | 370
`'validation'` | 370

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## lstnet


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:electricity_load_diagrams/lstnet')
```

*   **Description**:

```
This new dataset contains hourly kW electricity consumption time series of 370 Portuguese clients from 2011 to 2014.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2240
`'train'` | 320
`'validation'` | 320

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


