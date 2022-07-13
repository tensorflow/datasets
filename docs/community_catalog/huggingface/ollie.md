# ollie

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ollie)
*   [Huggingface](https://huggingface.co/datasets/ollie)


## ollie_lemmagrep


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ollie/ollie_lemmagrep')
```

*   **Description**:

```
The Ollie dataset includes two configs for the data
used to train the Ollie informatation extraction algorithm, for 18M
sentences and 3M sentences respectively. 

This data is for academic use only. From the authors:

Ollie is a program that automatically identifies and extracts binary
relationships from English sentences. Ollie is designed for Web-scale
information extraction, where target relations are not specified in
advance.

Ollie is our second-generation information extraction system . Whereas
ReVerb operates on flat sequences of tokens, Ollie works with the
tree-like (graph with only small cycles) representation using
Stanford's compression of the dependencies. This allows Ollie to
capture expression that ReVerb misses, such as long-range relations.

Ollie also captures context that modifies a binary relation. Presently
Ollie handles attribution (He said/she believes) and enabling
conditions (if X then).

More information is available at the Ollie homepage:
https://knowitall.github.io/ollie/
```

*   **License**: The University of Washington acamdemic license:
https://raw.githubusercontent.com/knowitall/ollie/master/LICENSE

*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 18674630

*   **Features**:

```json
{
    "arg1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "arg2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rel": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "search_query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "words": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pos": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "chunk": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_cnt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ollie_patterned


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ollie/ollie_patterned')
```

*   **Description**:

```
The Ollie dataset includes two configs for the data
used to train the Ollie informatation extraction algorithm, for 18M
sentences and 3M sentences respectively. 

This data is for academic use only. From the authors:

Ollie is a program that automatically identifies and extracts binary
relationships from English sentences. Ollie is designed for Web-scale
information extraction, where target relations are not specified in
advance.

Ollie is our second-generation information extraction system . Whereas
ReVerb operates on flat sequences of tokens, Ollie works with the
tree-like (graph with only small cycles) representation using
Stanford's compression of the dependencies. This allows Ollie to
capture expression that ReVerb misses, such as long-range relations.

Ollie also captures context that modifies a binary relation. Presently
Ollie handles attribution (He said/she believes) and enabling
conditions (if X then).

More information is available at the Ollie homepage:
https://knowitall.github.io/ollie/
```

*   **License**: The University of Washington acamdemic license:
https://raw.githubusercontent.com/knowitall/ollie/master/LICENSE

*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3048961

*   **Features**:

```json
{
    "rel": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "arg1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "arg2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "slot0": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "search_query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pattern": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "parse": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


