# riddle_sense

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/riddle_sense)
*   [Huggingface](https://huggingface.co/datasets/riddle_sense)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:riddle_sense')
```

*   **Description**:

```
Answering such a riddle-style question is a challenging cognitive process, in that it requires 
complex commonsense reasoning abilities, an understanding of figurative language, and counterfactual reasoning 
skills, which are all important abilities for advanced natural language understanding (NLU). However, 
there is currently no dedicated datasets aiming to test these abilities. Herein, we present RiddleSense, 
a new multiple-choice question answering task, which comes with the first large dataset (5.7k examples) for answering 
riddle-style commonsense questions. We systematically evaluate a wide range of models over the challenge, 
and point out that there is a large gap between the best-supervised model and human performance — suggesting 
intriguing future research in the direction of higher-order commonsense reasoning and linguistic creativity towards 
building advanced NLU systems.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1184
`'train'` | 3510
`'validation'` | 1021

*   **Features**:

```json
{
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choices": {
        "feature": {
            "label": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
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


