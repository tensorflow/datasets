# turk

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/turk)
*   [Huggingface](https://huggingface.co/datasets/turk)


## simplification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:turk/simplification')
```

*   **Description**:

```
TURKCorpus is a dataset for evaluating sentence simplification systems that focus on lexical paraphrasing,
as described in "Optimizing Statistical Machine Translation for Text Simplification". The corpus is composed of 2000 validation and 359 test original sentences that were each simplified 8 times by different annotators.
```

*   **License**: GNU General Public License v3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 359
`'validation'` | 2000

*   **Features**:

```json
{
    "original": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simplifications": {
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


