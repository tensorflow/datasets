# numer_sense

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/numer_sense)
*   [Huggingface](https://huggingface.co/datasets/numer_sense)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:numer_sense')
```

*   **Description**:

```
NumerSense is a new numerical commonsense reasoning probing task, with a diagnostic dataset consisting of 3,145 masked-word-prediction probes.

We propose to study whether numerical commonsense knowledge can be induced from pre-trained language models like BERT, and to what extent this access to knowledge robust against adversarial examples is. We hope this will be beneficial for tasks such as knowledge base completion and open-domain question answering.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test_all'` | 3146
`'test_core'` | 1132
`'train'` | 10444

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


