# snli

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/snli)
*   [Huggingface](https://huggingface.co/datasets/snli)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:snli/plain_text')
```

*   **Description**:

```
The SNLI corpus (version 1.0) is a collection of 570k human-written English
sentence pairs manually labeled for balanced classification with the labels
entailment, contradiction, and neutral, supporting the task of natural language
inference (NLI), also known as recognizing textual entailment (RTE).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 550152
`'validation'` | 10000

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


