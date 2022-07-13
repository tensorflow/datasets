# tamilmixsentiment

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tamilmixsentiment)
*   [Huggingface](https://huggingface.co/datasets/tamilmixsentiment)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tamilmixsentiment')
```

*   **Description**:

```
The first gold standard Tamil-English code-switched, sentiment-annotated corpus containing 15,744 comment posts from YouTube. Train: 11,335 Validation: 1,260 and Test: 3,149.  This makes the largest general domain sentiment dataset for this relatively low-resource language with code-mixing phenomenon.  The dataset contains all the three types of code-mixed sentences - Inter-Sentential switch, Intra-Sentential switch and Tag switching. Most comments were written in Roman script with either Tamil grammar with English lexicon or English grammar with Tamil lexicon. Some comments were written in Tamil script with English expressions in between.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3149
`'train'` | 11335
`'validation'` | 1260

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 5,
        "names": [
            "Positive",
            "Negative",
            "Mixed_feelings",
            "unknown_state",
            "not-Tamil"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


