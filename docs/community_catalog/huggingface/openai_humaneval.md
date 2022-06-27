# openai_humaneval

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/openai_humaneval)
*   [Huggingface](https://huggingface.co/datasets/openai_humaneval)


## openai_humaneval


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:openai_humaneval/openai_humaneval')
```

*   **Description**:

```
The HumanEval dataset released by OpenAI contains 164 handcrafted programming challenges together with unittests to very the viability of a proposed solution.
```

*   **License**: MIT
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 164

*   **Features**:

```json
{
    "task_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "prompt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "canonical_solution": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entry_point": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


