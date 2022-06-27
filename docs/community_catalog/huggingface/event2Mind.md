# event2Mind

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/event2Mind)
*   [Huggingface](https://huggingface.co/datasets/event2Mind)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:event2Mind')
```

*   **Description**:

```
In Event2Mind, we explore the task of understanding stereotypical intents and reactions to events. Through crowdsourcing, we create a large corpus with 25,000 events and free-form descriptions of their intents and reactions, both of the event's subject and (potentially implied) other participants.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5221
`'train'` | 46472
`'validation'` | 5401

*   **Features**:

```json
{
    "Source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Event": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Xintent": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Xemotion": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Otheremotion": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Xsent": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Osent": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


