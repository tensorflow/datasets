# setimes

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/setimes)
*   [Huggingface](https://huggingface.co/datasets/setimes)


## bg-bs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-bs')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 136009

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "bs"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bg-el


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-el')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 212437

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "el"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bs-el


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bs-el')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 137602

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bs",
            "el"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bg-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-en')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 213160

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bs-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bs-en')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 138387

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bs",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/el-en')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 227168

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "el",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bg-hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-hr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 203465

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "hr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bs-hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bs-hr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 138402

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bs",
            "hr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/el-hr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 205008

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "el",
            "hr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/en-hr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 205910

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "hr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bg-mk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-mk')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 207169

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "mk"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bs-mk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bs-mk')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 132779

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bs",
            "mk"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-mk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/el-mk')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 207262

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "el",
            "mk"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-mk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/en-mk')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 207777

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "mk"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hr-mk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/hr-mk')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 198876

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "hr",
            "mk"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bg-ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-ro')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 210842

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "ro"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bs-ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bs-ro')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 137365

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bs",
            "ro"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/el-ro')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 212359

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "el",
            "ro"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/en-ro')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 213047

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "ro"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hr-ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/hr-ro')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 203777

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "hr",
            "ro"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## mk-ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/mk-ro')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 206168

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "mk",
            "ro"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bg-sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-sq')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 211518

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "sq"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bs-sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bs-sq')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 137953

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bs",
            "sq"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/el-sq')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 226577

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "el",
            "sq"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/en-sq')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 227516

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "sq"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hr-sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/hr-sq')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 205044

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "hr",
            "sq"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## mk-sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/mk-sq')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 206601

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "mk",
            "sq"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## ro-sq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/ro-sq')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 212320

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "ro",
            "sq"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bg-sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-sr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 211172

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "sr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bs-sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bs-sr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 135945

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bs",
            "sr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/el-sr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 224311

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "el",
            "sr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/en-sr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 225169

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "sr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hr-sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/hr-sr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 203989

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "hr",
            "sr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## mk-sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/mk-sr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 207295

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "mk",
            "sr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## ro-sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/ro-sr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 210612

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "ro",
            "sr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## sq-sr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/sq-sr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 224595

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "sq",
            "sr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bg-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bg-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 206071

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bs-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/bs-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 133958

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bs",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/el-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 207029

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "el",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/en-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 207678

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hr-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/hr-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 199260

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "hr",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## mk-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/mk-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 203231

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "mk",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## ro-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/ro-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 206104

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "ro",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## sq-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/sq-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 207107

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "sq",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## sr-tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:setimes/sr-tr')
```

*   **Description**:

```
SETimes – A Parallel Corpus of English and South-East European Languages
The corpus is based on the content published on the SETimes.com news portal. The news portal publishes “news and views from Southeast Europe” in ten languages: Bulgarian, Bosnian, Greek, English, Croatian, Macedonian, Romanian, Albanian and Serbian. This version of the corpus tries to solve the issues present in an older version of the corpus (published inside OPUS, described in the LREC 2010 paper by Francis M. Tyers and Murat Serdar Alperen). The following procedures were applied to resolve existing issues:

- stricter extraction process – no HTML residues present
- language identification on every non-English document – non-English online documents contain English material in case the article was not translated into that language
- resolving encoding issues in Croatian and Serbian – diacritics were partially lost due to encoding errors – text was rediacritized.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 205993

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "sr",
            "tr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


