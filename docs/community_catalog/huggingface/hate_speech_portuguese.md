# hate_speech_portuguese

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hate_speech_portuguese)
*   [Huggingface](https://huggingface.co/datasets/hate_speech_portuguese)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hate_speech_portuguese')
```

*   **Description**:

```
Portuguese dataset for hate speech detection composed of 5,668 tweets with binary annotations (i.e. 'hate' vs. 'no-hate').
```

*   **License**: Unknown
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5670

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "no-hate",
            "hate"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "hatespeech_G1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotator_G1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hatespeech_G2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotator_G2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hatespeech_G3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotator_G3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


