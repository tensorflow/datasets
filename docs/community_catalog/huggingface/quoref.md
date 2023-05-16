# quoref

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/quoref)
*   [Huggingface](https://huggingface.co/datasets/quoref)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:quoref')
```

*   **Description**:

```
Quoref is a QA dataset which tests the coreferential reasoning capability of reading comprehension systems. In this 
span-selection benchmark containing 24K questions over 4.7K paragraphs from Wikipedia, a system must resolve hard 
coreferences before selecting the appropriate span(s) in the paragraphs for answering questions.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 19399
`'validation'` | 2418

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


