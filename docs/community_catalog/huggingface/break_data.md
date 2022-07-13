# break_data

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/break_data)
*   [Huggingface](https://huggingface.co/datasets/break_data)


## QDMR-high-level


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:break_data/QDMR-high-level')
```

*   **Description**:

```
Break is a human annotated dataset of natural language questions and their Question Decomposition Meaning Representations
(QDMRs). Break consists of 83,978 examples sampled from 10 question answering datasets over text, images and databases. 
This repository contains the Break dataset along with information on the exact data format.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3195
`'train'` | 17503
`'validation'` | 3130

*   **Features**:

```json
{
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "decomposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "operators": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## QDMR-high-level-lexicon


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:break_data/QDMR-high-level-lexicon')
```

*   **Description**:

```
Break is a human annotated dataset of natural language questions and their Question Decomposition Meaning Representations
(QDMRs). Break consists of 83,978 examples sampled from 10 question answering datasets over text, images and databases. 
This repository contains the Break dataset along with information on the exact data format.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3195
`'train'` | 17503
`'validation'` | 3130

*   **Features**:

```json
{
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "allowed_tokens": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## QDMR


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:break_data/QDMR')
```

*   **Description**:

```
Break is a human annotated dataset of natural language questions and their Question Decomposition Meaning Representations
(QDMRs). Break consists of 83,978 examples sampled from 10 question answering datasets over text, images and databases. 
This repository contains the Break dataset along with information on the exact data format.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8069
`'train'` | 44321
`'validation'` | 7760

*   **Features**:

```json
{
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "decomposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "operators": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## QDMR-lexicon


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:break_data/QDMR-lexicon')
```

*   **Description**:

```
Break is a human annotated dataset of natural language questions and their Question Decomposition Meaning Representations
(QDMRs). Break consists of 83,978 examples sampled from 10 question answering datasets over text, images and databases. 
This repository contains the Break dataset along with information on the exact data format.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8069
`'train'` | 44321
`'validation'` | 7760

*   **Features**:

```json
{
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "allowed_tokens": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## logical-forms


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:break_data/logical-forms')
```

*   **Description**:

```
Break is a human annotated dataset of natural language questions and their Question Decomposition Meaning Representations
(QDMRs). Break consists of 83,978 examples sampled from 10 question answering datasets over text, images and databases. 
This repository contains the Break dataset along with information on the exact data format.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8006
`'train'` | 44098
`'validation'` | 7719

*   **Features**:

```json
{
    "question_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "decomposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "operators": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "program": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


