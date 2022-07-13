# health_fact

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/health_fact)
*   [Huggingface](https://huggingface.co/datasets/health_fact)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:health_fact')
```

*   **Description**:

```
PUBHEALTH is a comprehensive dataset for explainable automated fact-checking of
public health claims. Each instance in the PUBHEALTH dataset has an associated
veracity label (true, false, unproven, mixture). Furthermore each instance in the
dataset has an explanation text field. The explanation is a justification for which
the claim has been assigned a particular veracity label.

The dataset was created to explore fact-checking of difficult to verify claims i.e.,
those which require expertise from outside of the journalistics domain, in this case
biomedical and public health expertise.

It was also created in response to the lack of fact-checking datasets which provide
gold standard natural language explanations for verdicts/labels.

NOTE: There are missing labels in the dataset and we have replaced them with -1.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1235
`'train'` | 9832
`'validation'` | 1225

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
    "date_published": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "explanation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fact_checkers": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "main_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sources": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 4,
        "names": [
            "false",
            "mixture",
            "true",
            "unproven"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "subjects": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


