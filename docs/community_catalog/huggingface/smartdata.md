# smartdata

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/smartdata)
*   [Huggingface](https://huggingface.co/datasets/smartdata)


## smartdata-v3_20200302


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:smartdata/smartdata-v3_20200302')
```

*   **Description**:

```
DFKI SmartData Corpus is a dataset of 2598 German-language documents
which has been annotated with fine-grained geo-entities, such as streets,
stops and routes, as well as standard named entity types. It has also
been annotated with a set of 15 traffic- and industry-related n-ary
relations and events, such as Accidents, Traffic jams, Acquisitions,
and Strikes. The corpus consists of newswire texts, Twitter messages,
and traffic reports from radio stations, police and railway companies.
It allows for training and evaluating both named entity recognition
algorithms that aim for fine-grained typing of geo-entities, as well
as n-ary relation extraction systems.
```

*   **License**: CC-BY 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 230
`'train'` | 1861
`'validation'` | 228

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
            "num_classes": 33,
            "names": [
                "O",
                "B-DATE",
                "I-DATE",
                "B-DISASTER_TYPE",
                "I-DISASTER_TYPE",
                "B-DISTANCE",
                "I-DISTANCE",
                "B-DURATION",
                "I-DURATION",
                "B-LOCATION",
                "I-LOCATION",
                "B-LOCATION_CITY",
                "I-LOCATION_CITY",
                "B-LOCATION_ROUTE",
                "I-LOCATION_ROUTE",
                "B-LOCATION_STOP",
                "I-LOCATION_STOP",
                "B-LOCATION_STREET",
                "I-LOCATION_STREET",
                "B-NUMBER",
                "I-NUMBER",
                "B-ORGANIZATION",
                "I-ORGANIZATION",
                "B-ORGANIZATION_COMPANY",
                "I-ORGANIZATION_COMPANY",
                "B-ORG_POSITION",
                "I-ORG_POSITION",
                "B-PERSON",
                "I-PERSON",
                "B-TIME",
                "I-TIME",
                "B-TRIGGER",
                "I-TRIGGER"
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


