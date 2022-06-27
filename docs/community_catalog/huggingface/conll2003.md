# conll2003

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/conll2003)
*   [Huggingface](https://huggingface.co/datasets/conll2003)


## conll2003


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conll2003/conll2003')
```

*   **Description**:

```
The shared task of CoNLL-2003 concerns language-independent named entity recognition. We will concentrate on
four types of named entities: persons, locations, organizations and names of miscellaneous entities that do
not belong to the previous three groups.

The CoNLL-2003 shared task data files contain four columns separated by a single space. Each word has been put on
a separate line and there is an empty line after each sentence. The first item on each line is a word, the second
a part-of-speech (POS) tag, the third a syntactic chunk tag and the fourth the named entity tag. The chunk tags
and the named entity tags have the format I-TYPE which means that the word is inside a phrase of type TYPE. Only
if two phrases of the same type immediately follow each other, the first word of the second phrase will have tag
B-TYPE to show that it starts a new phrase. A word with tag O is not part of a phrase. Note the dataset uses IOB2
tagging scheme, whereas the original dataset uses IOB1.

For more details see https://www.clips.uantwerpen.be/conll2003/ner/ and https://www.aclweb.org/anthology/W03-0419
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3454
`'train'` | 14042
`'validation'` | 3251

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
    "pos_tags": {
        "feature": {
            "num_classes": 47,
            "names": [
                "\"",
                "''",
                "#",
                "$",
                "(",
                ")",
                ",",
                ".",
                ":",
                "``",
                "CC",
                "CD",
                "DT",
                "EX",
                "FW",
                "IN",
                "JJ",
                "JJR",
                "JJS",
                "LS",
                "MD",
                "NN",
                "NNP",
                "NNPS",
                "NNS",
                "NN|SYM",
                "PDT",
                "POS",
                "PRP",
                "PRP$",
                "RB",
                "RBR",
                "RBS",
                "RP",
                "SYM",
                "TO",
                "UH",
                "VB",
                "VBD",
                "VBG",
                "VBN",
                "VBP",
                "VBZ",
                "WDT",
                "WP",
                "WP$",
                "WRB"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "chunk_tags": {
        "feature": {
            "num_classes": 23,
            "names": [
                "O",
                "B-ADJP",
                "I-ADJP",
                "B-ADVP",
                "I-ADVP",
                "B-CONJP",
                "I-CONJP",
                "B-INTJ",
                "I-INTJ",
                "B-LST",
                "I-LST",
                "B-NP",
                "I-NP",
                "B-PP",
                "I-PP",
                "B-PRT",
                "I-PRT",
                "B-SBAR",
                "I-SBAR",
                "B-UCP",
                "I-UCP",
                "B-VP",
                "I-VP"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
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


