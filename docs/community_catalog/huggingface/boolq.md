# boolq

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/boolq)
*   [Huggingface](https://huggingface.co/datasets/boolq)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:boolq')
```

*   **Description**:

```
BoolQ is a question answering dataset for yes/no questions containing 15942 examples. These questions are naturally
occurring ---they are generated in unprompted and unconstrained settings.
Each example is a triplet of (question, passage, answer), with the title of the page as optional additional context.
The text-pair classification setup is similar to existing natural language inference tasks.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 9427
`'validation'` | 3270

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "passage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


