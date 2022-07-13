# msr_sqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/msr_sqa)
*   [Huggingface](https://huggingface.co/datasets/msr_sqa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:msr_sqa')
```

*   **Description**:

```
Recent work in semantic parsing for question answering has focused on long and complicated questions, many of which would seem unnatural if asked in a normal conversation between two humans. In an effort to explore a conversational QA setting, we present a more realistic task: answering sequences of simple but inter-related questions. We created SQA by asking crowdsourced workers to decompose 2,022 questions from WikiTableQuestions (WTQ), which contains highly-compositional questions about tables from Wikipedia. We had three workers decompose each WTQ question, resulting in a dataset of 6,066 sequences that contain 17,553 questions in total. Each question is also associated with answers in the form of cell locations in the tables.
```

*   **License**: Microsoft Research Data License Agreement
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3012
`'train'` | 14541

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotator": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "position": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_header": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "table_data": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer_coordinates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answer_text": {
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


