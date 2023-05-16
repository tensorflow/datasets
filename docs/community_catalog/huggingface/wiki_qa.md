# wiki_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_qa)
*   [Huggingface](https://huggingface.co/datasets/wiki_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_qa')
```

*   **Description**:

```
Wiki Question Answering corpus from Microsoft
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6165
`'train'` | 20360
`'validation'` | 2733

*   **Features**:

```json
{
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


