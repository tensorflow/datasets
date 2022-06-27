# emotion

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/emotion)
*   [Huggingface](https://huggingface.co/datasets/emotion)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:emotion')
```

*   **Description**:

```
Emotion is a dataset of English Twitter messages with six basic emotions: anger, fear, joy, love, sadness, and surprise. For more detailed information please refer to the paper.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 16000
`'validation'` | 2000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 6,
        "names": [
            "sadness",
            "joy",
            "love",
            "anger",
            "fear",
            "surprise"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


