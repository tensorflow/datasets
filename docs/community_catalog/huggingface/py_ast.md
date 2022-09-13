# py_ast

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/py_ast)
*   [Huggingface](https://huggingface.co/datasets/py_ast)


## ast


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:py_ast/ast')
```

*   **Description**:

```
dataset consisting of parsed Parsed ASTs that were used to train and
evaluate the DeepSyn tool.
The Python programs are collected from GitHub repositories
by removing duplicate files, removing project forks (copy of another existing repository)
,keeping only programs that parse and have at most 30'000 nodes in the AST and
we aim to remove obfuscated files
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 50000
`'train'` | 100000

*   **Features**:

```json
{
    "ast": {
        "feature": {
            "type": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "value": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "children": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


