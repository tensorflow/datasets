# wiki_atomic_edits

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_atomic_edits)
*   [Huggingface](https://huggingface.co/datasets/wiki_atomic_edits)


## german_insertions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/german_insertions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3343403

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## german_deletions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/german_deletions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1994329

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## english_insertions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/english_insertions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 13737796

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## english_deletions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/english_deletions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 9352389

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## spanish_insertions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/spanish_insertions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1380934

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## spanish_deletions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/spanish_deletions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 908276

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## french_insertions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/french_insertions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2038305

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## french_deletions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/french_deletions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2060242

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## italian_insertions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/italian_insertions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1078814

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## italian_deletions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/italian_deletions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 583316

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## japanese_insertions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/japanese_insertions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2249527

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## japanese_deletions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/japanese_deletions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1352162

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## russian_insertions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/russian_insertions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1471638

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## russian_deletions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/russian_deletions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 960976

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## chinese_insertions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/chinese_insertions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 746509

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## chinese_deletions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_atomic_edits/chinese_deletions')
```

*   **Description**:

```
A dataset of atomic wikipedia edits containing insertions and deletions of a contiguous chunk of text in a sentence. This dataset contains ~43 million edits across 8 languages.

An atomic edit is defined as an edit e applied to a natural language expression S as the insertion, deletion, or substitution of a sub-expression P such that both the original expression S and the resulting expression e(S) are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 467271

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "base_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "phrase": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edited_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


