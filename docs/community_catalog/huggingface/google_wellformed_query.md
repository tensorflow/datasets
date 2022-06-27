# google_wellformed_query

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/google_wellformed_query)
*   [Huggingface](https://huggingface.co/datasets/google_wellformed_query)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:google_wellformed_query')
```

*   **Description**:

```
Google's query wellformedness dataset was created by crowdsourcing well-formedness annotations for 25,100 queries from the Paralex corpus. Every query was annotated by five raters each with 1/0 rating of whether or not the query is well-formed.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3850
`'train'` | 17500
`'validation'` | 3750

*   **Features**:

```json
{
    "rating": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


