# ronec

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ronec)
*   [Huggingface](https://huggingface.co/datasets/ronec)


## ronec


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ronec/ronec')
```

*   **Description**:

```
RONEC - the Romanian Named Entity Corpus, at version 2.0, holds 12330 sentences with over 0.5M tokens, annotated with 15 classes, to a total of 80.283 distinctly annotated entities. It is used for named entity recognition and represents the largest Romanian NER corpus to date.
```

*   **License**: MIT License
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 9000
`'validation'` | 1330

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
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
    "ner_ids": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "space_after": {
        "feature": {
            "dtype": "bool",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 31,
            "names": [
                "O",
                "B-PERSON",
                "I-PERSON",
                "B-ORG",
                "I-ORG",
                "B-GPE",
                "I-GPE",
                "B-LOC",
                "I-LOC",
                "B-NAT_REL_POL",
                "I-NAT_REL_POL",
                "B-EVENT",
                "I-EVENT",
                "B-LANGUAGE",
                "I-LANGUAGE",
                "B-WORK_OF_ART",
                "I-WORK_OF_ART",
                "B-DATETIME",
                "I-DATETIME",
                "B-PERIOD",
                "I-PERIOD",
                "B-MONEY",
                "I-MONEY",
                "B-QUANTITY",
                "I-QUANTITY",
                "B-NUMERIC",
                "I-NUMERIC",
                "B-ORDINAL",
                "I-ORDINAL",
                "B-FACILITY",
                "I-FACILITY"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


