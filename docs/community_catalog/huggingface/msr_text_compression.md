# msr_text_compression

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/msr_text_compression)
*   [Huggingface](https://huggingface.co/datasets/msr_text_compression)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:msr_text_compression')
```

*   **Description**:

```
This dataset contains sentences and short paragraphs with corresponding shorter (compressed) versions. There are up to five compressions for each input text, together with quality judgements of their meaning preservation and grammaticality. The dataset is derived using source texts from the Open American National Corpus (ww.anc.org) and crowd-sourcing.
```

*   **License**: Microsoft Research Data License Agreement
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 785
`'train'` | 4936
`'validation'` | 447

*   **Features**:

```json
{
    "source_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "compressed_text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "judge_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "num_ratings": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "ratings": {
                "feature": {
                    "dtype": "int64",
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


