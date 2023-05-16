# swiss_judgment_prediction

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/swiss_judgment_prediction)
*   [Huggingface](https://huggingface.co/datasets/swiss_judgment_prediction)


## de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swiss_judgment_prediction/de')
```

*   **Description**:

```
Swiss-Judgment-Prediction is a multilingual, diachronic dataset of 85K Swiss Federal Supreme Court (FSCS) cases annotated with
the respective binarized judgment outcome (approval/dismissal), posing a challenging text classification task.  
We also provide additional metadata, i.e., the publication year, the legal area and the canton of origin per case,  
to promote robustness and fairness studies on the critical area of legal NLP.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9725
`'train'` | 35458
`'validation'` | 4705

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "dismissal",
            "approval"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "region": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "canton": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "legal area": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swiss_judgment_prediction/fr')
```

*   **Description**:

```
Swiss-Judgment-Prediction is a multilingual, diachronic dataset of 85K Swiss Federal Supreme Court (FSCS) cases annotated with
the respective binarized judgment outcome (approval/dismissal), posing a challenging text classification task.  
We also provide additional metadata, i.e., the publication year, the legal area and the canton of origin per case,  
to promote robustness and fairness studies on the critical area of legal NLP.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6820
`'train'` | 21179
`'validation'` | 3095

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "dismissal",
            "approval"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "region": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "canton": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "legal area": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swiss_judgment_prediction/it')
```

*   **Description**:

```
Swiss-Judgment-Prediction is a multilingual, diachronic dataset of 85K Swiss Federal Supreme Court (FSCS) cases annotated with
the respective binarized judgment outcome (approval/dismissal), posing a challenging text classification task.  
We also provide additional metadata, i.e., the publication year, the legal area and the canton of origin per case,  
to promote robustness and fairness studies on the critical area of legal NLP.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 812
`'train'` | 3072
`'validation'` | 408

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "dismissal",
            "approval"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "region": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "canton": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "legal area": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## all_languages


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swiss_judgment_prediction/all_languages')
```

*   **Description**:

```
Swiss-Judgment-Prediction is a multilingual, diachronic dataset of 85K Swiss Federal Supreme Court (FSCS) cases annotated with
the respective binarized judgment outcome (approval/dismissal), posing a challenging text classification task.  
We also provide additional metadata, i.e., the publication year, the legal area and the canton of origin per case,  
to promote robustness and fairness studies on the critical area of legal NLP.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 17357
`'train'` | 59709
`'validation'` | 8208

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "dismissal",
            "approval"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "region": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "canton": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "legal area": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


