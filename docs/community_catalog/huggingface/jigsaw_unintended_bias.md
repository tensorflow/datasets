# jigsaw_unintended_bias

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/jigsaw_unintended_bias)
*   [Huggingface](https://huggingface.co/datasets/jigsaw_unintended_bias)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:jigsaw_unintended_bias')
```

*   **Description**:

```
A collection of comments from the defunct Civil Comments platform that have been annotated for their toxicity.
```

*   **License**: CC0 (both the dataset and underlying text)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test_private_leaderboard'` | 97320
`'test_public_leaderboard'` | 97320
`'train'` | 1804874

*   **Features**:

```json
{
    "target": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "comment_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "severe_toxicity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "obscene": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "identity_attack": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "insult": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "threat": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "asian": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "atheist": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "bisexual": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "black": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "buddhist": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "christian": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "female": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "heterosexual": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "hindu": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "homosexual_gay_or_lesbian": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "intellectual_or_learning_disability": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "jewish": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "latino": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "male": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "muslim": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "other_disability": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "other_gender": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "other_race_or_ethnicity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "other_religion": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "other_sexual_orientation": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "physical_disability": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "psychiatric_or_mental_illness": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "transgender": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "white": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "created_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "publication_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "parent_id": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "article_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "rating": {
        "num_classes": 2,
        "names": [
            "rejected",
            "approved"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "funny": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "wow": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "sad": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "likes": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "disagree": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "sexual_explicit": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "identity_annotator_count": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "toxicity_annotator_count": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


