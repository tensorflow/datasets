# com_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/com_qa)
*   [Huggingface](https://huggingface.co/datasets/com_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:com_qa')
```

*   **Description**:

```
ComQA is a dataset of 11,214 questions, which were collected from WikiAnswers, a community question answering website. 
By collecting questions from such a site we ensure that the information needs are ones of interest to actual users. 
Moreover, questions posed there are often cannot be answered by commercial search engines or QA technology, making them 
more interesting for driving future research compared to those collected from an engine's query log. The dataset contains 
questions with various challenging phenomena such as the need for temporal reasoning, comparison (e.g., comparatives, 
superlatives, ordinals), compositionality (multiple, possibly nested, subquestions with multiple entities), and 
unanswerable questions (e.g., Who was the first human being on Mars?). Through a large crowdsourcing effort, questions 
in ComQA are grouped into 4,834 paraphrase clusters that express the same information need. Each cluster is annotated 
with its answer(s). ComQA answers come in the form of Wikipedia entities wherever possible. Wherever the answers are 
temporal or measurable quantities, TIMEX3 and the International System of Units (SI) are used for normalization.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2243
`'train'` | 3966
`'validation'` | 966

*   **Features**:

```json
{
    "cluster_id": {
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


