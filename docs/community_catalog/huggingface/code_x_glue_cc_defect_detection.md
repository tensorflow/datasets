# code_x_glue_cc_defect_detection

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/code_x_glue_cc_defect_detection)
*   [Huggingface](https://huggingface.co/datasets/code_x_glue_cc_defect_detection)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:code_x_glue_cc_defect_detection')
```

*   **Description**:

```
CodeXGLUE Defect-detection dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Defect-detection

Given a source code, the task is to identify whether it is an insecure code that may attack software systems, such as resource leaks, use-after-free vulnerabilities and DoS attack. We treat the task as binary classification (0/1), where 1 stands for insecure code and 0 for secure code.
The dataset we use comes from the paper Devign: Effective Vulnerability Identification by Learning Comprehensive Program Semantics via Graph Neural Networks. We combine all projects and split 80%/10%/10% for training/dev/test.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2732
`'train'` | 21854
`'validation'` | 2732

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "func": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "project": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "commit_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


