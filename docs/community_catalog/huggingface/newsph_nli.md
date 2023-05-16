# newsph_nli

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/newsph_nli)
*   [Huggingface](https://huggingface.co/datasets/newsph_nli)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:newsph_nli')
```

*   **Description**:

```
First benchmark dataset for sentence entailment in the low-resource Filipino language. Constructed through exploting the structure of news articles. Contains 600,000 premise-hypothesis pairs, in 70-15-15 split for training, validation, and testing.
```

*   **License**: Filipino-Text-Benchmarks is licensed under the GNU General Public License v3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9000
`'train'` | 420000
`'validation'` | 90000

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


