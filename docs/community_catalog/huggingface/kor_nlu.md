# kor_nlu

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kor_nlu)
*   [Huggingface](https://huggingface.co/datasets/kor_nlu)


## nli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_nlu/nli')
```

*   **Description**:

```
The dataset contains data for bechmarking korean models on NLI and STS
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4954
`'train'` | 550146
`'validation'` | 1570

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## sts


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_nlu/sts')
```

*   **Description**:

```
The dataset contains data for bechmarking korean models on NLI and STS
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1379
`'train'` | 5703
`'validation'` | 1471

*   **Features**:

```json
{
    "genre": {
        "num_classes": 4,
        "names": [
            "main-news",
            "main-captions",
            "main-forum",
            "main-forums"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "filename": {
        "num_classes": 9,
        "names": [
            "images",
            "MSRpar",
            "MSRvid",
            "headlines",
            "deft-forum",
            "deft-news",
            "track5.en-en",
            "answers-forums",
            "answer-answer"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "year": {
        "num_classes": 7,
        "names": [
            "2017",
            "2016",
            "2013",
            "2012train",
            "2014",
            "2015",
            "2012test"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


