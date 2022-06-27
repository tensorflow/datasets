# nkjp-ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/nkjp-ner)
*   [Huggingface](https://huggingface.co/datasets/nkjp-ner)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nkjp-ner')
```

*   **Description**:

```
The NKJP-NER is based on a human-annotated part of National Corpus of Polish (NKJP). We extracted sentences with named entities of exactly one type. The task is to predict the type of the named entity.
```

*   **License**: GNU GPL v.3
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2058
`'train'` | 15794
`'validation'` | 1941

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "num_classes": 6,
        "names": [
            "geogName",
            "noEntity",
            "orgName",
            "persName",
            "placeName",
            "time"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


