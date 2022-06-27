# social_bias_frames

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/social_bias_frames)
*   [Huggingface](https://huggingface.co/datasets/social_bias_frames)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:social_bias_frames')
```

*   **Description**:

```
Social Bias Frames is a new way of representing the biases and offensiveness that are implied in language.
For example, these frames are meant to distill the implication that "women (candidates) are less qualified"
behind the statement "we shouldn’t lower our standards to hire more women."
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 17501
`'train'` | 112900
`'validation'` | 16738

*   **Features**:

```json
{
    "whoTarget": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "intentYN": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sexYN": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sexReason": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "offensiveYN": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotatorGender": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotatorMinority": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sexPhrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "speakerMinorityYN": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "WorkerId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "HITId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotatorPolitics": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotatorRace": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotatorAge": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "post": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targetMinority": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targetCategory": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targetStereotype": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dataSource": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


