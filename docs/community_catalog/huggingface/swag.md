# swag

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/swag)
*   [Huggingface](https://huggingface.co/datasets/swag)


## regular


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swag/regular')
```

*   **Description**:

```
Given a partial description like "she opened the hood of the car,"
humans can reason about the situation and anticipate what might come
next ("then, she examined the engine"). SWAG (Situations With Adversarial Generations)
is a large-scale dataset for this task of grounded commonsense
inference, unifying natural language inference and physically grounded reasoning.

The dataset consists of 113k multiple choice questions about grounded situations
(73k training, 20k validation, 20k test).
Each question is a video caption from LSMDC or ActivityNet Captions,
with four answer choices about what might happen next in the scene.
The correct answer is the (real) video caption for the next event in the video;
the three incorrect answers are adversarially generated and human verified,
so as to fool machines but not humans. SWAG aims to be a benchmark for
evaluating grounded commonsense NLI and for learning representations.

The full data contain more information,
but the regular configuration will be more interesting for modeling
(note that the regular data are shuffled). The test set for leaderboard submission
is under the regular configuration.
```

*   **License**: Unknown
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 20005
`'train'` | 73546
`'validation'` | 20006

*   **Features**:

```json
{
    "video-id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fold-ind": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "startphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sent1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sent2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold-source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ending0": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ending1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ending2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ending3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 4,
        "names": [
            "0",
            "1",
            "2",
            "3"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## full


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swag/full')
```

*   **Description**:

```
Given a partial description like "she opened the hood of the car,"
humans can reason about the situation and anticipate what might come
next ("then, she examined the engine"). SWAG (Situations With Adversarial Generations)
is a large-scale dataset for this task of grounded commonsense
inference, unifying natural language inference and physically grounded reasoning.

The dataset consists of 113k multiple choice questions about grounded situations
(73k training, 20k validation, 20k test).
Each question is a video caption from LSMDC or ActivityNet Captions,
with four answer choices about what might happen next in the scene.
The correct answer is the (real) video caption for the next event in the video;
the three incorrect answers are adversarially generated and human verified,
so as to fool machines but not humans. SWAG aims to be a benchmark for
evaluating grounded commonsense NLI and for learning representations.

The full data contain more information,
but the regular configuration will be more interesting for modeling
(note that the regular data are shuffled). The test set for leaderboard submission
is under the regular configuration.
```

*   **License**: Unknown
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 73546
`'validation'` | 20006

*   **Features**:

```json
{
    "video-id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fold-ind": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "startphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold-ending": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor-0": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor-1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor-2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor-3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold-source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold-type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor-0-type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor-1-type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor-2-type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "distractor-3-type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sent1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sent2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


