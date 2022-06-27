# ropes

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ropes)
*   [Huggingface](https://huggingface.co/datasets/ropes)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ropes/plain_text')
```

*   **Description**:

```
ROPES (Reasoning Over Paragraph Effects in Situations) is a QA dataset
which tests a system's ability to apply knowledge from a passage
of text to a new situation. A system is presented a background
passage containing a causal or qualitative relation(s) (e.g.,
"animal pollinators increase efficiency of fertilization in flowers"),
a novel situation that uses this background, and questions that require
reasoning about effects of the relationships in the background
passage in the background of the situation.
```

*   **License**: CC BY 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1710
`'train'` | 10924
`'validation'` | 1688

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "background": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "situation": {
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
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


