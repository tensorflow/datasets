# tweet_eval

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tweet_eval)
*   [Huggingface](https://huggingface.co/datasets/tweet_eval)


## emoji


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/emoji')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 50000
`'train'` | 45000
`'validation'` | 5000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 20,
        "names": [
            "\u2764",
            "\ud83d\ude0d",
            "\ud83d\ude02",
            "\ud83d\udc95",
            "\ud83d\udd25",
            "\ud83d\ude0a",
            "\ud83d\ude0e",
            "\u2728",
            "\ud83d\udc99",
            "\ud83d\ude18",
            "\ud83d\udcf7",
            "\ud83c\uddfa\ud83c\uddf8",
            "\u2600",
            "\ud83d\udc9c",
            "\ud83d\ude09",
            "\ud83d\udcaf",
            "\ud83d\ude01",
            "\ud83c\udf84",
            "\ud83d\udcf8",
            "\ud83d\ude1c"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## emotion


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/emotion')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1421
`'train'` | 3257
`'validation'` | 374

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 4,
        "names": [
            "anger",
            "joy",
            "optimism",
            "sadness"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## hate


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/hate')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2970
`'train'` | 9000
`'validation'` | 1000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "non-hate",
            "hate"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## irony


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/irony')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 784
`'train'` | 2862
`'validation'` | 955

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "non_irony",
            "irony"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## offensive


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/offensive')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 860
`'train'` | 11916
`'validation'` | 1324

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "non-offensive",
            "offensive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## sentiment


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/sentiment')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 12284
`'train'` | 45615
`'validation'` | 2000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## stance_abortion


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/stance_abortion')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 280
`'train'` | 587
`'validation'` | 66

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "none",
            "against",
            "favor"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## stance_atheism


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/stance_atheism')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 220
`'train'` | 461
`'validation'` | 52

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "none",
            "against",
            "favor"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## stance_climate


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/stance_climate')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 169
`'train'` | 355
`'validation'` | 40

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "none",
            "against",
            "favor"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## stance_feminist


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/stance_feminist')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 285
`'train'` | 597
`'validation'` | 67

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "none",
            "against",
            "favor"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## stance_hillary


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tweet_eval/stance_hillary')
```

*   **Description**:

```
TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 295
`'train'` | 620
`'validation'` | 69

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "none",
            "against",
            "favor"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


