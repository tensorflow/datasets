# tydiqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tydiqa)
*   [Huggingface](https://huggingface.co/datasets/tydiqa)


## primary_task


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tydiqa/primary_task')
```

*   **Description**:

```
TyDi QA is a question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs.
The languages of TyDi QA are diverse with regard to their typology -- the set of linguistic features that each language
expresses -- such that we expect models performing well on this set to generalize across a large number of the languages
in the world. It contains language phenomena that would not be found in English-only corpora. To provide a realistic
information-seeking task and avoid priming effects, questions are written by people who want to know the answer, but
don’t know the answer yet, (unlike SQuAD and its descendents) and the data is collected directly in each language without
the use of translation (unlike MLQA and XQuAD).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 166916
`'validation'` | 18670

*   **Features**:

```json
{
    "passage_answer_candidates": {
        "feature": {
            "plaintext_start_byte": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "plaintext_end_byte": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "question_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotations": {
        "feature": {
            "passage_answer_candidate_index": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "minimal_answers_start_byte": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "minimal_answers_end_byte": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "yes_no_answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "document_plaintext": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## secondary_task


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tydiqa/secondary_task')
```

*   **Description**:

```
TyDi QA is a question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs.
The languages of TyDi QA are diverse with regard to their typology -- the set of linguistic features that each language
expresses -- such that we expect models performing well on this set to generalize across a large number of the languages
in the world. It contains language phenomena that would not be found in English-only corpora. To provide a realistic
information-seeking task and avoid priming effects, questions are written by people who want to know the answer, but
don’t know the answer yet, (unlike SQuAD and its descendents) and the data is collected directly in each language without
the use of translation (unlike MLQA and XQuAD).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 49881
`'validation'` | 5077

*   **Features**:

```json
{
    "id": {
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
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


