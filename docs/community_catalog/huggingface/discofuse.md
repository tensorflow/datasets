# discofuse

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/discofuse)
*   [Huggingface](https://huggingface.co/datasets/discofuse)


## discofuse-sport


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:discofuse/discofuse-sport')
```

*   **Description**:

```
DISCOFUSE is a large scale dataset for discourse-based sentence fusion.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 445521
`'train'` | 43291020
`'validation'` | 440902

*   **Features**:

```json
{
    "connective_string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "discourse_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "coherent_second_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "has_coref_type_pronoun": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "incoherent_first_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "incoherent_second_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "has_coref_type_nominal": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "coherent_first_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## discofuse-wikipedia


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:discofuse/discofuse-wikipedia')
```

*   **Description**:

```
DISCOFUSE is a large scale dataset for discourse-based sentence fusion.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 163657
`'train'` | 16310585
`'validation'` | 168081

*   **Features**:

```json
{
    "connective_string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "discourse_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "coherent_second_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "has_coref_type_pronoun": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "incoherent_first_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "incoherent_second_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "has_coref_type_nominal": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "coherent_first_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


