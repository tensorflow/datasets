# kor_3i4k

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kor_3i4k)
*   [Huggingface](https://huggingface.co/datasets/kor_3i4k)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_3i4k')
```

*   **Description**:

```
This dataset is designed to identify speaker intention based on real-life spoken utterance in Korean into one of
7 categories: fragment, description, question, command, rhetorical question, rhetorical command, utterances.
```

*   **License**: CC BY-SA-4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6121
`'train'` | 55134

*   **Features**:

```json
{
    "label": {
        "num_classes": 7,
        "names": [
            "fragment",
            "statement",
            "question",
            "command",
            "rhetorical question",
            "rhetorical command",
            "intonation-dependent utterance"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


