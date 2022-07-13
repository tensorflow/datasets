# snips_built_in_intents

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/snips_built_in_intents)
*   [Huggingface](https://huggingface.co/datasets/snips_built_in_intents)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:snips_built_in_intents')
```

*   **Description**:

```
Snips' built in intents dataset was initially used to compare different voice assistants and released as a public dataset hosted at
https://github.com/sonos/nlu-benchmark 2016-12-built-in-intents. The dataset contains 328 utterances over 10 intent classes. The
related paper mentioned on the github page is https://arxiv.org/abs/1805.10190 and a related Medium post is
https://medium.com/snips-ai/benchmarking-natural-language-understanding-systems-d35be6ce568d .
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 328

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 10,
        "names": [
            "ComparePlaces",
            "RequestRide",
            "GetWeather",
            "SearchPlace",
            "GetPlaceDetails",
            "ShareCurrentLocation",
            "GetTrafficInformation",
            "BookRestaurant",
            "GetDirections",
            "ShareETA"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


