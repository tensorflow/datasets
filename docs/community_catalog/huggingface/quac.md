# quac

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/quac)
*   [Huggingface](https://huggingface.co/datasets/quac)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:quac/plain_text')
```

*   **Description**:

```
Question Answering in Context is a dataset for modeling, understanding,
and participating in information seeking dialog. Data instances consist
of an interactive dialog between two crowd workers: (1) a student who
poses a sequence of freeform questions to learn as much as possible
about a hidden Wikipedia text, and (2) a teacher who answers the questions
by providing short excerpts (spans) from the text. QuAC introduces
challenges not found in existing machine comprehension datasets: its
questions are often more open-ended, unanswerable, or only meaningful
within the dialog context.
```

*   **License**: MIT
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 11567
`'validation'` | 1000

*   **Features**:

```json
{
    "dialogue_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "wikipedia_page_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "background": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "section_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "turn_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
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
    "followups": {
        "feature": {
            "num_classes": 3,
            "names": [
                "y",
                "n",
                "m"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "yesnos": {
        "feature": {
            "num_classes": 3,
            "names": [
                "y",
                "n",
                "x"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answers": {
        "feature": {
            "texts": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "answer_starts": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "orig_answers": {
        "texts": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "answer_starts": {
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
}
```


