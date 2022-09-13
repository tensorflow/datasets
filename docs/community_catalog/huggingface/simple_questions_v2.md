# simple_questions_v2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/simple_questions_v2)
*   [Huggingface](https://huggingface.co/datasets/simple_questions_v2)


## annotated


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:simple_questions_v2/annotated')
```

*   **Description**:

```
SimpleQuestions is a dataset for simple QA, which consists
of a total of 108,442 questions written in natural language by human
English-speaking annotators each paired with a corresponding fact,
formatted as (subject, relationship, object), that provides the answer
but also a complete explanation.  Fast have been extracted from the
Knowledge Base Freebase (freebase.com).  We randomly shuffle these
questions and use 70% of them (75910) as training set, 10% as
validation set (10845), and the remaining 20% as test set.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 75910
`'train'` | 75910
`'validation'` | 75910

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relationship": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "object_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## freebase2m


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:simple_questions_v2/freebase2m')
```

*   **Description**:

```
SimpleQuestions is a dataset for simple QA, which consists
of a total of 108,442 questions written in natural language by human
English-speaking annotators each paired with a corresponding fact,
formatted as (subject, relationship, object), that provides the answer
but also a complete explanation.  Fast have been extracted from the
Knowledge Base Freebase (freebase.com).  We randomly shuffle these
questions and use 70% of them (75910) as training set, 10% as
validation set (10845), and the remaining 20% as test set.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10843106

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relationship": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "object_entities": {
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



## freebase5m


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:simple_questions_v2/freebase5m')
```

*   **Description**:

```
SimpleQuestions is a dataset for simple QA, which consists
of a total of 108,442 questions written in natural language by human
English-speaking annotators each paired with a corresponding fact,
formatted as (subject, relationship, object), that provides the answer
but also a complete explanation.  Fast have been extracted from the
Knowledge Base Freebase (freebase.com).  We randomly shuffle these
questions and use 70% of them (75910) as training set, 10% as
validation set (10845), and the remaining 20% as test set.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 12010500

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relationship": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "object_entities": {
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


