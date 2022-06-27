# mrqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mrqa)
*   [Huggingface](https://huggingface.co/datasets/mrqa)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mrqa/plain_text')
```

*   **Description**:

```
The MRQA 2019 Shared Task focuses on generalization in question answering.
An effective question answering system should do more than merely
interpolate from the training set to answer test examples drawn
from the same distribution: it should also be able to extrapolate
to out-of-distribution examples — a significantly harder challenge.

The dataset is a collection of 18 existing QA dataset (carefully selected
subset of them) and converted to the same format (SQuAD format). Among
these 18 datasets, six datasets were made available for training,
six datasets were made available for development, and the final six
for testing. The dataset is released as part of the MRQA 2019 Shared Task.
```

*   **License**: Unknwon
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9633
`'train'` | 516819
`'validation'` | 58221

*   **Features**:

```json
{
    "subset": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context_tokens": {
        "feature": {
            "tokens": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "offsets": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "qid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tokens": {
        "feature": {
            "tokens": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "offsets": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "detected_answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "char_spans": {
                "feature": {
                    "start": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "token_spans": {
                "feature": {
                    "start": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "end": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    }
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


