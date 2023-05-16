# psc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/psc)
*   [Huggingface](https://huggingface.co/datasets/psc)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:psc')
```

*   **Description**:

```
The Polish Summaries Corpus contains news articles and their summaries. We used summaries of the same article as positive pairs and sampled the most similar summaries of different articles as negatives.
```

*   **License**: CC BY-SA 3.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1078
`'train'` | 4302

*   **Features**:

```json
{
    "extract_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


