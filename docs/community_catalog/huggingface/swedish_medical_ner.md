# swedish_medical_ner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/swedish_medical_ner)
*   [Huggingface](https://huggingface.co/datasets/swedish_medical_ner)


## wiki


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swedish_medical_ner/wiki')
```

*   **Description**:

```
SwedMedNER is a dataset for training and evaluating Named Entity Recognition systems on medical texts in Swedish.
It is derived from medical articles on the Swedish Wikipedia, Läkartidningen, and 1177 Vårdguiden.
```

*   **License**: Creative Commons Attribution-ShareAlike 4.0 International Public License (CC BY-SA 4.0)
See http://creativecommons.org/licenses/by-sa/4.0/ for the summary of the license.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 48720

*   **Features**:

```json
{
    "sid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entities": {
        "feature": {
            "start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 3,
                "names": [
                    "Disorder and Finding",
                    "Pharmaceutical Drug",
                    "Body Structure"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## lt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swedish_medical_ner/lt')
```

*   **Description**:

```
SwedMedNER is a dataset for training and evaluating Named Entity Recognition systems on medical texts in Swedish.
It is derived from medical articles on the Swedish Wikipedia, Läkartidningen, and 1177 Vårdguiden.
```

*   **License**: Creative Commons Attribution-ShareAlike 4.0 International Public License (CC BY-SA 4.0)
See http://creativecommons.org/licenses/by-sa/4.0/ for the summary of the license.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 745753

*   **Features**:

```json
{
    "sid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entities": {
        "feature": {
            "start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 3,
                "names": [
                    "Disorder and Finding",
                    "Pharmaceutical Drug",
                    "Body Structure"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## 1177


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swedish_medical_ner/1177')
```

*   **Description**:

```
SwedMedNER is a dataset for training and evaluating Named Entity Recognition systems on medical texts in Swedish.
It is derived from medical articles on the Swedish Wikipedia, Läkartidningen, and 1177 Vårdguiden.
```

*   **License**: Creative Commons Attribution-ShareAlike 4.0 International Public License (CC BY-SA 4.0)
See http://creativecommons.org/licenses/by-sa/4.0/ for the summary of the license.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 927

*   **Features**:

```json
{
    "sid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entities": {
        "feature": {
            "start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "type": {
                "num_classes": 3,
                "names": [
                    "Disorder and Finding",
                    "Pharmaceutical Drug",
                    "Body Structure"
                ],
                "names_file": null,
                "id": null,
                "_type": "ClassLabel"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


