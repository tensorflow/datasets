# samsum

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/samsum)
*   [Huggingface](https://huggingface.co/datasets/samsum)


## samsum


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:samsum/samsum')
```

*   **Description**:

```
SAMSum Corpus contains over 16k chat dialogues with manually annotated
summaries.
There are two features:
  - dialogue: text of dialogue.
  - summary: human written summary of the dialogue.
  - id: id of a example.
```

*   **License**: CC BY-NC-ND 4.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 819
`'train'` | 14732
`'validation'` | 818

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dialogue": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


