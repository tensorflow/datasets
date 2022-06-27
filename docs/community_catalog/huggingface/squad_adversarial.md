# squad_adversarial

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/squad_adversarial)
*   [Huggingface](https://huggingface.co/datasets/squad_adversarial)


## squad_adversarial


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_adversarial/squad_adversarial')
```

*   **Description**:

```
Here are two different adversaries, each of which uses a different procedure to pick the sentence it adds to the paragraph:
AddSent: Generates up to five candidate adversarial sentences that don't answer the question, but have a lot of words in common with the question. Picks the one that most confuses the model.
AddOneSent: Similar to AddSent, but just picks one of the candidate sentences at random. This adversary is does not query the model in any way.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'AddOneSent'` | 1787
`'AddSent'` | 3560

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



## AddSent


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_adversarial/AddSent')
```

*   **Description**:

```
Here are two different adversaries, each of which uses a different procedure to pick the sentence it adds to the paragraph:
AddSent: Generates up to five candidate adversarial sentences that don't answer the question, but have a lot of words in common with the question. Picks the one that most confuses the model.
AddOneSent: Similar to AddSent, but just picks one of the candidate sentences at random. This adversary is does not query the model in any way.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 3560

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



## AddOneSent


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_adversarial/AddOneSent')
```

*   **Description**:

```
Here are two different adversaries, each of which uses a different procedure to pick the sentence it adds to the paragraph:
AddSent: Generates up to five candidate adversarial sentences that don't answer the question, but have a lot of words in common with the question. Picks the one that most confuses the model.
AddOneSent: Similar to AddSent, but just picks one of the candidate sentences at random. This adversary is does not query the model in any way.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 1787

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


