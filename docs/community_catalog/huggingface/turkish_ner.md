# turkish_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/turkish_ner)
*   [Huggingface](https://huggingface.co/datasets/turkish_ner)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:turkish_ner')
```

*   **Description**:

```
Turkish Wikipedia Named-Entity Recognition and Text Categorization
(TWNERTC) dataset is a collection of automatically categorized and annotated
sentences obtained from Wikipedia. The authors constructed large-scale
gazetteers by using a graph crawler algorithm to extract
relevant entity and domain information
from a semantic knowledge base, Freebase.
The constructed gazetteers contains approximately
300K entities with thousands of fine-grained entity types
under 77 different domains.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 532629

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
    "domain": {
        "num_classes": 25,
        "names": [
            "architecture",
            "basketball",
            "book",
            "business",
            "education",
            "fictional_universe",
            "film",
            "food",
            "geography",
            "government",
            "law",
            "location",
            "military",
            "music",
            "opera",
            "organization",
            "people",
            "religion",
            "royalty",
            "soccer",
            "sports",
            "theater",
            "time",
            "travel",
            "tv"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "O",
                "B-PERSON",
                "I-PERSON",
                "B-ORGANIZATION",
                "I-ORGANIZATION",
                "B-LOCATION",
                "I-LOCATION",
                "B-MISC",
                "I-MISC"
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


