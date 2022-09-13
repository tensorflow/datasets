# coached_conv_pref

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/coached_conv_pref)
*   [Huggingface](https://huggingface.co/datasets/coached_conv_pref)


## coached_conv_pref


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:coached_conv_pref/coached_conv_pref')
```

*   **Description**:

```
A dataset consisting of 502 English dialogs with 12,000 annotated utterances between a user and an assistant discussing
movie preferences in natural language. It was collected using a Wizard-of-Oz methodology between two paid crowd-workers,
where one worker plays the role of an 'assistant', while the other plays the role of a 'user'. The 'assistant' elicits
the 'user’s' preferences about movies following a Coached Conversational Preference Elicitation (CCPE) method. The
assistant asks questions designed to minimize the bias in the terminology the 'user' employs to convey his or her
preferences as much as possible, and to obtain these preferences in natural language. Each dialog is annotated with
entity mentions, preferences expressed about entities, descriptions of entities provided, and other statements of
entities.
```

*   **License**: https://creativecommons.org/licenses/by-sa/4.0/
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 502

*   **Features**:

```json
{
    "conversationId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterances": {
        "feature": {
            "index": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "speaker": {
                "num_classes": 2,
                "names": [
                    "USER",
                    "ASSISTANT"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "segments": {
                "feature": {
                    "startIndex": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "endIndex": {
                        "dtype": "int32",
                        "id": null,
                        "_type": "Value"
                    },
                    "text": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "annotations": {
                        "feature": {
                            "annotationType": {
                                "num_classes": 4,
                                "names": [
                                    "ENTITY_NAME",
                                    "ENTITY_PREFERENCE",
                                    "ENTITY_DESCRIPTION",
                                    "ENTITY_OTHER"
                                ],
                                "names_file": null,
                                "id": null,
                                "_type": "ClassLabel"
                            },
                            "entityType": {
                                "num_classes": 4,
                                "names": [
                                    "MOVIE_GENRE_OR_CATEGORY",
                                    "MOVIE_OR_SERIES",
                                    "PERSON",
                                    "SOMETHING_ELSE"
                                ],
                                "names_file": null,
                                "id": null,
                                "_type": "ClassLabel"
                            }
                        },
                        "length": -1,
                        "id": null,
                        "_type": "Sequence"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


