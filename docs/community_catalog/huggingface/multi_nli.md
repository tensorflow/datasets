# multi_nli

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multi_nli)
*   [Huggingface](https://huggingface.co/datasets/multi_nli)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_nli')
```

*   **Description**:

```
The Multi-Genre Natural Language Inference (MultiNLI) corpus is a
crowd-sourced collection of 433k sentence pairs annotated with textual
entailment information. The corpus is modeled on the SNLI corpus, but differs in
that covers a range of genres of spoken and written text, and supports a
distinctive cross-genre generalization evaluation. The corpus served as the
basis for the shared task of the RepEval 2017 Workshop at EMNLP in Copenhagen.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 392702
`'validation_matched'` | 9815
`'validation_mismatched'` | 9832

*   **Features**:

```json
{
    "promptID": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "premise_binary_parse": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "premise_parse": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis_binary_parse": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis_parse": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "genre": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


