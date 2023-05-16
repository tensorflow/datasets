# piqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/piqa)
*   [Huggingface](https://huggingface.co/datasets/piqa)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:piqa/plain_text')
```

*   **Description**:

```
To apply eyeshadow without a brush, should I use a cotton swab or a toothpick?
Questions requiring this kind of physical commonsense pose a challenge to state-of-the-art
natural language understanding systems. The PIQA dataset introduces the task of physical commonsense reasoning
and a corresponding benchmark dataset Physical Interaction: Question Answering or PIQA.

Physical commonsense knowledge is a major challenge on the road to true AI-completeness,
including robots that interact with the world and understand natural language.

The dataset focuses on everyday situations with a preference for atypical solutions.
The dataset is inspired by instructables.com, which provides users with instructions on how to build, craft,
bake, or manipulate objects using everyday materials.

The underlying task is formualted as multiple choice question answering:
given a question `q` and two possible solutions `s1`, `s2`, a model or
a human must choose the most appropriate solution, of which exactly one is correct.
The dataset is further cleaned of basic artifacts using the AFLite algorithm which is an improvement of
adversarial filtering. The dataset contains 16,000 examples for training, 2,000 for development and 3,000 for testing.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3084
`'train'` | 16113
`'validation'` | 1838

*   **Features**:

```json
{
    "goal": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sol1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sol2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


