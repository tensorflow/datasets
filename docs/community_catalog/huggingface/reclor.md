# reclor

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/reclor)
*   [Huggingface](https://huggingface.co/datasets/reclor)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:reclor')
```

*   **Description**:

```
Logical reasoning is an important ability to examine, analyze, and critically evaluate arguments as they occur in ordinary
language as the definition from LSAC. ReClor is a dataset extracted from logical reasoning questions of standardized graduate
admission examinations. Empirical results show that the state-of-the-art models struggle on ReClor with poor performance
indicating more research is needed to essentially enhance the logical reasoning ability of current models. We hope this
dataset could help push Machine Reading Comprehension (MRC) towards more complicated reasonin
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 4638
`'validation'` | 500

*   **Features**:

```json
{
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
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id_string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


