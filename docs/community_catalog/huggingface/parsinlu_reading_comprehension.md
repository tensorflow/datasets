# parsinlu_reading_comprehension

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/parsinlu_reading_comprehension)
*   [Huggingface](https://huggingface.co/datasets/parsinlu_reading_comprehension)


## parsinlu-repo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:parsinlu_reading_comprehension/parsinlu-repo')
```

*   **Description**:

```
A Persian reading comprehenion task (generating an answer, given a question and a context paragraph). 
The questions are mined using Google auto-complete, their answers and the corresponding evidence documents are manually annotated by native speakers.
```

*   **License**: CC BY-NC-SA 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 575
`'train'` | 600
`'validation'` | 125

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
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
            "answer_text": {
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


