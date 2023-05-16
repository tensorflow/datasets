# multi_x_science_sum

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multi_x_science_sum)
*   [Huggingface](https://huggingface.co/datasets/multi_x_science_sum)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_x_science_sum')
```

*   **Description**:

```
Multi-XScience,a large-scale multi-document summarization dataset created from scientific articles. Multi-XScience introduces a challenging multi-document summarization task: writing therelated-work section of a paper based on itsabstract and the articles it references.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5093
`'train'` | 30369
`'validation'` | 5066

*   **Features**:

```json
{
    "aid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "mid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "abstract": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "related_work": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ref_abstract": {
        "feature": {
            "cite_N": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "mid": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "abstract": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


