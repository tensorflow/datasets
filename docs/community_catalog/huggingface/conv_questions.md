# conv_questions

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/conv_questions)
*   [Huggingface](https://huggingface.co/datasets/conv_questions)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conv_questions')
```

*   **Description**:

```
ConvQuestions is the first realistic benchmark for conversational question answering over knowledge graphs.
It contains 11,200 conversations which can be evaluated over Wikidata. The questions feature a variety of complex
question phenomena like comparisons, aggregations, compositionality, and temporal reasoning.
```

*   **License**: CC BY 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2240
`'train'` | 6720
`'validation'` | 2240

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "seed_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "seed_entity_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "questions": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answers": {
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
    "answer_texts": {
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


