# code_x_glue_cc_code_to_code_trans

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/code_x_glue_cc_code_to_code_trans)
*   [Huggingface](https://huggingface.co/datasets/code_x_glue_cc_code_to_code_trans)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:code_x_glue_cc_code_to_code_trans')
```

*   **Description**:

```
CodeXGLUE code-to-code-trans dataset, available at https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-to-code-trans

The dataset is collected from several public repos, including Lucene(http://lucene.apache.org/), POI(http://poi.apache.org/), JGit(https://github.com/eclipse/jgit/) and Antlr(https://github.com/antlr/).
        We collect both the Java and C# versions of the codes and find the parallel functions. After removing duplicates and functions with the empty body, we split the whole dataset into training, validation and test sets.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10300
`'validation'` | 500

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "java": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "cs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


