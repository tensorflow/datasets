# hate_speech18

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hate_speech18)
*   [Huggingface](https://huggingface.co/datasets/hate_speech18)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hate_speech18')
```

*   **Description**:

```
These files contain text extracted from Stormfront, a white supremacist forum. A random set of 
forums posts have been sampled from several subforums and split into sentences. Those sentences 
have been manually labelled as containing hate speech or not, according to certain annotation guidelines.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10944

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "user_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "subforum_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "num_contexts": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 4,
        "names": [
            "noHate",
            "hate",
            "idk/skip",
            "relation"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


