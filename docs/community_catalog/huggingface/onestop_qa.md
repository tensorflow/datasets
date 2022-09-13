# onestop_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/onestop_qa)
*   [Huggingface](https://huggingface.co/datasets/onestop_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:onestop_qa')
```

*   **Description**:

```
OneStopQA is a multiple choice reading comprehension dataset annotated according to the STARC (Structured Annotations for Reading Comprehension) scheme. The reading materials are Guardian articles taken from the [OneStopEnglish corpus](https://github.com/nishkalavallabhi/OneStopEnglishCorpus). Each article comes in three difficulty levels, Elementary, Intermediate and Advanced. Each paragraph is annotated with three multiple choice reading comprehension questions. The reading comprehension questions can be answered based on any of the three paragraph levels.
```

*   **License**: Creative Commons Attribution-ShareAlike 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1458

*   **Features**:

```json
{
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paragraph": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "level": {
        "num_classes": 3,
        "names": [
            "Adv",
            "Int",
            "Ele"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paragraph_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": 4,
        "id": null,
        "_type": "Sequence"
    },
    "a_span": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "d_span": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


