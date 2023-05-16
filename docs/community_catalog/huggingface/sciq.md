# sciq

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sciq)
*   [Huggingface](https://huggingface.co/datasets/sciq)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sciq')
```

*   **Description**:

```
The SciQ dataset contains 13,679 crowdsourced science exam questions about Physics, Chemistry and Biology, among others. The questions are in multiple-choice format with 4 answer options each. For the majority of the questions, an additional paragraph with supporting evidence for the correct answer is provided.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 11679
`'validation'` | 1000

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct_answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "support": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


