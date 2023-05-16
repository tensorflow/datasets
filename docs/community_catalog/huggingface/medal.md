# medal

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/medal)
*   [Huggingface](https://huggingface.co/datasets/medal)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:medal')
```

*   **Description**:

```
A large medical text dataset (14Go) curated to 4Go for abbreviation disambiguation, designed for natural language understanding pre-training in the medical domain. For example, DHF can be disambiguated to dihydrofolate, diastolic heart failure, dengue hemorragic fever or dihydroxyfumarate
```

*   **License**: No known license
*   **Version**: 4.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'full'` | 14393619
`'test'` | 1000000
`'train'` | 3000000
`'validation'` | 1000000

*   **Features**:

```json
{
    "abstract_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "location": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "label": {
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


