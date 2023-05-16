# codah

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/codah)
*   [Huggingface](https://huggingface.co/datasets/codah)


## codah


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:codah/codah')
```

*   **Description**:

```
The COmmonsense Dataset Adversarially-authored by Humans (CODAH) is an evaluation set for commonsense question-answering in the sentence completion style of SWAG. As opposed to other automatically generated NLI datasets, CODAH is adversarially constructed by humans who can view feedback from a pre-trained model and use this information to design challenging commonsense questions. Our experimental results show that CODAH questions present a complementary extension to the SWAG dataset, testing additional modes of common sense.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2776

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question_category": {
        "num_classes": 6,
        "names": [
            "Idioms",
            "Reference",
            "Polysemy",
            "Negation",
            "Quantitative",
            "Others"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "question_propmt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## fold_0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:codah/fold_0')
```

*   **Description**:

```
The COmmonsense Dataset Adversarially-authored by Humans (CODAH) is an evaluation set for commonsense question-answering in the sentence completion style of SWAG. As opposed to other automatically generated NLI datasets, CODAH is adversarially constructed by humans who can view feedback from a pre-trained model and use this information to design challenging commonsense questions. Our experimental results show that CODAH questions present a complementary extension to the SWAG dataset, testing additional modes of common sense.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 555
`'train'` | 1665
`'validation'` | 556

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question_category": {
        "num_classes": 6,
        "names": [
            "Idioms",
            "Reference",
            "Polysemy",
            "Negation",
            "Quantitative",
            "Others"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "question_propmt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## fold_1


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:codah/fold_1')
```

*   **Description**:

```
The COmmonsense Dataset Adversarially-authored by Humans (CODAH) is an evaluation set for commonsense question-answering in the sentence completion style of SWAG. As opposed to other automatically generated NLI datasets, CODAH is adversarially constructed by humans who can view feedback from a pre-trained model and use this information to design challenging commonsense questions. Our experimental results show that CODAH questions present a complementary extension to the SWAG dataset, testing additional modes of common sense.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 555
`'train'` | 1665
`'validation'` | 556

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question_category": {
        "num_classes": 6,
        "names": [
            "Idioms",
            "Reference",
            "Polysemy",
            "Negation",
            "Quantitative",
            "Others"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "question_propmt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## fold_2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:codah/fold_2')
```

*   **Description**:

```
The COmmonsense Dataset Adversarially-authored by Humans (CODAH) is an evaluation set for commonsense question-answering in the sentence completion style of SWAG. As opposed to other automatically generated NLI datasets, CODAH is adversarially constructed by humans who can view feedback from a pre-trained model and use this information to design challenging commonsense questions. Our experimental results show that CODAH questions present a complementary extension to the SWAG dataset, testing additional modes of common sense.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 555
`'train'` | 1665
`'validation'` | 556

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question_category": {
        "num_classes": 6,
        "names": [
            "Idioms",
            "Reference",
            "Polysemy",
            "Negation",
            "Quantitative",
            "Others"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "question_propmt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## fold_3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:codah/fold_3')
```

*   **Description**:

```
The COmmonsense Dataset Adversarially-authored by Humans (CODAH) is an evaluation set for commonsense question-answering in the sentence completion style of SWAG. As opposed to other automatically generated NLI datasets, CODAH is adversarially constructed by humans who can view feedback from a pre-trained model and use this information to design challenging commonsense questions. Our experimental results show that CODAH questions present a complementary extension to the SWAG dataset, testing additional modes of common sense.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 555
`'train'` | 1665
`'validation'` | 556

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question_category": {
        "num_classes": 6,
        "names": [
            "Idioms",
            "Reference",
            "Polysemy",
            "Negation",
            "Quantitative",
            "Others"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "question_propmt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## fold_4


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:codah/fold_4')
```

*   **Description**:

```
The COmmonsense Dataset Adversarially-authored by Humans (CODAH) is an evaluation set for commonsense question-answering in the sentence completion style of SWAG. As opposed to other automatically generated NLI datasets, CODAH is adversarially constructed by humans who can view feedback from a pre-trained model and use this information to design challenging commonsense questions. Our experimental results show that CODAH questions present a complementary extension to the SWAG dataset, testing additional modes of common sense.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 556
`'train'` | 1665
`'validation'` | 555

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question_category": {
        "num_classes": 6,
        "names": [
            "Idioms",
            "Reference",
            "Polysemy",
            "Negation",
            "Quantitative",
            "Others"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "question_propmt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate_answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct_answer_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


