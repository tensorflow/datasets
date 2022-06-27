# code_x_glue_cc_clone_detection_poj104

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/code_x_glue_cc_clone_detection_poj104)
*   [Huggingface](https://huggingface.co/datasets/code_x_glue_cc_clone_detection_poj104)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:code_x_glue_cc_clone_detection_poj104')
```

*   **Description**:

```
CodeXGLUE Clone-detection-POJ-104 dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Clone-detection-POJ-104

Given a code and a collection of candidates as the input, the task is to return Top K codes with the same semantic. Models are evaluated by MAP score.
We use POJ-104 dataset on this task.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 12000
`'train'` | 32000
`'validation'` | 8000

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "code": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


