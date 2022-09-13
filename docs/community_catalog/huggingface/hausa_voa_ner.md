# hausa_voa_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hausa_voa_ner)
*   [Huggingface](https://huggingface.co/datasets/hausa_voa_ner)


## hausa_voa_ner


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hausa_voa_ner/hausa_voa_ner')
```

*   **Description**:

```
The Hausa VOA NER dataset is a labeled dataset for named entity recognition in Hausa. The texts were obtained from
Hausa Voice of America News articles https://www.voahausa.com/ . We concentrate on
four types of named entities: persons [PER], locations [LOC], organizations [ORG], and dates & time [DATE].

The Hausa VOA NER data files contain 2 columns separated by a tab ('	'). Each word has been put on a separate line and
there is an empty line after each sentences i.e the CoNLL format. The first item on each line is a word, the second
is the named entity tag. The named entity tags have the format I-TYPE which means that the word is inside a phrase
of type TYPE. For every multi-word expression like 'New York', the first word gets a tag B-TYPE and the subsequent words
have tags I-TYPE, a word with tag O is not part of a phrase. The dataset is in the BIO tagging scheme.

For more details, see https://www.aclweb.org/anthology/2020.emnlp-main.204/
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 292
`'train'` | 1015
`'validation'` | 146

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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


