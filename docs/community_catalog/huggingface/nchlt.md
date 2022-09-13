# nchlt

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/nchlt)
*   [Huggingface](https://huggingface.co/datasets/nchlt)


## af


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/af')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8961

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## nr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/nr')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 9334

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## xh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/xh')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6283

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## zu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/zu')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10955

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## nso-sepedi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/nso-sepedi')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7116

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## nso-sesotho


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/nso-sesotho')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 9471

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## tn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/tn')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7943

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ss


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/ss')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10797

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ve


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/ve')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8477

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ts


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nchlt/ts')
```

*   **Description**:

```
The development of linguistic resources for use in natural language processingis of utmost importance for the continued growth of research anddevelopment in the field, especially for resource-scarce languages. In this paper we describe the process and challenges of simultaneouslydevelopingmultiple linguistic resources for ten of the official languages of South Africa. The project focussed on establishing a set of foundational resources that can foster further development of both resources and technologies for the NLP industry in South Africa. The development efforts during the project included creating monolingual unannotated corpora, of which a subset of the corpora for each language was annotated on token, orthographic, morphological and morphosyntactic layers. The annotated subsetsincludes both development and test setsand were used in the creation of five core-technologies, viz. atokeniser, sentenciser,lemmatiser, part of speech tagger and morphological decomposer for each language. We report on the quality of these tools for each language and provide some more context of the importance of the resources within the South African context.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8477

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 9,
            "names": [
                "OUT",
                "B-PERS",
                "I-PERS",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-MISC",
                "I-MISC"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


