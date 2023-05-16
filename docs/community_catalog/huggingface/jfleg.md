# jfleg

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/jfleg)
*   [Huggingface](https://huggingface.co/datasets/jfleg)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:jfleg')
```

*   **Description**:

```
JFLEG (JHU FLuency-Extended GUG) is an English grammatical error correction (GEC) corpus.
It is a gold standard benchmark for developing and evaluating GEC systems with respect to
fluency (extent to which a text is native-sounding) as well as grammaticality.

For each source document, there are four human-written corrections (ref0 to ref3).
```

*   **License**: CC BY-NC-SA 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 748
`'validation'` | 755

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "corrections": {
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


