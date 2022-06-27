# medical_questions_pairs

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/medical_questions_pairs)
*   [Huggingface](https://huggingface.co/datasets/medical_questions_pairs)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:medical_questions_pairs')
```

*   **Description**:

```
This dataset consists of 3048 similar and dissimilar medical question pairs hand-generated and labeled by Curai's doctors.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3048

*   **Features**:

```json
{
    "dr_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question_1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            0,
            1
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


