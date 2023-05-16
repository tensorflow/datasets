# xed_en_fi

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/xed_en_fi)
*   [Huggingface](https://huggingface.co/datasets/xed_en_fi)


## en_annotated


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xed_en_fi/en_annotated')
```

*   **Description**:

```
A multilingual fine-grained emotion dataset. The dataset consists of human annotated Finnish (25k) and English sentences (30k). Plutchik’s
core emotions are used to annotate the dataset with the addition of neutral to create a multilabel multiclass
dataset. The dataset is carefully evaluated using language-specific BERT models and SVMs to
show that XED performs on par with other similar datasets and is therefore a useful tool for
sentiment analysis and emotion detection.
```

*   **License**: License: Creative Commons Attribution 4.0 International License (CC-BY)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 17528

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 9,
            "names": [
                "neutral",
                "anger",
                "anticipation",
                "disgust",
                "fear",
                "joy",
                "sadness",
                "surprise",
                "trust"
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



## en_neutral


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xed_en_fi/en_neutral')
```

*   **Description**:

```
A multilingual fine-grained emotion dataset. The dataset consists of human annotated Finnish (25k) and English sentences (30k). Plutchik’s
core emotions are used to annotate the dataset with the addition of neutral to create a multilabel multiclass
dataset. The dataset is carefully evaluated using language-specific BERT models and SVMs to
show that XED performs on par with other similar datasets and is therefore a useful tool for
sentiment analysis and emotion detection.
```

*   **License**: License: Creative Commons Attribution 4.0 International License (CC-BY)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 9675

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "num_classes": 9,
        "names": [
            "neutral",
            "anger",
            "anticipation",
            "disgust",
            "fear",
            "joy",
            "sadness",
            "surprise",
            "trust"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## fi_annotated


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xed_en_fi/fi_annotated')
```

*   **Description**:

```
A multilingual fine-grained emotion dataset. The dataset consists of human annotated Finnish (25k) and English sentences (30k). Plutchik’s
core emotions are used to annotate the dataset with the addition of neutral to create a multilabel multiclass
dataset. The dataset is carefully evaluated using language-specific BERT models and SVMs to
show that XED performs on par with other similar datasets and is therefore a useful tool for
sentiment analysis and emotion detection.
```

*   **License**: License: Creative Commons Attribution 4.0 International License (CC-BY)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 14449

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 9,
            "names": [
                "neutral",
                "anger",
                "anticipation",
                "disgust",
                "fear",
                "joy",
                "sadness",
                "surprise",
                "trust"
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



## fi_neutral


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xed_en_fi/fi_neutral')
```

*   **Description**:

```
A multilingual fine-grained emotion dataset. The dataset consists of human annotated Finnish (25k) and English sentences (30k). Plutchik’s
core emotions are used to annotate the dataset with the addition of neutral to create a multilabel multiclass
dataset. The dataset is carefully evaluated using language-specific BERT models and SVMs to
show that XED performs on par with other similar datasets and is therefore a useful tool for
sentiment analysis and emotion detection.
```

*   **License**: License: Creative Commons Attribution 4.0 International License (CC-BY)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10794

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "num_classes": 9,
        "names": [
            "neutral",
            "anger",
            "anticipation",
            "disgust",
            "fear",
            "joy",
            "sadness",
            "surprise",
            "trust"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


