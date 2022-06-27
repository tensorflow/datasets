# ehealth_kd

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ehealth_kd)
*   [Huggingface](https://huggingface.co/datasets/ehealth_kd)


## ehealth_kd


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ehealth_kd/ehealth_kd')
```

*   **Description**:

```
Dataset of the eHealth Knowledge Discovery Challenge at IberLEF 2020. It is designed for
the identification of semantic entities and relations in Spanish health documents.
```

*   **License**: https://creativecommons.org/licenses/by-nc-sa/4.0/
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 100
`'train'` | 800
`'validation'` | 199

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entities": [
        {
            "ent_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "ent_text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "ent_label": {
                "num_classes": 4,
                "names": [
                    "Concept",
                    "Action",
                    "Predicate",
                    "Reference"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "start_character": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end_character": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        }
    ],
    "relations": [
        {
            "rel_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "rel_label": {
                "num_classes": 13,
                "names": [
                    "is-a",
                    "same-as",
                    "has-property",
                    "part-of",
                    "causes",
                    "entails",
                    "in-time",
                    "in-place",
                    "in-context",
                    "subject",
                    "target",
                    "domain",
                    "arg"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "arg1": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "arg2": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```


