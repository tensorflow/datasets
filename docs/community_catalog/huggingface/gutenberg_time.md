# gutenberg_time

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/gutenberg_time)
*   [Huggingface](https://huggingface.co/datasets/gutenberg_time)


## gutenberg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:gutenberg_time/gutenberg')
```

*   **Description**:

```
A clean data resource containing all explicit time references in a dataset of 52,183 novels whose full text is available via Project Gutenberg.
```

*   **License**: [More Information needed]
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 120694

*   **Features**:

```json
{
    "guten_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hour_reference": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "time_phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "is_ambiguous": {
        "dtype": "bool_",
        "id": null,
        "_type": "Value"
    },
    "time_pos_start": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "time_pos_end": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "tok_context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


