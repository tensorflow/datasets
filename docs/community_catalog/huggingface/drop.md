# drop

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/drop)
*   [Huggingface](https://huggingface.co/datasets/drop)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:drop')
```

*   **Description**:

```
DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs.
. DROP is a crowdsourced, adversarially-created, 96k-question benchmark, in which a system must resolve references in a
question, perhaps to multiple input positions, and perform discrete operations over them (such as addition, counting, or
 sorting). These operations require a much more comprehensive understanding of the content of paragraphs than what was
 necessary for prior datasets.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 77400
`'validation'` | 9535

*   **Features**:

```json
{
    "section_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "passage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers_spans": {
        "feature": {
            "spans": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "types": {
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


