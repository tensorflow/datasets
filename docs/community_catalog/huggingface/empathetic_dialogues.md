# empathetic_dialogues

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/empathetic_dialogues)
*   [Huggingface](https://huggingface.co/datasets/empathetic_dialogues)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:empathetic_dialogues')
```

*   **Description**:

```
PyTorch original implementation of Towards Empathetic Open-domain Conversation Models: a New Benchmark and Dataset
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10943
`'train'` | 76673
`'validation'` | 12030

*   **Features**:

```json
{
    "conv_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "prompt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "speaker_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "selfeval": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tags": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


