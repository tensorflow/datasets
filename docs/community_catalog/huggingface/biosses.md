# biosses

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/biosses)
*   [Huggingface](https://huggingface.co/datasets/biosses)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:biosses')
```

*   **Description**:

```
BIOSSES is a benchmark dataset for biomedical sentence similarity estimation. The dataset comprises 100 sentence pairs, in which each sentence was selected from the TAC (Text Analysis Conference) Biomedical Summarization Track Training Dataset containing articles from the biomedical domain. The sentence pairs were evaluated by five different human experts that judged their similarity and gave scores ranging from 0 (no relation) to 4 (equivalent).
```

*   **License**: BIOSSES is made available under the terms of The GNU Common Public License v.3.0.

*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 100

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


