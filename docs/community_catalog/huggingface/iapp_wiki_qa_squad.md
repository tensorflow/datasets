# iapp_wiki_qa_squad

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/iapp_wiki_qa_squad)
*   [Huggingface](https://huggingface.co/datasets/iapp_wiki_qa_squad)


## iapp_wiki_qa_squad


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:iapp_wiki_qa_squad/iapp_wiki_qa_squad')
```

*   **Description**:

```
`iapp_wiki_qa_squad` is an extractive question answering dataset from Thai Wikipedia articles.
It is adapted from [the original iapp-wiki-qa-dataset](https://github.com/iapp-technology/iapp-wiki-qa-dataset)
to [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) format, resulting in
5761/742/739 questions from 1529/191/192 articles.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 739
`'train'` | 5761
`'validation'` | 742

*   **Features**:

```json
{
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "answer_end": {
                "dtype": "int32",
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


