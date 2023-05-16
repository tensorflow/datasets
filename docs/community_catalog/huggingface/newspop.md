# newspop

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/newspop)
*   [Huggingface](https://huggingface.co/datasets/newspop)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:newspop')
```

*   **Description**:

```
This is a large data set of news items and their respective social feedback on multiple platforms: Facebook, Google+ and LinkedIn.
The collected data relates to a period of 8 months, between November 2015 and July 2016, accounting for about 100,000 news items on four different topics: economy, microsoft, obama and palestine.
This data set is tailored for evaluative comparisons in predictive analytics tasks, although allowing for tasks in other research areas such as topic detection and tracking, sentiment analysis in short text, first story detection or news recommendation.
```

*   **License**: Creative Commons Attribution 4.0 International License (CC-BY)
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 93239

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "headline": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "publish_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "facebook": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "google_plus": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "linked_in": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


