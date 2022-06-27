# multi_nli_mismatch

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multi_nli_mismatch)
*   [Huggingface](https://huggingface.co/datasets/multi_nli_mismatch)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_nli_mismatch/plain_text')
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
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 392702
`'validation'` | 10000

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


