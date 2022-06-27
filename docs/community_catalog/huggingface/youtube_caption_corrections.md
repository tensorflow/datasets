# youtube_caption_corrections

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/youtube_caption_corrections)
*   [Huggingface](https://huggingface.co/datasets/youtube_caption_corrections)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:youtube_caption_corrections')
```

*   **Description**:

```
Dataset built from pairs of YouTube captions where both 'auto-generated' and
'manually-corrected' captions are available for a single specified language.
This dataset labels two-way (e.g. ignoring single-sided insertions) same-length
token differences in the `diff_type` column. The `default_seq` is composed of
tokens from the 'auto-generated' captions. When a difference occurs between
the 'auto-generated' vs 'manually-corrected' captions types, the `correction_seq`
contains tokens from the 'manually-corrected' captions.
```

*   **License**: MIT License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10769

*   **Features**:

```json
{
    "video_ids": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "default_seq": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correction_seq": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "diff_type": {
        "feature": {
            "num_classes": 9,
            "names": [
                "NO_DIFF",
                "CASE_DIFF",
                "PUNCUATION_DIFF",
                "CASE_AND_PUNCUATION_DIFF",
                "STEM_BASED_DIFF",
                "DIGIT_DIFF",
                "INTRAWORD_PUNC_DIFF",
                "UNKNOWN_TYPE_DIFF",
                "RESERVED_DIFF"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


