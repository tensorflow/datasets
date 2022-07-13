# euronews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/euronews)
*   [Huggingface](https://huggingface.co/datasets/euronews)


## fr-bnf


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:euronews/fr-bnf')
```

*   **Description**:

```
The corpora comprise of files per data provider that are encoded in the IOB format (Ramshaw & Marcus, 1995). The IOB format is a simple text chunking format that divides texts into single tokens per line, and, separated by a whitespace, tags to mark named entities. The most commonly used categories for tags are PER (person), LOC (location) and ORG (organization). To mark named entities that span multiple tokens, the tags have a prefix of either B- (beginning of named entity) or I- (inside of named entity). O (outside of named entity) tags are used to mark tokens that are not a named entity.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
            "num_classes": 7,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC"
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



## nl-kb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:euronews/nl-kb')
```

*   **Description**:

```
The corpora comprise of files per data provider that are encoded in the IOB format (Ramshaw & Marcus, 1995). The IOB format is a simple text chunking format that divides texts into single tokens per line, and, separated by a whitespace, tags to mark named entities. The most commonly used categories for tags are PER (person), LOC (location) and ORG (organization). To mark named entities that span multiple tokens, the tags have a prefix of either B- (beginning of named entity) or I- (inside of named entity). O (outside of named entity) tags are used to mark tokens that are not a named entity.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
            "num_classes": 7,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC"
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



## de-sbb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:euronews/de-sbb')
```

*   **Description**:

```
The corpora comprise of files per data provider that are encoded in the IOB format (Ramshaw & Marcus, 1995). The IOB format is a simple text chunking format that divides texts into single tokens per line, and, separated by a whitespace, tags to mark named entities. The most commonly used categories for tags are PER (person), LOC (location) and ORG (organization). To mark named entities that span multiple tokens, the tags have a prefix of either B- (beginning of named entity) or I- (inside of named entity). O (outside of named entity) tags are used to mark tokens that are not a named entity.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
            "num_classes": 7,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC"
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



## de-onb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:euronews/de-onb')
```

*   **Description**:

```
The corpora comprise of files per data provider that are encoded in the IOB format (Ramshaw & Marcus, 1995). The IOB format is a simple text chunking format that divides texts into single tokens per line, and, separated by a whitespace, tags to mark named entities. The most commonly used categories for tags are PER (person), LOC (location) and ORG (organization). To mark named entities that span multiple tokens, the tags have a prefix of either B- (beginning of named entity) or I- (inside of named entity). O (outside of named entity) tags are used to mark tokens that are not a named entity.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
            "num_classes": 7,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC"
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



## de-lft


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:euronews/de-lft')
```

*   **Description**:

```
The corpora comprise of files per data provider that are encoded in the IOB format (Ramshaw & Marcus, 1995). The IOB format is a simple text chunking format that divides texts into single tokens per line, and, separated by a whitespace, tags to mark named entities. The most commonly used categories for tags are PER (person), LOC (location) and ORG (organization). To mark named entities that span multiple tokens, the tags have a prefix of either B- (beginning of named entity) or I- (inside of named entity). O (outside of named entity) tags are used to mark tokens that are not a named entity.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
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
            "num_classes": 7,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC"
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


