# mocha

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mocha)
*   [Huggingface](https://huggingface.co/datasets/mocha)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mocha')
```

*   **Description**:

```
Posing reading comprehension as a generation problem provides a great deal of flexibility, allowing for open-ended questions with few restrictions on possible answers. However, progress is impeded by existing generation metrics, which rely on token overlap and are agnostic to the nuances of reading comprehension. To address this, we introduce a benchmark for training and evaluating generative reading comprehension metrics: MOdeling Correctness with Human Annotations. MOCHA contains 40K human judgement scores on model outputs from 6 diverse question answering datasets and an additional set of minimal pairs for evaluation. Using MOCHA, we train an evaluation metric: LERC, a Learned Evaluation metric for Reading Comprehension, to mimic human judgement scores.
```

*   **License**: https://creativecommons.org/licenses/by-sa/4.0/legalcode
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'minimal_pairs'` | 200
`'test'` | 6321
`'train'` | 31069
`'validation'` | 4009

*   **Features**:

```json
{
    "constituent_dataset": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "reference": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "metadata": {
        "scores": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "source": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "candidate2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score2": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


