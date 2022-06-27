# tlc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tlc)
*   [Huggingface](https://huggingface.co/datasets/tlc)


## tlcv1.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tlc/tlcv1.0')
```

*   **Description**:

```
Thai Literature Corpora (TLC): Corpora of machine-ingestible Thai classical literature texts.

Release: 6/25/19

It consists of two datasets:

## TLC set
It is texts from [Vajirayana Digital Library](https://vajirayana.org/), stored by chapters and stanzas (non-tokenized).

tlc v.2.0 (6/17/19 : a total of 34 documents, 292,270 lines, 31,790,734 characters)
tlc v.1.0 (6/11/19 : a total of 25 documents, 113,981 lines, 28,775,761 characters)

## TNHC set
It is texts from Thai National Historical Corpus, stored by lines (manually tokenized).

tnhc v.1.0 (6/25/19 : a total of 47 documents, 756,478 lines, 13,361,142 characters)
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
    "ch_num": {
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
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## tlcv2.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tlc/tlcv2.0')
```

*   **Description**:

```
Thai Literature Corpora (TLC): Corpora of machine-ingestible Thai classical literature texts.

Release: 6/25/19

It consists of two datasets:

## TLC set
It is texts from [Vajirayana Digital Library](https://vajirayana.org/), stored by chapters and stanzas (non-tokenized).

tlc v.2.0 (6/17/19 : a total of 34 documents, 292,270 lines, 31,790,734 characters)
tlc v.1.0 (6/11/19 : a total of 25 documents, 113,981 lines, 28,775,761 characters)

## TNHC set
It is texts from Thai National Historical Corpus, stored by lines (manually tokenized).

tnhc v.1.0 (6/25/19 : a total of 47 documents, 756,478 lines, 13,361,142 characters)
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1

*   **Features**:

```json
{
    "ch_num": {
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
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## tnhcv1.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tlc/tnhcv1.0')
```

*   **Description**:

```
Thai Literature Corpora (TLC): Corpora of machine-ingestible Thai classical literature texts.

Release: 6/25/19

It consists of two datasets:

## TLC set
It is texts from [Vajirayana Digital Library](https://vajirayana.org/), stored by chapters and stanzas (non-tokenized).

tlc v.2.0 (6/17/19 : a total of 34 documents, 292,270 lines, 31,790,734 characters)
tlc v.1.0 (6/11/19 : a total of 25 documents, 113,981 lines, 28,775,761 characters)

## TNHC set
It is texts from Thai National Historical Corpus, stored by lines (manually tokenized).

tnhc v.1.0 (6/25/19 : a total of 47 documents, 756,478 lines, 13,361,142 characters)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 152

*   **Features**:

```json
{
    "text": {
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


