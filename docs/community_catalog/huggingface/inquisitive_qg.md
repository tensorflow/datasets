# inquisitive_qg

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/inquisitive_qg)
*   [Huggingface](https://huggingface.co/datasets/inquisitive_qg)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:inquisitive_qg/plain_text')
```

*   **Description**:

```
A dataset of about 20k questions that are elicited from readers as they naturally read through a document sentence by sentence. Compared to existing datasets, INQUISITIVE questions target more towards high-level (semantic and discourse) comprehension of text. Because these questions are generated while the readers are pro-cessing the information, the questions directly communicate gaps between the reader’s and writer’s knowledge about the events described in the text, and are not necessarily answered in the document itself. This type of question reflects a real-world scenario: if one has questions during reading, some of them are answered by the text later on, the rest are not, but any of them would help further the reader’s understanding at the particular point when they asked it. This resource could enable question generation models to simulate human-like curiosity and cognitive processing, which may open up a new realm of applications.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1894
`'train'` | 15931
`'validation'` | 1991

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "article_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span_start_position": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "span_end_position": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


