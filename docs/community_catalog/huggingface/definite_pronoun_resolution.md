# definite_pronoun_resolution

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/definite_pronoun_resolution)
*   [Huggingface](https://huggingface.co/datasets/definite_pronoun_resolution)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:definite_pronoun_resolution/plain_text')
```

*   **Description**:

```
Composed by 30 students from one of the author's undergraduate classes. These
sentence pairs cover topics ranging from real events (e.g., Iran's plan to
attack the Saudi ambassador to the U.S.) to events/characters in movies (e.g.,
Batman) and purely imaginary situations, largely reflecting the pop culture as
perceived by the American kids born in the early 90s. Each annotated example
spans four lines: the first line contains the sentence, the second line contains
the target pronoun, the third line contains the two candidate antecedents, and
the fourth line contains the correct antecedent. If the target pronoun appears
more than once in the sentence, its first occurrence is the one to be resolved.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 564
`'train'` | 1322

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pronoun": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidates": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": 2,
        "id": null,
        "_type": "Sequence"
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


