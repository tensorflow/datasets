# sberquad

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sberquad)
*   [Huggingface](https://huggingface.co/datasets/sberquad)


## sberquad


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sberquad/sberquad')
```

*   **Description**:

```
Sber Question Answering Dataset (SberQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable. Russian original analogue presented in Sberbank Data Science Journey 2017.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 23936
`'train'` | 45328
`'validation'` | 5036

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
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
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


