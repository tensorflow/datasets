# code_x_glue_cc_code_refinement

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/code_x_glue_cc_code_refinement)
*   [Huggingface](https://huggingface.co/datasets/code_x_glue_cc_code_refinement)


## medium


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:code_x_glue_cc_code_refinement/medium')
```

*   **Description**:

```
CodeXGLUE code-refinement dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement

We use the dataset released by this paper(https://arxiv.org/pdf/1812.08693.pdf). The source side is a Java function with bugs and the target side is the refined one. All the function and variable names are normalized. Their dataset contains two subsets ( i.e.small and medium) based on the function length.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6545
`'train'` | 52364
`'validation'` | 6546

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "buggy": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fixed": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## small


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:code_x_glue_cc_code_refinement/small')
```

*   **Description**:

```
CodeXGLUE code-refinement dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement

We use the dataset released by this paper(https://arxiv.org/pdf/1812.08693.pdf). The source side is a Java function with bugs and the target side is the refined one. All the function and variable names are normalized. Their dataset contains two subsets ( i.e.small and medium) based on the function length.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5835
`'train'` | 46680
`'validation'` | 5835

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "buggy": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fixed": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


