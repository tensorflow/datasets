# species_800

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/species_800)
*   [Huggingface](https://huggingface.co/datasets/species_800)


## species_800


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:species_800/species_800')
```

*   **Description**:

```
We have developed an efficient algorithm and implementation of a dictionary-based approach to named entity recognition,
which we here use to identifynames of species and other taxa in text. The tool, SPECIES, is more than an order of
magnitude faster and as accurate as existing tools. The precision and recall was assessed both on an existing gold-standard
corpus and on a new corpus of 800 abstracts, which were manually annotated after the development of the tool. The corpus
comprises abstracts from journals selected to represent many taxonomic groups, which gives insights into which types of
organism names are hard to detect and which are easy. Finally, we have tagged organism names in the entire Medline database
and developed a web resource, ORGANISMS, that makes the results accessible to the broad community of biologists.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1631
`'train'` | 5734
`'validation'` | 831

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
            "num_classes": 3,
            "names": [
                "O",
                "B",
                "I"
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


