# medical_dialog

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/medical_dialog)
*   [Huggingface](https://huggingface.co/datasets/medical_dialog)


## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:medical_dialog/en')
```

*   **Description**:

```
The MedDialog dataset (English) contains conversations (in English) between doctors and patients.It has 0.26 million dialogues. The data is continuously growing and more dialogues will be added. The raw dialogues are from healthcaremagic.com and icliniq.com.
All copyrights of the data belong to healthcaremagic.com and icliniq.com.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 229674

*   **Features**:

```json
{
    "file_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dialogue_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dialogue_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dialogue_turns": {
        "feature": {
            "speaker": {
                "num_classes": 2,
                "names": [
                    "Patient",
                    "Doctor"
                ],
                "id": null,
                "_type": "ClassLabel"
            },
            "utterance": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:medical_dialog/zh')
```

*   **Description**:

```
The MedDialog dataset (English) contains conversations (in English) between doctors and patients.It has 0.26 million dialogues. The data is continuously growing and more dialogues will be added. The raw dialogues are from healthcaremagic.com and icliniq.com.
All copyrights of the data belong to healthcaremagic.com and icliniq.com.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1921127

*   **Features**:

```json
{
    "file_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dialogue_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "dialogue_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "dialogue_turns": {
        "feature": {
            "speaker": {
                "num_classes": 2,
                "names": [
                    "\u75c5\u4eba",
                    "\u533b\u751f"
                ],
                "id": null,
                "_type": "ClassLabel"
            },
            "utterance": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## processed.en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:medical_dialog/processed.en')
```

*   **Description**:

```
The MedDialog dataset (English) contains conversations (in English) between doctors and patients.It has 0.26 million dialogues. The data is continuously growing and more dialogues will be added. The raw dialogues are from healthcaremagic.com and icliniq.com.
All copyrights of the data belong to healthcaremagic.com and icliniq.com.
```

*   **License**: Copyright
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 61
`'train'` | 482
`'validation'` | 60

*   **Features**:

```json
{
    "description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterances": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## processed.zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:medical_dialog/processed.zh')
```

*   **Description**:

```
The MedDialog dataset (English) contains conversations (in English) between doctors and patients.It has 0.26 million dialogues. The data is continuously growing and more dialogues will be added. The raw dialogues are from healthcaremagic.com and icliniq.com.
All copyrights of the data belong to healthcaremagic.com and icliniq.com.
```

*   **License**: Copyright
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 340754
`'train'` | 2725989
`'validation'` | 340748

*   **Features**:

```json
{
    "utterances": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


