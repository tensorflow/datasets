# multi_re_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multi_re_qa)
*   [Huggingface](https://huggingface.co/datasets/multi_re_qa)


## SearchQA


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/SearchQA')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3163801
`'validation'` | 454836

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## TriviaQA


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/TriviaQA')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1893674
`'validation'` | 238339

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## HotpotQA


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/HotpotQA')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 508879
`'validation'` | 52191

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## SQuAD


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/SQuAD')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 95659
`'validation'` | 10642

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## NaturalQuestions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/NaturalQuestions')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 448355
`'validation'` | 22118

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## BioASQ


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/BioASQ')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 14158

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## RelationExtraction


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/RelationExtraction')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3301

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## TextbookQA


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/TextbookQA')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 71147

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## DuoRC


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_re_qa/DuoRC')
```

*   **Description**:

```
MultiReQA contains the sentence boundary annotation from eight publicly available QA datasets including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, BioASQ, RelationExtraction, and TextbookQA. Five of these datasets, including SearchQA, TriviaQA, HotpotQA, NaturalQuestions, SQuAD, contain both training and test data, and three, including BioASQ, RelationExtraction, TextbookQA, contain only the test data
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5525

*   **Features**:

```json
{
    "candidate_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "response_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "response_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


