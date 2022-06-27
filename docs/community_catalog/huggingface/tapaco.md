# tapaco

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tapaco)
*   [Huggingface](https://huggingface.co/datasets/tapaco)


## all_languages


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/all_languages')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1926192

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## af


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/af')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 307

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ar


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ar')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6446

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## az


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/az')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 624

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## be


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/be')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1512

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ber


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ber')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 67484

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## bg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/bg')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6324

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## bn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/bn')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1440

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## br


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/br')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2536

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ca


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ca')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 518

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## cbk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/cbk')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 262

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## cmn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/cmn')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 12549

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## cs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/cs')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6659

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## da


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/da')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 11220

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/de')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 125091

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## el


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/el')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10072

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/en')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 158053

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## eo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/eo')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 207105

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/es')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 85064

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## et


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/et')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 241

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## eu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/eu')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 573

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## fi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/fi')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 31753

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/fr')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 116733

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## gl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/gl')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 351

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## gos


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/gos')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 279

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## he


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/he')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 68350

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/hi')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1913

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/hr')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 505

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/hu')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 67964

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## hy


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/hy')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 603

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ia


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ia')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2548

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## id


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/id')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1602

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ie


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ie')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 488

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## io


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/io')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 480

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## is


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/is')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1641

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/it')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 198919

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ja


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ja')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 44267

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## jbo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/jbo')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2704

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## kab


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/kab')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 15944

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ko


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ko')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 503

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## kw


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/kw')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1328

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## la


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/la')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6889

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## lfn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/lfn')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2313

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## lt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/lt')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8042

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## mk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/mk')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 14678

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## mr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/mr')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 16413

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/nb')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1094

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nds


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/nds')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2633

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/nl')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 23561

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## orv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/orv')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 471

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ota


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ota')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 486

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## pes


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/pes')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4285

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/pl')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 22391

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/pt')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 78430

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## rn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/rn')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 648

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ro')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2092

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ru')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 251263

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## sl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/sl')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 706

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/sr')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8175

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## sv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/sv')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7005

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/tk')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1165

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/tl')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1017

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tlh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/tlh')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2804

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## toki


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/toki')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3738

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/tr')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 142088

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/tt')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2398

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ug


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ug')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1183

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## uk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/uk')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 54431

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ur


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/ur')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 252

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## vi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/vi')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 962

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## vo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/vo')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 328

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## war


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/war')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 327

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wuu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/wuu')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 408

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## yue


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tapaco/yue')
```

*   **Description**:

```
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. Tatoeba is a
crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences and translations for particular
linguistic constructions and words. The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links
between sentences “meaning the same thing”. This graph is then traversed to extract sets of paraphrases. Several language-independent
filters and pruning steps are applied to remove uninteresting sentences. A manual evaluation performed on three languages shows
that between half and three quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, or
near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million sentences, with 200 – 250 000
sentences per language. It covers a range of languages for which, to our knowledge, no other paraphrase dataset exists.
```

*   **License**: Creative Commons Attribution 2.0 Generic
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 561

*   **Features**:

```json
{
    "paraphrase_set_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lists": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


