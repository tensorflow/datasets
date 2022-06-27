# brwac

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/brwac)
*   [Huggingface](https://huggingface.co/datasets/brwac)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:brwac')
```

*   **Description**:

```
The BrWaC (Brazilian Portuguese Web as Corpus) is a large corpus constructed following the Wacky framework,
which was made public for research purposes. The current corpus version, released in January 2017, is composed by
3.53 million documents, 2.68 billion tokens and 5.79 million types. Please note that this resource is available
solely for academic research purposes, and you agreed not to use it for any commercial applications.
Manually download at https://www.inf.ufrgs.br/pln/wiki/index.php?title=BrWaC
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3530796

*   **Features**:

```json
{
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "uri": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "feature": {
            "paragraphs": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


