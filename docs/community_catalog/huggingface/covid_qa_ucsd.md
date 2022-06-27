# covid_qa_ucsd

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/covid_qa_ucsd)
*   [Huggingface](https://huggingface.co/datasets/covid_qa_ucsd)


## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covid_qa_ucsd/en')
```

*   **Description**:

```
COVID-Dialogue-Dataset is amedical dialogue dataset about COVID-19 and other types of pneumonia.
Patients who are concerned that they may be infected by COVID-19 or other pneumonia consult doctors and doctors provide advice.
There are 603 consultations in English and 1393 consultations in Chinese.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 572

*   **Features**:

```json
{
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
                "names_file": null,
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
ds = tfds.load('huggingface:covid_qa_ucsd/zh')
```

*   **Description**:

```
COVID-Dialogue-Dataset is amedical dialogue dataset about COVID-19 and other types of pneumonia.
Patients who are concerned that they may be infected by COVID-19 or other pneumonia consult doctors and doctors provide advice.
There are 603 consultations in English and 1393 consultations in Chinese.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1088

*   **Features**:

```json
{
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
                "names_file": null,
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


