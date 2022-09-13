# ubuntu_dialogs_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ubuntu_dialogs_corpus)
*   [Huggingface](https://huggingface.co/datasets/ubuntu_dialogs_corpus)


## train


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ubuntu_dialogs_corpus/train')
```

*   **Description**:

```
Ubuntu Dialogue Corpus, a dataset containing almost 1 million multi-turn dialogues, with a total of over 7 million utterances and 100 million words. This provides a unique resource for research into building dialogue managers based on neural language models that can make use of large amounts of unlabeled data. The dataset has both the multi-turn property of conversations in the Dialog State Tracking Challenge datasets, and the unstructured nature of interactions from microblog services such as Twitter.
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1000000

*   **Features**:

```json
{
    "Context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## dev_test


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ubuntu_dialogs_corpus/dev_test')
```

*   **Description**:

```
Ubuntu Dialogue Corpus, a dataset containing almost 1 million multi-turn dialogues, with a total of over 7 million utterances and 100 million words. This provides a unique resource for research into building dialogue managers based on neural language models that can make use of large amounts of unlabeled data. The dataset has both the multi-turn property of conversations in the Dialog State Tracking Challenge datasets, and the unstructured nature of interactions from microblog services such as Twitter.
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 18920
`'validation'` | 19560

*   **Features**:

```json
{
    "Context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Ground Truth Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_0": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_4": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_5": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_6": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_7": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Distractor_8": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


