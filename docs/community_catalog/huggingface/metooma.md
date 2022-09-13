# metooma

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/metooma)
*   [Huggingface](https://huggingface.co/datasets/metooma)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:metooma')
```

*   **Description**:

```
The dataset consists of tweets belonging to #MeToo movement on Twitter, labelled into different categories.
Due to Twitter's development policies, we only provide the tweet ID's and corresponding labels,
other data can be fetched via Twitter API.
The data has been labelled by experts, with the majority taken into the account for deciding the final label.
We provide these labels for each of the tweets. The labels provided for each data point
includes -- Relevance, Directed Hate, Generalized Hate,
Sarcasm, Allegation, Justification, Refutation, Support, Oppose
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1995
`'train'` | 7978

*   **Features**:

```json
{
    "TweetId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Text_Only_Informative": {
        "num_classes": 2,
        "names": [
            "Text Non Informative",
            "Text Informative"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Image_Only_Informative": {
        "num_classes": 2,
        "names": [
            "Image Non Informative",
            "Image Informative"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Directed_Hate": {
        "num_classes": 2,
        "names": [
            "Directed Hate Absent",
            "Directed Hate Present"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Generalized_Hate": {
        "num_classes": 2,
        "names": [
            "Generalized Hate Absent",
            "Generalized Hate Present"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Sarcasm": {
        "num_classes": 2,
        "names": [
            "Sarcasm Absent",
            "Sarcasm Present"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Allegation": {
        "num_classes": 2,
        "names": [
            "Allegation Absent",
            "Allegation Present"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Justification": {
        "num_classes": 2,
        "names": [
            "Justification Absent",
            "Justification Present"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Refutation": {
        "num_classes": 2,
        "names": [
            "Refutation Absent",
            "Refutation Present"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Support": {
        "num_classes": 2,
        "names": [
            "Support Absent",
            "Support Present"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Oppose": {
        "num_classes": 2,
        "names": [
            "Oppose Absent",
            "Oppose Present"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


