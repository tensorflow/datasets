# story_cloze

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/story_cloze)
*   [Huggingface](https://huggingface.co/datasets/story_cloze)


## 2016


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:story_cloze/2016')
```

*   **Description**:

```
Story Cloze Test' is a commonsense reasoning framework for evaluating story understanding,
story generation, and script learning.This test requires a system to choose the correct ending
to a four-sentence story.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1871
`'validation'` | 1871

*   **Features**:

```json
{
    "story_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_sentence_1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_sentence_2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_sentence_3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_sentence_4": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_quiz1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_quiz2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_right_ending": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## 2018


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:story_cloze/2018')
```

*   **Description**:

```
Story Cloze Test' is a commonsense reasoning framework for evaluating story understanding,
story generation, and script learning.This test requires a system to choose the correct ending
to a four-sentence story.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 1571

*   **Features**:

```json
{
    "story_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_sentence_1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_sentence_2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_sentence_3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "input_sentence_4": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_quiz1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_quiz2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer_right_ending": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


