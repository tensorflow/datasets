# social_i_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/social_i_qa)
*   [Huggingface](https://huggingface.co/datasets/social_i_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:social_i_qa')
```

*   **Description**:

```
We introduce Social IQa: Social Interaction QA, a new question-answering benchmark for testing social commonsense intelligence. Contrary to many prior benchmarks that focus on physical or taxonomic knowledge, Social IQa focuses on reasoning about people’s actions and their social implications. For example, given an action like "Jesse saw a concert" and a question like "Why did Jesse do this?", humans can easily infer that Jesse wanted "to see their favorite performer" or "to enjoy the music", and not "to see what's happening inside" or "to see if it works". The actions in Social IQa span a wide variety of social situations, and answer candidates contain both human-curated answers and adversarially-filtered machine-generated candidates. Social IQa contains over 37,000 QA pairs for evaluating models’ abilities to reason about the social implications of everyday events and situations. (Less)
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 33410
`'validation'` | 1954

*   **Features**:

```json
{
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answerA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answerB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answerC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


