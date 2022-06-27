# trec

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/trec)
*   [Huggingface](https://huggingface.co/datasets/trec)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:trec')
```

*   **Description**:

```
The Text REtrieval Conference (TREC) Question Classification dataset contains 5500 labeled questions in training set and another 500 for test set. The dataset has 6 labels, 47 level-2 labels. Average length of each sentence is 10, vocabulary size of 8700.

Data are collected from four sources: 4,500 English questions published by USC (Hovy et al., 2001), about 500 manually constructed questions for a few rare classes, 894 TREC 8 and TREC 9 questions, and also 500 questions from TREC 10 which serves as the test set.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 5452

*   **Features**:

```json
{
    "label-coarse": {
        "num_classes": 6,
        "names": [
            "DESC",
            "ENTY",
            "ABBR",
            "HUM",
            "NUM",
            "LOC"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "label-fine": {
        "num_classes": 47,
        "names": [
            "manner",
            "cremat",
            "animal",
            "exp",
            "ind",
            "gr",
            "title",
            "def",
            "date",
            "reason",
            "event",
            "state",
            "desc",
            "count",
            "other",
            "letter",
            "religion",
            "food",
            "country",
            "color",
            "termeq",
            "city",
            "body",
            "dismed",
            "mount",
            "money",
            "product",
            "period",
            "substance",
            "sport",
            "plant",
            "techmeth",
            "volsize",
            "instru",
            "abb",
            "speed",
            "word",
            "lang",
            "perc",
            "code",
            "dist",
            "temp",
            "symbol",
            "ord",
            "veh",
            "weight",
            "currency"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


