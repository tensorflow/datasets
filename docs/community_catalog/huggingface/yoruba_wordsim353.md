# yoruba_wordsim353

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/yoruba_wordsim353)
*   [Huggingface](https://huggingface.co/datasets/yoruba_wordsim353)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:yoruba_wordsim353')
```

*   **Description**:

```
A translation of the word pair similarity dataset wordsim-353 to Yorùbá.

The dataset was presented in the paper
Alabi et al.: Massive vs. Curated Embeddings for Low-Resourced
Languages: the Case of Yorùbá and Twi (LREC 2020).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 353

*   **Features**:

```json
{
    "english1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "english2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "yoruba1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "yoruba2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "similarity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


