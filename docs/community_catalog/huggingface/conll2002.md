# conll2002

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/conll2002)
*   [Huggingface](https://huggingface.co/datasets/conll2002)


## es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conll2002/es')
```

*   **Description**:

```
Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .

The shared task of CoNLL-2002 concerns language-independent named entity recognition.
We will concentrate on four types of named entities: persons, locations, organizations and names of miscellaneous entities that do not belong to the previous three groups.
The participants of the shared task will be offered training and test data for at least two languages.
They will use the data for developing a named-entity recognition system that includes a machine learning component.
Information sources other than the training data may be used in this shared task.
We are especially interested in methods that can use additional unannotated data for improving their performance (for example co-training).

The train/validation/test sets are available in Spanish and Dutch.

For more details see https://www.clips.uantwerpen.be/conll2002/ner/ and https://www.aclweb.org/anthology/W02-2024/
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1518
`'train'` | 8324
`'validation'` | 1916

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
            "num_classes": 60,
            "names": [
                "AO",
                "AQ",
                "CC",
                "CS",
                "DA",
                "DE",
                "DD",
                "DI",
                "DN",
                "DP",
                "DT",
                "Faa",
                "Fat",
                "Fc",
                "Fd",
                "Fe",
                "Fg",
                "Fh",
                "Fia",
                "Fit",
                "Fp",
                "Fpa",
                "Fpt",
                "Fs",
                "Ft",
                "Fx",
                "Fz",
                "I",
                "NC",
                "NP",
                "P0",
                "PD",
                "PI",
                "PN",
                "PP",
                "PR",
                "PT",
                "PX",
                "RG",
                "RN",
                "SP",
                "VAI",
                "VAM",
                "VAN",
                "VAP",
                "VAS",
                "VMG",
                "VMI",
                "VMM",
                "VMN",
                "VMP",
                "VMS",
                "VSG",
                "VSI",
                "VSM",
                "VSN",
                "VSP",
                "VSS",
                "Y",
                "Z"
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



## nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conll2002/nl')
```

*   **Description**:

```
Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .

The shared task of CoNLL-2002 concerns language-independent named entity recognition.
We will concentrate on four types of named entities: persons, locations, organizations and names of miscellaneous entities that do not belong to the previous three groups.
The participants of the shared task will be offered training and test data for at least two languages.
They will use the data for developing a named-entity recognition system that includes a machine learning component.
Information sources other than the training data may be used in this shared task.
We are especially interested in methods that can use additional unannotated data for improving their performance (for example co-training).

The train/validation/test sets are available in Spanish and Dutch.

For more details see https://www.clips.uantwerpen.be/conll2002/ner/ and https://www.aclweb.org/anthology/W02-2024/
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5196
`'train'` | 15807
`'validation'` | 2896

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
            "num_classes": 12,
            "names": [
                "Adj",
                "Adv",
                "Art",
                "Conj",
                "Int",
                "Misc",
                "N",
                "Num",
                "Prep",
                "Pron",
                "Punc",
                "V"
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


