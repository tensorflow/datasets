# hippocorpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hippocorpus)
*   [Huggingface](https://huggingface.co/datasets/hippocorpus)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hippocorpus')
```

*   **Description**:

```
To examine the cognitive processes of remembering and imagining and their traces in language, we introduce Hippocorpus, a dataset of 6,854 English diary-like short stories about recalled and imagined events. Using a crowdsourcing framework, we first collect recalled stories and summaries from workers, then provide these summaries to other workers who write imagined stories. Finally, months later, we collect a retold version of the recalled stories from a subset of recalled authors. Our dataset comes paired with author demographics (age, gender, race), their openness to experience, as well as some variables regarding the author's relationship to the event (e.g., how personal the event is, how often they tell its story, etc.).
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6854

*   **Features**:

```json
{
    "AssignmentId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "WorkTimeInSeconds": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "WorkerId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotatorAge": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "annotatorGender": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotatorRace": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distracted": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "draining": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "frequency": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "importance": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "logTimeSinceEvent": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "mainEvent": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "memType": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "mostSurprising": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "openness": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "recAgnPairId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "recImgPairId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "similarity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "similarityReason": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "story": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stressful": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "timeSinceEvent": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


