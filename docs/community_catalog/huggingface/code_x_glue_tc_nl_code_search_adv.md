# code_x_glue_tc_nl_code_search_adv

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/code_x_glue_tc_nl_code_search_adv)
*   [Huggingface](https://huggingface.co/datasets/code_x_glue_tc_nl_code_search_adv)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:code_x_glue_tc_nl_code_search_adv')
```

*   **Description**:

```
CodeXGLUE NL-code-search-Adv dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/NL-code-search-Adv

The dataset we use comes from CodeSearchNet and we filter the dataset as the following:
- Remove examples that codes cannot be parsed into an abstract syntax tree.
- Remove examples that #tokens of documents is < 3 or >256
- Remove examples that documents contain special tokens (e.g. <img ...> or https:...)
- Remove examples that documents are not English.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 19210
`'train'` | 251820
`'validation'` | 9604

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "repo": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "path": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "func_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "code": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "code_tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "docstring": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "docstring_tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "sha": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "docstring_summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "parameters": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "return_statement": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "argument_list": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "identifier": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nwo": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


