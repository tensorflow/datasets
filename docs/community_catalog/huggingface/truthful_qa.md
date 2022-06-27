# truthful_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/truthful_qa)
*   [Huggingface](https://huggingface.co/datasets/truthful_qa)


## generation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:truthful_qa/generation')
```

*   **Description**:

```
TruthfulQA is a benchmark to measure whether a language model is truthful in
generating answers to questions. The benchmark comprises 817 questions that
span 38 categories, including health, law, finance and politics. Questions are
crafted so that some humans would answer falsely due to a false belief or
misconception. To perform well, models must avoid generating false answers
learned from imitating human texts.
```

*   **License**: Apache License 2.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 817

*   **Features**:

```json
{
    "type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "best_answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "incorrect_answers": {
        "feature": {
            "dtype": "string",
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
}
```



## multiple_choice


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:truthful_qa/multiple_choice')
```

*   **Description**:

```
TruthfulQA is a benchmark to measure whether a language model is truthful in
generating answers to questions. The benchmark comprises 817 questions that
span 38 categories, including health, law, finance and politics. Questions are
crafted so that some humans would answer falsely due to a false belief or
misconception. To perform well, models must avoid generating false answers
learned from imitating human texts.
```

*   **License**: Apache License 2.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 817

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "mc1_targets": {
        "choices": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "labels": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "mc2_targets": {
        "choices": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "labels": {
            "feature": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    }
}
```


