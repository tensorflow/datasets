# gsm8k

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/gsm8k)
*   [Huggingface](https://huggingface.co/datasets/gsm8k)


## main


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:gsm8k/main')
```

*   **Description**:

```
GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems. The
dataset was created to support the task of question answering
on basic mathematical problems that require multi-step reasoning.
```

*   **License**: MIT
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1319
`'train'` | 7473

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## socratic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:gsm8k/socratic')
```

*   **Description**:

```
GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems. The
dataset was created to support the task of question answering
on basic mathematical problems that require multi-step reasoning.
```

*   **License**: MIT
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1319
`'train'` | 7473

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


