# kelm

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kelm)
*   [Huggingface](https://huggingface.co/datasets/kelm)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kelm')
```

*   **Description**:

```
Data-To-Text Generation involves converting knowledge graph (KG) triples of the form (subject, relation, object) into
a natural language sentence(s). This dataset consists of English KG data converted into paired natural language text.
The generated corpus consists of ∼18M sentences spanning ∼45M triples with ∼1500 distinct relations.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 796493
`'train'` | 6371131
`'validation'` | 796471

*   **Features**:

```json
{
    "triple": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


