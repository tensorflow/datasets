# eraser_multi_rc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/eraser_multi_rc)
*   [Huggingface](https://huggingface.co/datasets/eraser_multi_rc)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:eraser_multi_rc')
```

*   **Description**:

```
Eraser Multi RC is a dataset for queries over multi-line passages, along with
answers and a rationalte. Each example in this dataset has the following 5 parts
1. A Mutli-line Passage
2. A Query about the passage
3. An Answer to the query
4. A Classification as to whether the answer is right or wrong
5. An Explanation justifying the classification
```

*   **License**: No known license
*   **Version**: 0.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4848
`'train'` | 24029
`'validation'` | 3214

*   **Features**:

```json
{
    "passage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_and_answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "evidences": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


