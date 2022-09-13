# paws-x

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/paws-x)
*   [Huggingface](https://huggingface.co/datasets/paws-x)


## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws-x/en')
```

*   **Description**:

```
PAWS-X, a multilingual version of PAWS (Paraphrase Adversaries from Word Scrambling) for six languages.

This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine
translated training pairs in six typologically distinct languages: French, Spanish, German,
Chinese, Japanese, and Korean. English language is available by default. All translated
pairs are sourced from examples in PAWS-Wiki.

For further details, see the accompanying paper: PAWS-X: A Cross-lingual Adversarial Dataset
for Paraphrase Identification (https://arxiv.org/abs/1908.11828)

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 49401
`'validation'` | 2000

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



## de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws-x/de')
```

*   **Description**:

```
PAWS-X, a multilingual version of PAWS (Paraphrase Adversaries from Word Scrambling) for six languages.

This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine
translated training pairs in six typologically distinct languages: French, Spanish, German,
Chinese, Japanese, and Korean. English language is available by default. All translated
pairs are sourced from examples in PAWS-Wiki.

For further details, see the accompanying paper: PAWS-X: A Cross-lingual Adversarial Dataset
for Paraphrase Identification (https://arxiv.org/abs/1908.11828)

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 49401
`'validation'` | 2000

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



## es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws-x/es')
```

*   **Description**:

```
PAWS-X, a multilingual version of PAWS (Paraphrase Adversaries from Word Scrambling) for six languages.

This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine
translated training pairs in six typologically distinct languages: French, Spanish, German,
Chinese, Japanese, and Korean. English language is available by default. All translated
pairs are sourced from examples in PAWS-Wiki.

For further details, see the accompanying paper: PAWS-X: A Cross-lingual Adversarial Dataset
for Paraphrase Identification (https://arxiv.org/abs/1908.11828)

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 49401
`'validation'` | 2000

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



## fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws-x/fr')
```

*   **Description**:

```
PAWS-X, a multilingual version of PAWS (Paraphrase Adversaries from Word Scrambling) for six languages.

This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine
translated training pairs in six typologically distinct languages: French, Spanish, German,
Chinese, Japanese, and Korean. English language is available by default. All translated
pairs are sourced from examples in PAWS-Wiki.

For further details, see the accompanying paper: PAWS-X: A Cross-lingual Adversarial Dataset
for Paraphrase Identification (https://arxiv.org/abs/1908.11828)

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 49401
`'validation'` | 2000

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



## ja


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws-x/ja')
```

*   **Description**:

```
PAWS-X, a multilingual version of PAWS (Paraphrase Adversaries from Word Scrambling) for six languages.

This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine
translated training pairs in six typologically distinct languages: French, Spanish, German,
Chinese, Japanese, and Korean. English language is available by default. All translated
pairs are sourced from examples in PAWS-Wiki.

For further details, see the accompanying paper: PAWS-X: A Cross-lingual Adversarial Dataset
for Paraphrase Identification (https://arxiv.org/abs/1908.11828)

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 49401
`'validation'` | 2000

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



## ko


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws-x/ko')
```

*   **Description**:

```
PAWS-X, a multilingual version of PAWS (Paraphrase Adversaries from Word Scrambling) for six languages.

This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine
translated training pairs in six typologically distinct languages: French, Spanish, German,
Chinese, Japanese, and Korean. English language is available by default. All translated
pairs are sourced from examples in PAWS-Wiki.

For further details, see the accompanying paper: PAWS-X: A Cross-lingual Adversarial Dataset
for Paraphrase Identification (https://arxiv.org/abs/1908.11828)

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 49401
`'validation'` | 2000

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



## zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:paws-x/zh')
```

*   **Description**:

```
PAWS-X, a multilingual version of PAWS (Paraphrase Adversaries from Word Scrambling) for six languages.

This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine
translated training pairs in six typologically distinct languages: French, Spanish, German,
Chinese, Japanese, and Korean. English language is available by default. All translated
pairs are sourced from examples in PAWS-Wiki.

For further details, see the accompanying paper: PAWS-X: A Cross-lingual Adversarial Dataset
for Paraphrase Identification (https://arxiv.org/abs/1908.11828)

NOTE: There might be some missing or wrong labels in the dataset and we have replaced them with -1.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated. The dataset is provided "AS IS" without any warranty, express or implied. Google disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 49401
`'validation'` | 2000

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


