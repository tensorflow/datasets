# paws

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/paws)
*   [Huggingface](https://huggingface.co/datasets/paws)


## labeled_final


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws/labeled_final')
```

*   **Description**:

```
PAWS: Paraphrase Adversaries from Word Scrambling

This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that feature
the importance of modeling structure, context, and word order information for the problem
of paraphrase identification. The dataset has two subsets, one based on Wikipedia and the
other one based on the Quora Question Pairs (QQP) dataset.

For further details, see the accompanying paper: PAWS: Paraphrase Adversaries from Word Scrambling
(https://arxiv.org/abs/1904.01130)

PAWS-QQP is not available due to license of QQP. It must be reconstructed by downloading the original
data and then running our scripts to produce the data and attach the labels.

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8000
`'train'` | 49401
`'validation'` | 8000

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
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
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## labeled_swap


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws/labeled_swap')
```

*   **Description**:

```
PAWS: Paraphrase Adversaries from Word Scrambling

This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that feature
the importance of modeling structure, context, and word order information for the problem
of paraphrase identification. The dataset has two subsets, one based on Wikipedia and the
other one based on the Quora Question Pairs (QQP) dataset.

For further details, see the accompanying paper: PAWS: Paraphrase Adversaries from Word Scrambling
(https://arxiv.org/abs/1904.01130)

PAWS-QQP is not available due to license of QQP. It must be reconstructed by downloading the original
data and then running our scripts to produce the data and attach the labels.

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 30397

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
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
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## unlabeled_final


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws/unlabeled_final')
```

*   **Description**:

```
PAWS: Paraphrase Adversaries from Word Scrambling

This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that feature
the importance of modeling structure, context, and word order information for the problem
of paraphrase identification. The dataset has two subsets, one based on Wikipedia and the
other one based on the Quora Question Pairs (QQP) dataset.

For further details, see the accompanying paper: PAWS: Paraphrase Adversaries from Word Scrambling
(https://arxiv.org/abs/1904.01130)

PAWS-QQP is not available due to license of QQP. It must be reconstructed by downloading the original
data and then running our scripts to produce the data and attach the labels.

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 645652
`'validation'` | 10000

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
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
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


