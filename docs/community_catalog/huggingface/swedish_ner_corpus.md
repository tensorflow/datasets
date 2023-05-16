# swedish_ner_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/swedish_ner_corpus)
*   [Huggingface](https://huggingface.co/datasets/swedish_ner_corpus)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swedish_ner_corpus')
```

*   **Description**:

```
Webbnyheter 2012 from Spraakbanken, semi-manually annotated and adapted for CoreNLP Swedish NER. Semi-manually defined in this case as: Bootstrapped from Swedish Gazetters then manually correcte/reviewed by two independent native speaking swedish annotators. No annotator agreement calculated.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2453
`'train'` | 6886

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 5,
            "names": [
                "0",
                "LOC",
                "MISC",
                "ORG",
                "PER"
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


