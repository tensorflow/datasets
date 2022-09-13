# disaster_response_messages

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/disaster_response_messages)
*   [Huggingface](https://huggingface.co/datasets/disaster_response_messages)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:disaster_response_messages')
```

*   **Description**:

```
This dataset contains 30,000 messages drawn from events including an earthquake in Haiti in 2010, an earthquake in Chile in 2010, floods in Pakistan in 2010, super-storm Sandy in the U.S.A. in 2012, and news articles spanning a large number of years and 100s of different disasters.
The data has been encoded with 36 different categories related to disaster response and has been stripped of messages with sensitive information in their entirety.
Upon release, this is the featured dataset of a new Udacity course on Data Science and the AI4ALL summer school and is especially utile for text analytics and natural language processing (NLP) tasks and models.
The input data in this job contains thousands of untranslated disaster-related messages and their English translations.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2629
`'train'` | 21046
`'validation'` | 2573

*   **Features**:

```json
{
    "split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "message": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "genre": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "related": {
        "num_classes": 3,
        "names": [
            "false",
            "true",
            "maybe"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "PII": {
        "dtype": "int8",
        "id": null,
        "_type": "Value"
    },
    "request": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "offer": {
        "dtype": "int8",
        "id": null,
        "_type": "Value"
    },
    "aid_related": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "medical_help": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "medical_products": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "search_and_rescue": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "security": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "military": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "child_alone": {
        "dtype": "int8",
        "id": null,
        "_type": "Value"
    },
    "water": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "food": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "shelter": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "clothing": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "money": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "missing_people": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "refugees": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "death": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "other_aid": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "infrastructure_related": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "transport": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "buildings": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "electricity": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "tools": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "hospitals": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "shops": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "aid_centers": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "other_infrastructure": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "weather_related": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "floods": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "storm": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "fire": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "earthquake": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "cold": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "other_weather": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "direct_report": {
        "num_classes": 2,
        "names": [
            "false",
            "true"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


