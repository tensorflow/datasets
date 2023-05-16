# hda_nli_hindi

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hda_nli_hindi)
*   [Huggingface](https://huggingface.co/datasets/hda_nli_hindi)


## HDA hindi nli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hda_nli_hindi/HDA hindi nli')
```

*   **Description**:

```
This dataset is a recasted version of the Hindi Discourse Analysis Dataset used to train models for Natural Language Inference Tasks in Low-Resource Languages like Hindi.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9970
`'train'` | 31892
`'validation'` | 9460

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "not-entailment",
            "entailment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "topic": {
        "num_classes": 5,
        "names": [
            "Argumentative",
            "Descriptive",
            "Dialogic",
            "Informative",
            "Narrative"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## hda nli hindi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hda_nli_hindi/hda nli hindi')
```

*   **Description**:

```
This dataset is a recasted version of the Hindi Discourse Analysis Dataset used to train models for Natural Language Inference Tasks in Low-Resource Languages like Hindi.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9970
`'train'` | 31892
`'validation'` | 9460

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "not-entailment",
            "entailment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "topic": {
        "num_classes": 5,
        "names": [
            "Argumentative",
            "Descriptive",
            "Dialogic",
            "Informative",
            "Narrative"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


