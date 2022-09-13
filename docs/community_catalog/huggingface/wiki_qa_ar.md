# wiki_qa_ar

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_qa_ar)
*   [Huggingface](https://huggingface.co/datasets/wiki_qa_ar)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_qa_ar/plain_text')
```

*   **Description**:

```
Arabic Version of WikiQA by automatic automatic machine translators and crowdsourced the selection of the best one to be incorporated into the corpus
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 20632
`'train'` | 70264
`'validation'` | 10387

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
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_id": {
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


