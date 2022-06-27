# cedr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cedr)
*   [Huggingface](https://huggingface.co/datasets/cedr)


## main


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cedr/main')
```

*   **Description**:

```
This new dataset is designed to solve emotion recognition task for text data in Russian. The Corpus for Emotions Detecting in
Russian-language text sentences of different social sources (CEDR) contains 9410 sentences in Russian labeled for 5 emotion
categories. The data collected from different sources: posts of the LiveJournal social network, texts of the online news
agency Lenta.ru, and Twitter microblog posts. There are two variants of the corpus: main and enriched. The enriched variant
is include tokenization and lemmatization. Dataset with predefined train/test splits.
```

*   **License**: http://www.apache.org/licenses/LICENSE-2.0
*   **Version**: 0.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1882
`'train'` | 7528

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 5,
            "names": [
                "joy",
                "sadness",
                "surprise",
                "fear",
                "anger"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## enriched


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cedr/enriched')
```

*   **Description**:

```
This new dataset is designed to solve emotion recognition task for text data in Russian. The Corpus for Emotions Detecting in
Russian-language text sentences of different social sources (CEDR) contains 9410 sentences in Russian labeled for 5 emotion
categories. The data collected from different sources: posts of the LiveJournal social network, texts of the online news
agency Lenta.ru, and Twitter microblog posts. There are two variants of the corpus: main and enriched. The enriched variant
is include tokenization and lemmatization. Dataset with predefined train/test splits.
```

*   **License**: http://www.apache.org/licenses/LICENSE-2.0
*   **Version**: 0.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1882
`'train'` | 7528

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 5,
            "names": [
                "joy",
                "sadness",
                "surprise",
                "fear",
                "anger"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentences": [
        [
            {
                "forma": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "lemma": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            }
        ]
    ]
}
```


