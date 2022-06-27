# hate_speech_pl

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hate_speech_pl)
*   [Huggingface](https://huggingface.co/datasets/hate_speech_pl)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hate_speech_pl')
```

*   **Description**:

```
HateSpeech corpus in the current version contains over 2000 posts crawled from public Polish web. They represent various types and degrees of offensive language, expressed toward minorities (eg. ethnical, racial). The data were annotated manually.
```

*   **License**: CC BY-NC-SA
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 13887

*   **Features**:

```json
{
    "id": {
        "dtype": "uint16",
        "id": null,
        "_type": "Value"
    },
    "text_id": {
        "dtype": "uint32",
        "id": null,
        "_type": "Value"
    },
    "annotator_id": {
        "dtype": "uint8",
        "id": null,
        "_type": "Value"
    },
    "minority_id": {
        "dtype": "uint8",
        "id": null,
        "_type": "Value"
    },
    "negative_emotions": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "call_to_action": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "source_of_knowledge": {
        "dtype": "uint8",
        "id": null,
        "_type": "Value"
    },
    "irony_sarcasm": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "topic": {
        "dtype": "uint8",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rating": {
        "dtype": "uint8",
        "id": null,
        "_type": "Value"
    }
}
```


