# wikicorpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wikicorpus)
*   [Huggingface](https://huggingface.co/datasets/wikicorpus)


## raw_ca


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikicorpus/raw_ca')
```

*   **Description**:

```
The Wikicorpus is a trilingual corpus (Catalan, Spanish, English) that contains large portions of the Wikipedia (based on a 2006 dump) and has been automatically enriched with linguistic information. 
In its present version, it contains over 750 million words.
```

*   **License**: GNU Free Documentation License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 143883

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## raw_es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikicorpus/raw_es')
```

*   **Description**:

```
The Wikicorpus is a trilingual corpus (Catalan, Spanish, English) that contains large portions of the Wikipedia (based on a 2006 dump) and has been automatically enriched with linguistic information. 
In its present version, it contains over 750 million words.
```

*   **License**: GNU Free Documentation License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 259409

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## raw_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikicorpus/raw_en')
```

*   **Description**:

```
The Wikicorpus is a trilingual corpus (Catalan, Spanish, English) that contains large portions of the Wikipedia (based on a 2006 dump) and has been automatically enriched with linguistic information. 
In its present version, it contains over 750 million words.
```

*   **License**: GNU Free Documentation License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1359146

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tagged_ca


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikicorpus/tagged_ca')
```

*   **Description**:

```
The Wikicorpus is a trilingual corpus (Catalan, Spanish, English) that contains large portions of the Wikipedia (based on a 2006 dump) and has been automatically enriched with linguistic information. 
In its present version, it contains over 750 million words.
```

*   **License**: GNU Free Documentation License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2016221

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "lemmas": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pos_tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "wordnet_senses": {
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



## tagged_es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikicorpus/tagged_es')
```

*   **Description**:

```
The Wikicorpus is a trilingual corpus (Catalan, Spanish, English) that contains large portions of the Wikipedia (based on a 2006 dump) and has been automatically enriched with linguistic information. 
In its present version, it contains over 750 million words.
```

*   **License**: GNU Free Documentation License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5039367

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "lemmas": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pos_tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "wordnet_senses": {
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



## tagged_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wikicorpus/tagged_en')
```

*   **Description**:

```
The Wikicorpus is a trilingual corpus (Catalan, Spanish, English) that contains large portions of the Wikipedia (based on a 2006 dump) and has been automatically enriched with linguistic information. 
In its present version, it contains over 750 million words.
```

*   **License**: GNU Free Documentation License
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 26350272

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "lemmas": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "pos_tags": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "wordnet_senses": {
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


