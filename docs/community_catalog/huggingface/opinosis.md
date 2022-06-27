# opinosis

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opinosis)
*   [Huggingface](https://huggingface.co/datasets/opinosis)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opinosis')
```

*   **Description**:

```
The Opinosis Opinion Dataset consists of sentences extracted from reviews for 51 topics.
Topics and opinions are obtained from Tripadvisor, Edmunds.com and Amazon.com.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 51

*   **Features**:

```json
{
    "review_sents": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summaries": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


