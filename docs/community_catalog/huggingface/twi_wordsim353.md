# twi_wordsim353

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/twi_wordsim353)
*   [Huggingface](https://huggingface.co/datasets/twi_wordsim353)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:twi_wordsim353')
```

*   **Description**:

```
A translation of the word pair similarity dataset wordsim-353 to Twi.

The dataset was presented in the paper
Alabi et al.: Massive vs. Curated Embeddings for Low-Resourced
Languages: the Case of Yorùbá and Twi (LREC 2020).
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 274

*   **Features**:

```json
{
    "twi1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "twi2": {
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


