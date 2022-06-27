# xor_tydi_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/xor_tydi_qa)
*   [Huggingface](https://huggingface.co/datasets/xor_tydi_qa)


## xor-retrieve


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xor_tydi_qa/xor-retrieve')
```

*   **Description**:

```
XOR-TyDi QA brings together for the first time information-seeking questions,
    open-retrieval QA, and multilingual QA to create a multilingual open-retrieval
    QA dataset that enables cross-lingual answer retrieval. It consists of questions
    written by information-seeking native speakers in 7 typologically diverse languages
    and answer annotations that are retrieved from multilingual document collections.
    There are three sub-tasks: XOR-Retrieve, XOR-EnglishSpan, and XOR-Full.

XOR-Retrieve is a cross-lingual retrieval task where a question is written in the target
language (e.g., Japanese) and a system is required to retrieve English document that answers the question.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2499
`'train'` | 15250
`'validation'` | 2110

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "num_classes": 7,
        "names": [
            "ar",
            "bn",
            "fi",
            "ja",
            "ko",
            "ru",
            "te"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "answers": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## xor-full


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xor_tydi_qa/xor-full')
```

*   **Description**:

```
XOR-TyDi QA brings together for the first time information-seeking questions,
    open-retrieval QA, and multilingual QA to create a multilingual open-retrieval
    QA dataset that enables cross-lingual answer retrieval. It consists of questions
    written by information-seeking native speakers in 7 typologically diverse languages
    and answer annotations that are retrieved from multilingual document collections.
    There are three sub-tasks: XOR-Retrieve, XOR-EnglishSpan, and XOR-Full.

XOR-Full is a cross-lingual retrieval task where a question is written in the target
language (e.g., Japanese) and a system is required to output a short answer in the target language.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8176
`'train'` | 61360
`'validation'` | 3473

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "num_classes": 7,
        "names": [
            "ar",
            "bn",
            "fi",
            "ja",
            "ko",
            "ru",
            "te"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "answers": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


