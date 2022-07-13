# scicite

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/scicite)
*   [Huggingface](https://huggingface.co/datasets/scicite)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scicite')
```

*   **Description**:

```
This is a dataset for classifying citation intents in academic papers.
The main citation intent label for each Json object is specified with the label
key while the citation context is specified in with a context key. Example:
{
 'string': 'In chacma baboons, male-infant relationships can be linked to both
    formation of friendships and paternity success [30,31].'
 'sectionName': 'Introduction',
 'label': 'background',
 'citingPaperId': '7a6b2d4b405439',
 'citedPaperId': '9d1abadc55b5e0',
 ...
 }
You may obtain the full information about the paper using the provided paper ids
with the Semantic Scholar API (https://api.semanticscholar.org/).
The labels are:
Method, Background, Result
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1859
`'train'` | 8194
`'validation'` | 916

*   **Features**:

```json
{
    "string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sectionName": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "method",
            "background",
            "result"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "citingPaperId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "citedPaperId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "excerpt_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "isKeyCitation": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "label2": {
        "num_classes": 4,
        "names": [
            "supportive",
            "not_supportive",
            "cant_determine",
            "none"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "citeEnd": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "citeStart": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "num_classes": 7,
        "names": [
            "properNoun",
            "andPhrase",
            "acronym",
            "etAlPhrase",
            "explicit",
            "acronymParen",
            "nan"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "label_confidence": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "label2_confidence": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


