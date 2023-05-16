# emo

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/emo)
*   [Huggingface](https://huggingface.co/datasets/emo)


## emo2019


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:emo/emo2019')
```

*   **Description**:

```
In this dataset, given a textual dialogue i.e. an utterance along with two previous turns of context, the goal was to infer the underlying emotion of the utterance by choosing from four emotion classes - Happy, Sad, Angry and Others.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5509
`'train'` | 30160

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 4,
        "names": [
            "others",
            "happy",
            "sad",
            "angry"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


