# sem_eval_2020_task_11

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sem_eval_2020_task_11)
*   [Huggingface](https://huggingface.co/datasets/sem_eval_2020_task_11)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sem_eval_2020_task_11')
```

*   **Description**:

```
Propagandistic news articles use specific techniques to convey their message,
such as whataboutism, red Herring, and name calling, among many others.
The Propaganda Techniques Corpus (PTC) allows to study automatic algorithms to
detect them. We provide a permanent leaderboard to allow researchers both to
advertise their progress and to be up-to-speed with the state of the art on the
tasks offered (see below for a definition).
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 90
`'train'` | 371
`'validation'` | 75

*   **Features**:

```json
{
    "article_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span_identification": {
        "feature": {
            "start_char_offset": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "end_char_offset": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "technique_classification": {
        "feature": {
            "start_char_offset": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "end_char_offset": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "technique": {
                "num_classes": 14,
                "names": [
                    "Appeal_to_Authority",
                    "Appeal_to_fear-prejudice",
                    "Bandwagon,Reductio_ad_hitlerum",
                    "Black-and-White_Fallacy",
                    "Causal_Oversimplification",
                    "Doubt",
                    "Exaggeration,Minimisation",
                    "Flag-Waving",
                    "Loaded_Language",
                    "Name_Calling,Labeling",
                    "Repetition",
                    "Slogans",
                    "Thought-terminating_Cliches",
                    "Whataboutism,Straw_Men,Red_Herring"
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
}
```


