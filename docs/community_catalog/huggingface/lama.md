# lama

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lama)
*   [Huggingface](https://huggingface.co/datasets/lama)


## trex


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lama/trex')
```

*   **Description**:

```
LAMA is a dataset used to probe and analyze the factual and commonsense knowledge contained in pretrained language models. See https://github.com/facebookresearch/LAMA.
```

*   **License**: The Creative Commons Attribution-Noncommercial 4.0 International License. see https://github.com/facebookresearch/LAMA/blob/master/LICENSE
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1304391

*   **Features**:

```json
{
    "uuid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_uri": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_uri": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "predicate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_surface": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_surface": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "masked_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "template": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "template_negated": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## squad


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lama/squad')
```

*   **Description**:

```
LAMA is a dataset used to probe and analyze the factual and commonsense knowledge contained in pretrained language models. See https://github.com/facebookresearch/LAMA.
```

*   **License**: The Creative Commons Attribution-Noncommercial 4.0 International License. see https://github.com/facebookresearch/LAMA/blob/master/LICENSE
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 305

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "negated": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "masked_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## google_re


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lama/google_re')
```

*   **Description**:

```
LAMA is a dataset used to probe and analyze the factual and commonsense knowledge contained in pretrained language models. See https://github.com/facebookresearch/LAMA.
```

*   **License**: The Creative Commons Attribution-Noncommercial 4.0 International License. see https://github.com/facebookresearch/LAMA/blob/master/LICENSE
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6106

*   **Features**:

```json
{
    "pred": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "evidences": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "judgments": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_w": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub_aliases": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_w": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_aliases": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "uuid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "masked_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "template": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "template_negated": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## conceptnet


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lama/conceptnet')
```

*   **Description**:

```
LAMA is a dataset used to probe and analyze the factual and commonsense knowledge contained in pretrained language models. See https://github.com/facebookresearch/LAMA.
```

*   **License**: The Creative Commons Attribution-Noncommercial 4.0 International License. see https://github.com/facebookresearch/LAMA/blob/master/LICENSE
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 29774

*   **Features**:

```json
{
    "uuid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pred": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "obj_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "masked_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "negated": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


