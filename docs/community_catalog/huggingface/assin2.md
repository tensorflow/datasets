# assin2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/assin2)
*   [Huggingface](https://huggingface.co/datasets/assin2)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:assin2')
```

*   **Description**:

```
The ASSIN 2 corpus is composed of rather simple sentences. Following the procedures of SemEval 2014 Task 1.
The training and validation data are composed, respectively, of 6,500 and 500 sentence pairs in Brazilian Portuguese,
annotated for entailment and semantic similarity. Semantic similarity values range from 1 to 5, and text entailment
classes are either entailment or none. The test data are composed of approximately 3,000 sentence pairs with the same
annotation. All data were manually annotated.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2448
`'train'` | 6500
`'validation'` | 500

*   **Features**:

```json
{
    "sentence_pair_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
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
    "relatedness_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "entailment_judgment": {
        "num_classes": 2,
        "names": [
            "NONE",
            "ENTAILMENT"
        ],
        "id": null,
        "_type": "ClassLabel"
    }
}
```


