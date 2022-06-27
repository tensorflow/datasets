# mac_morpho

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mac_morpho)
*   [Huggingface](https://huggingface.co/datasets/mac_morpho)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mac_morpho')
```

*   **Description**:

```
Mac-Morpho is a corpus of Brazilian Portuguese texts annotated with part-of-speech tags.
Its first version was released in 2003 [1], and since then, two revisions have been made in order
to improve the quality of the resource [2, 3].
The corpus is available for download split into train, development and test sections.
These are 76%, 4% and 20% of the corpus total, respectively (the reason for the unusual numbers
is that the corpus was first split into 80%/20% train/test, and then 5% of the train section was
set aside for development). This split was used in [3], and new POS tagging research with Mac-Morpho
is encouraged to follow it in order to make consistent comparisons possible.


[1] Aluísio, S., Pelizzoni, J., Marchi, A.R., de Oliveira, L., Manenti, R., Marquiafável, V. 2003.
An account of the challenge of tagging a reference corpus for brazilian portuguese.
In: Proceedings of the 6th International Conference on Computational Processing of the Portuguese Language. PROPOR 2003

[2] Fonseca, E.R., Rosa, J.L.G. 2013. Mac-morpho revisited: Towards robust part-of-speech.
In: Proceedings of the 9th Brazilian Symposium in Information and Human Language Technology – STIL

[3] Fonseca, E.R., Aluísio, Sandra Maria, Rosa, J.L.G. 2015.
Evaluating word embeddings and a revised corpus for part-of-speech tagging in Portuguese.
Journal of the Brazilian Computer Society.
```

*   **License**: Creative Commons Attribution 4.0 International License
*   **Version**: 3.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9987
`'train'` | 37948
`'validation'` | 1997

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
            "num_classes": 26,
            "names": [
                "PREP+PROADJ",
                "IN",
                "PREP+PRO-KS",
                "NPROP",
                "PREP+PROSUB",
                "KC",
                "PROPESS",
                "NUM",
                "PROADJ",
                "PREP+ART",
                "KS",
                "PRO-KS",
                "ADJ",
                "ADV-KS",
                "N",
                "PREP",
                "PROSUB",
                "PREP+PROPESS",
                "PDEN",
                "V",
                "PREP+ADV",
                "PCP",
                "CUR",
                "ADV",
                "PU",
                "ART"
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


