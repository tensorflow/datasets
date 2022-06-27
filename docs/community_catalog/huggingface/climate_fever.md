# climate_fever

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/climate_fever)
*   [Huggingface](https://huggingface.co/datasets/climate_fever)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:climate_fever')
```

*   **Description**:

```
A dataset adopting the FEVER methodology that consists of 1,535 real-world claims regarding climate-change collected on the internet. Each claim is accompanied by five manually annotated evidence sentences retrieved from the English Wikipedia that support, refute or do not give enough information to validate the claim totalling in 7,675 claim-evidence pairs. The dataset features challenging claims that relate multiple facets and disputed cases of claims where both supporting and refuting evidence are present.
```

*   **License**: No known license
*   **Version**: 1.0.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1535

*   **Features**:

```json
{
    "claim_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim_label": {
        "num_classes": 4,
        "names": [
            "SUPPORTS",
            "REFUTES",
            "NOT_ENOUGH_INFO",
            "DISPUTED"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "evidences": [
        {
            "evidence_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "evidence_label": {
                "num_classes": 3,
                "names": [
                    "SUPPORTS",
                    "REFUTES",
                    "NOT_ENOUGH_INFO"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "article": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "evidence": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "entropy": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "votes": [
                {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            ]
        }
    ]
}
```


