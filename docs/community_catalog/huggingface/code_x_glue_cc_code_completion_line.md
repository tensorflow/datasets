# code_x_glue_cc_code_completion_line

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/code_x_glue_cc_code_completion_line)
*   [Huggingface](https://huggingface.co/datasets/code_x_glue_cc_code_completion_line)


## java


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:code_x_glue_cc_code_completion_line/java')
```

*   **Description**:

```
CodeXGLUE CodeCompletion-line dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/CodeCompletion-line

Complete the unfinished line given previous context. Models are evaluated by exact match and edit similarity.
We propose line completion task to test model's ability to autocomplete a line. Majority code completion systems behave well in token level completion, but fail in completing an unfinished line like a method call with specific parameters, a function signature, a loop condition, a variable definition and so on. When a software develop finish one or more tokens of the current line, the line level completion model is expected to generate the entire line of syntactically correct code.
Line level code completion task shares the train/dev dataset with token level completion. After training a model on CodeCompletion-token, you could directly use it to test on line-level completion.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3000

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## python


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:code_x_glue_cc_code_completion_line/python')
```

*   **Description**:

```
CodeXGLUE CodeCompletion-line dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/CodeCompletion-line

Complete the unfinished line given previous context. Models are evaluated by exact match and edit similarity.
We propose line completion task to test model's ability to autocomplete a line. Majority code completion systems behave well in token level completion, but fail in completing an unfinished line like a method call with specific parameters, a function signature, a loop condition, a variable definition and so on. When a software develop finish one or more tokens of the current line, the line level completion model is expected to generate the entire line of syntactically correct code.
Line level code completion task shares the train/dev dataset with token level completion. After training a model on CodeCompletion-token, you could directly use it to test on line-level completion.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10000

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "input": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


