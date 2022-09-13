# sem_eval_2014_task_1

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sem_eval_2014_task_1)
*   [Huggingface](https://huggingface.co/datasets/sem_eval_2014_task_1)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sem_eval_2014_task_1')
```

*   **Description**:

```
The SemEval-2014 Task 1 focuses on Evaluation of Compositional Distributional Semantic Models
on Full Sentences through Semantic Relatedness and Entailment. The task was designed to
predict the degree of relatedness between two sentences and to detect the entailment
relation holding between them.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4927
`'train'` | 4500
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
        "num_classes": 3,
        "names": [
            "NEUTRAL",
            "ENTAILMENT",
            "CONTRADICTION"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


