# generics_kb

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/generics_kb)
*   [Huggingface](https://huggingface.co/datasets/generics_kb)


## generics_kb_best


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:generics_kb/generics_kb_best')
```

*   **Description**:

```
The GenericsKB contains 3.4M+ generic sentences about the world, i.e., sentences expressing general truths such as "Dogs bark," and "Trees remove carbon dioxide from the atmosphere." Generics are potentially useful as a knowledge source for AI systems requiring general world knowledge. The GenericsKB is the first large-scale resource containing naturally occurring generic sentences (as opposed to extracted or crowdsourced triples), and is rich in high-quality, general, semantically complete statements. Generics were primarily extracted from three large text sources, namely the Waterloo Corpus, selected parts of Simple Wikipedia, and the ARC Corpus. A filtered, high-quality subset is also available in GenericsKB-Best, containing 1,020,868 sentences. We recommend you start with GenericsKB-Best.
```

*   **License**: cc-by-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1020868

*   **Features**:

```json
{
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "term": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "quantifier_frequency": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "quantifier_number": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "generic_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    }
}
```



## generics_kb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:generics_kb/generics_kb')
```

*   **Description**:

```
The GenericsKB contains 3.4M+ generic sentences about the world, i.e., sentences expressing general truths such as "Dogs bark," and "Trees remove carbon dioxide from the atmosphere." Generics are potentially useful as a knowledge source for AI systems requiring general world knowledge. The GenericsKB is the first large-scale resource containing naturally occurring generic sentences (as opposed to extracted or crowdsourced triples), and is rich in high-quality, general, semantically complete statements. Generics were primarily extracted from three large text sources, namely the Waterloo Corpus, selected parts of Simple Wikipedia, and the ARC Corpus. A filtered, high-quality subset is also available in GenericsKB-Best, containing 1,020,868 sentences. We recommend you start with GenericsKB-Best.
```

*   **License**: cc-by-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3433000

*   **Features**:

```json
{
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "term": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "quantifier_frequency": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "quantifier_number": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "generic_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    }
}
```



## generics_kb_simplewiki


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:generics_kb/generics_kb_simplewiki')
```

*   **Description**:

```
The GenericsKB contains 3.4M+ generic sentences about the world, i.e., sentences expressing general truths such as "Dogs bark," and "Trees remove carbon dioxide from the atmosphere." Generics are potentially useful as a knowledge source for AI systems requiring general world knowledge. The GenericsKB is the first large-scale resource containing naturally occurring generic sentences (as opposed to extracted or crowdsourced triples), and is rich in high-quality, general, semantically complete statements. Generics were primarily extracted from three large text sources, namely the Waterloo Corpus, selected parts of Simple Wikipedia, and the ARC Corpus. A filtered, high-quality subset is also available in GenericsKB-Best, containing 1,020,868 sentences. We recommend you start with GenericsKB-Best.
```

*   **License**: cc-by-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 12765

*   **Features**:

```json
{
    "source_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentences_before": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "sentences_after": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "concept_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "quantifiers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bert_score": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    },
    "headings": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "categories": {
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



## generics_kb_waterloo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:generics_kb/generics_kb_waterloo')
```

*   **Description**:

```
The GenericsKB contains 3.4M+ generic sentences about the world, i.e., sentences expressing general truths such as "Dogs bark," and "Trees remove carbon dioxide from the atmosphere." Generics are potentially useful as a knowledge source for AI systems requiring general world knowledge. The GenericsKB is the first large-scale resource containing naturally occurring generic sentences (as opposed to extracted or crowdsourced triples), and is rich in high-quality, general, semantically complete statements. Generics were primarily extracted from three large text sources, namely the Waterloo Corpus, selected parts of Simple Wikipedia, and the ARC Corpus. A filtered, high-quality subset is also available in GenericsKB-Best, containing 1,020,868 sentences. We recommend you start with GenericsKB-Best.
```

*   **License**: cc-by-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3666725

*   **Features**:

```json
{
    "source_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentences_before": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "sentences_after": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "concept_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "quantifiers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bert_score": {
        "dtype": "float64",
        "id": null,
        "_type": "Value"
    }
}
```


