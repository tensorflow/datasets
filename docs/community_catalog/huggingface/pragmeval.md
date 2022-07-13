# pragmeval

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/pragmeval)
*   [Huggingface](https://huggingface.co/datasets/pragmeval)


## verifiability


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/verifiability')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2424
`'train'` | 5712
`'validation'` | 634

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "experiential",
            "unverifiable",
            "non-experiential"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## emobank-arousal


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/emobank-arousal')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 683
`'train'` | 5470
`'validation'` | 684

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## switchboard


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/switchboard')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 649
`'train'` | 18930
`'validation'` | 2113

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 41,
        "names": [
            "Response Acknowledgement",
            "Uninterpretable",
            "Or-Clause",
            "Reject",
            "Statement-non-opinion",
            "3rd-party-talk",
            "Repeat-phrase",
            "Hold Before Answer/Agreement",
            "Signal-non-understanding",
            "Offers, Options Commits",
            "Agree/Accept",
            "Dispreferred Answers",
            "Hedge",
            "Action-directive",
            "Tag-Question",
            "Self-talk",
            "Yes-No-Question",
            "Rhetorical-Question",
            "No Answers",
            "Open-Question",
            "Conventional-closing",
            "Other Answers",
            "Acknowledge (Backchannel)",
            "Wh-Question",
            "Declarative Wh-Question",
            "Thanking",
            "Yes Answers",
            "Affirmative Non-yes Answers",
            "Declarative Yes-No-Question",
            "Backchannel in Question Form",
            "Apology",
            "Downplayer",
            "Conventional-opening",
            "Collaborative Completion",
            "Summarize/Reformulate",
            "Negative Non-no Answers",
            "Statement-opinion",
            "Appreciation",
            "Other",
            "Quotation",
            "Maybe/Accept-part"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## persuasiveness-eloquence


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/persuasiveness-eloquence')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 90
`'train'` | 725
`'validation'` | 91

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## mrda


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/mrda')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6459
`'train'` | 14484
`'validation'` | 1630

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 51,
        "names": [
            "Declarative-Question",
            "Statement",
            "Reject",
            "Or-Clause",
            "3rd-party-talk",
            "Continuer",
            "Hold Before Answer/Agreement",
            "Assessment/Appreciation",
            "Signal-non-understanding",
            "Floor Holder",
            "Sympathy",
            "Dispreferred Answers",
            "Reformulate/Summarize",
            "Exclamation",
            "Interrupted/Abandoned/Uninterpretable",
            "Expansions of y/n Answers",
            "Action-directive",
            "Tag-Question",
            "Accept",
            "Rhetorical-question Continue",
            "Self-talk",
            "Rhetorical-Question",
            "Yes-No-question",
            "Open-Question",
            "Rising Tone",
            "Other Answers",
            "Commit",
            "Wh-Question",
            "Repeat",
            "Follow Me",
            "Thanking",
            "Offer",
            "About-task",
            "Reject-part",
            "Affirmative Non-yes Answers",
            "Apology",
            "Downplayer",
            "Humorous Material",
            "Accept-part",
            "Collaborative Completion",
            "Mimic Other",
            "Understanding Check",
            "Misspeak Self-Correction",
            "Or-Question",
            "Topic Change",
            "Negative Non-no Answers",
            "Floor Grabber",
            "Correct-misspeaking",
            "Maybe",
            "Acknowledge-answer",
            "Defending/Explanation"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## gum


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/gum')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 248
`'train'` | 1700
`'validation'` | 259

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 17,
        "names": [
            "preparation",
            "evaluation",
            "circumstance",
            "solutionhood",
            "justify",
            "result",
            "evidence",
            "purpose",
            "concession",
            "elaboration",
            "background",
            "condition",
            "cause",
            "restatement",
            "motivation",
            "antithesis",
            "no_relation"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## emergent


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/emergent')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 259
`'train'` | 2076
`'validation'` | 259

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "observing",
            "for",
            "against"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## persuasiveness-relevance


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/persuasiveness-relevance')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 90
`'train'` | 725
`'validation'` | 91

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## persuasiveness-specificity


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/persuasiveness-specificity')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 62
`'train'` | 504
`'validation'` | 62

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## persuasiveness-strength


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/persuasiveness-strength')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 46
`'train'` | 371
`'validation'` | 46

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## emobank-dominance


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/emobank-dominance')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 798
`'train'` | 6392
`'validation'` | 798

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## squinky-implicature


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/squinky-implicature')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 465
`'train'` | 3724
`'validation'` | 465

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## sarcasm


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/sarcasm')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 469
`'train'` | 3754
`'validation'` | 469

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "notsarc",
            "sarc"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## squinky-formality


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/squinky-formality')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 452
`'train'` | 3622
`'validation'` | 453

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## stac


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/stac')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1304
`'train'` | 11230
`'validation'` | 1247

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 18,
        "names": [
            "Comment",
            "Contrast",
            "Q_Elab",
            "Parallel",
            "Explanation",
            "Narration",
            "Continuation",
            "Result",
            "Acknowledgement",
            "Alternation",
            "Question_answer_pair",
            "Correction",
            "Clarification_question",
            "Conditional",
            "Sequence",
            "Elaboration",
            "Background",
            "no_relation"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## pdtb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/pdtb')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1085
`'train'` | 12907
`'validation'` | 1204

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 16,
        "names": [
            "Synchrony",
            "Contrast",
            "Asynchronous",
            "Conjunction",
            "List",
            "Condition",
            "Pragmatic concession",
            "Restatement",
            "Pragmatic cause",
            "Alternative",
            "Pragmatic condition",
            "Pragmatic contrast",
            "Instantiation",
            "Exception",
            "Cause",
            "Concession"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## persuasiveness-premisetype


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/persuasiveness-premisetype')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 70
`'train'` | 566
`'validation'` | 71

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 8,
        "names": [
            "testimony",
            "warrant",
            "invented_instance",
            "common_knowledge",
            "statistics",
            "analogy",
            "definition",
            "real_example"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## squinky-informativeness


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/squinky-informativeness')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 464
`'train'` | 3719
`'validation'` | 465

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## persuasiveness-claimtype


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/persuasiveness-claimtype')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 19
`'train'` | 160
`'validation'` | 20

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "Value",
            "Fact",
            "Policy"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## emobank-valence


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:pragmeval/emobank-valence')
```

*   **Description**:

```
Evaluation of language understanding with a 11 datasets benchmark focusing on discourse and pragmatics
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 643
`'train'` | 5150
`'validation'` | 644

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "low",
            "high"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


