# tweet_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tweet_qa)
*   [Huggingface](https://huggingface.co/datasets/tweet_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_qa')
```

*   **Description**:

```
TweetQA is the first dataset for QA on social media data by leveraging news media and crowdsourcing.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1979
`'train'` | 10692
`'validation'` | 1086

*   **Features**:

```json
{
    "Question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Answer": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "Tweet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "qid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


