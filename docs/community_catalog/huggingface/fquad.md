# fquad

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/fquad)
*   [Huggingface](https://huggingface.co/datasets/fquad)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:fquad')
```

*   **Description**:

```
FQuAD: French Question Answering Dataset
We introduce FQuAD, a native French Question Answering Dataset. FQuAD contains 25,000+ question and answer pairs.
Finetuning CamemBERT on FQuAD yields a F1 score of 88% and an exact match of 77.9%.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4921
`'validation'` | 768

*   **Features**:

```json
{
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "questions": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answers": {
        "feature": {
            "texts": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answers_starts": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


