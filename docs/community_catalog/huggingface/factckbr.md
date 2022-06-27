# factckbr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/factckbr)
*   [Huggingface](https://huggingface.co/datasets/factckbr)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:factckbr')
```

*   **Description**:

```
A dataset to study Fake News in Portuguese, presenting a supposedly false News along with their respective fact check and classification.
The data is collected from the ClaimReview, a structured data schema used by fact check agencies to share their results in search engines, enabling data collect in real time.
The FACTCK.BR dataset contains 1309 claims with its corresponding label.
```

*   **License**: MIT
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1313

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "author": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "claim": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rating": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "best_rating": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 14,
        "names": [
            "falso",
            "distorcido",
            "impreciso",
            "exagerado",
            "insustent\u00e1vel",
            "verdadeiro",
            "outros",
            "subestimado",
            "imposs\u00edvel provar",
            "discut\u00edvel",
            "sem contexto",
            "de olho",
            "verdadeiro, mas",
            "ainda \u00e9 cedo para dizer"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


