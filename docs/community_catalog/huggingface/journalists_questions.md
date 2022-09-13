# journalists_questions

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/journalists_questions)
*   [Huggingface](https://huggingface.co/datasets/journalists_questions)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:journalists_questions/plain_text')
```

*   **Description**:

```
The journalists_questions corpus (version 1.0) is a collection of 10K human-written Arabic
tweets manually labeled for question identification over Arabic tweets posted by journalists.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10077

*   **Features**:

```json
{
    "tweet_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "no",
            "yes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "label_confidence": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


