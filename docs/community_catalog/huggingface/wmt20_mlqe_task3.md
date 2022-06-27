# wmt20_mlqe_task3

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wmt20_mlqe_task3)
*   [Huggingface](https://huggingface.co/datasets/wmt20_mlqe_task3)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task3/plain_text')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

The goal of this task 3 is to predict document-level quality scores as well as fine-grained annotations.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 180
`'train'` | 1448
`'validation'` | 200

*   **Features**:

```json
{
    "document_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source_segments": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "source_tokenized": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mt_segments": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mt_tokenized": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "annotations": {
        "feature": {
            "segment_id": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "annotation_start": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "annotation_length": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "severity": {
                "num_classes": 3,
                "names": [
                    "minor",
                    "major",
                    "critical"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "severity_weight": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "category": {
                "num_classes": 45,
                "names": [
                    "Addition",
                    "Agreement",
                    "Ambiguous Translation",
                    "Capitalization",
                    "Character Encoding",
                    "Company Terminology",
                    "Date/Time",
                    "Diacritics",
                    "Duplication",
                    "False Friend",
                    "Grammatical Register",
                    "Hyphenation",
                    "Inconsistency",
                    "Lexical Register",
                    "Lexical Selection",
                    "Named Entity",
                    "Number",
                    "Omitted Auxiliary Verb",
                    "Omitted Conjunction",
                    "Omitted Determiner",
                    "Omitted Preposition",
                    "Omitted Pronoun",
                    "Orthography",
                    "Other POS Omitted",
                    "Over-translation",
                    "Overly Literal",
                    "POS",
                    "Punctuation",
                    "Shouldn't Have Been Translated",
                    "Shouldn't have been translated",
                    "Spelling",
                    "Tense/Mood/Aspect",
                    "Under-translation",
                    "Unidiomatic",
                    "Unintelligible",
                    "Unit Conversion",
                    "Untranslated",
                    "Whitespace",
                    "Word Order",
                    "Wrong Auxiliary Verb",
                    "Wrong Conjunction",
                    "Wrong Determiner",
                    "Wrong Language Variety",
                    "Wrong Preposition",
                    "Wrong Pronoun"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "token_annotations": {
        "feature": {
            "segment_id": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "first_token": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "last_token": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "token_after_gap": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "severity": {
                "num_classes": 3,
                "names": [
                    "minor",
                    "major",
                    "critical"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "category": {
                "num_classes": 45,
                "names": [
                    "Addition",
                    "Agreement",
                    "Ambiguous Translation",
                    "Capitalization",
                    "Character Encoding",
                    "Company Terminology",
                    "Date/Time",
                    "Diacritics",
                    "Duplication",
                    "False Friend",
                    "Grammatical Register",
                    "Hyphenation",
                    "Inconsistency",
                    "Lexical Register",
                    "Lexical Selection",
                    "Named Entity",
                    "Number",
                    "Omitted Auxiliary Verb",
                    "Omitted Conjunction",
                    "Omitted Determiner",
                    "Omitted Preposition",
                    "Omitted Pronoun",
                    "Orthography",
                    "Other POS Omitted",
                    "Over-translation",
                    "Overly Literal",
                    "POS",
                    "Punctuation",
                    "Shouldn't Have Been Translated",
                    "Shouldn't have been translated",
                    "Spelling",
                    "Tense/Mood/Aspect",
                    "Under-translation",
                    "Unidiomatic",
                    "Unintelligible",
                    "Unit Conversion",
                    "Untranslated",
                    "Whitespace",
                    "Word Order",
                    "Wrong Auxiliary Verb",
                    "Wrong Conjunction",
                    "Wrong Determiner",
                    "Wrong Language Variety",
                    "Wrong Preposition",
                    "Wrong Pronoun"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "token_index": {
        "feature": {
            "feature": {
                "feature": {
                    "dtype": "int32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "total_words": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


