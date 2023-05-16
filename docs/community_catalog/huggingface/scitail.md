# scitail

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/scitail)
*   [Huggingface](https://huggingface.co/datasets/scitail)


## snli_format


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scitail/snli_format')
```

*   **Description**:

```
The SciTail dataset is an entailment dataset created from multiple-choice science exams and web sentences. Each question 
and the correct answer choice are converted into an assertive statement to form the hypothesis. We use information 
retrieval to obtain relevant text from a large text corpus of web sentences, and use these sentences as a premise P. We 
crowdsource the annotation of such premise-hypothesis pair as supports (entails) or not (neutral), in order to create 
the SciTail dataset. The dataset contains 27,026 examples with 10,101 examples with entails label and 16,925 examples 
with neutral label
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2126
`'train'` | 23596
`'validation'` | 1304

*   **Features**:

```json
{
    "sentence1_binary_parse": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence1_parse": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2_parse": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "annotator_labels": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "gold_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tsv_format


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scitail/tsv_format')
```

*   **Description**:

```
The SciTail dataset is an entailment dataset created from multiple-choice science exams and web sentences. Each question 
and the correct answer choice are converted into an assertive statement to form the hypothesis. We use information 
retrieval to obtain relevant text from a large text corpus of web sentences, and use these sentences as a premise P. We 
crowdsource the annotation of such premise-hypothesis pair as supports (entails) or not (neutral), in order to create 
the SciTail dataset. The dataset contains 27,026 examples with 10,101 examples with entails label and 16,925 examples 
with neutral label
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2126
`'train'` | 23097
`'validation'` | 1304

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
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## dgem_format


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scitail/dgem_format')
```

*   **Description**:

```
The SciTail dataset is an entailment dataset created from multiple-choice science exams and web sentences. Each question 
and the correct answer choice are converted into an assertive statement to form the hypothesis. We use information 
retrieval to obtain relevant text from a large text corpus of web sentences, and use these sentences as a premise P. We 
crowdsource the annotation of such premise-hypothesis pair as supports (entails) or not (neutral), in order to create 
the SciTail dataset. The dataset contains 27,026 examples with 10,101 examples with entails label and 16,925 examples 
with neutral label
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2126
`'train'` | 23088
`'validation'` | 1304

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
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis_graph_structure": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## predictor_format


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scitail/predictor_format')
```

*   **Description**:

```
The SciTail dataset is an entailment dataset created from multiple-choice science exams and web sentences. Each question 
and the correct answer choice are converted into an assertive statement to form the hypothesis. We use information 
retrieval to obtain relevant text from a large text corpus of web sentences, and use these sentences as a premise P. We 
crowdsource the annotation of such premise-hypothesis pair as supports (entails) or not (neutral), in order to create 
the SciTail dataset. The dataset contains 27,026 examples with 10,101 examples with entails label and 16,925 examples 
with neutral label
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2126
`'train'` | 23587
`'validation'` | 1304

*   **Features**:

```json
{
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2_structure": {
        "dtype": "string",
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
    "gold_label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


