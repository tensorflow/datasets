# text2log

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/text2log)
*   [Huggingface](https://huggingface.co/datasets/text2log)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:text2log')
```

*   **Description**:

```
The dataset contains about 100,000 simple English sentences selected and filtered from enTenTen15 and their translation into First Order Logic (FOL) Lambda Dependency-based Compositional Semantics using ccg2lambda.
```

*   **License**: none provided
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 101931

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fol_translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


