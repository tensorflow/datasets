# open_subtitles

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/open_subtitles)
*   [Huggingface](https://huggingface.co/datasets/open_subtitles)


## bs-eo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:open_subtitles/bs-eo')
```

*   **Description**:

```
This is a new collection of translated movie subtitles from http://www.opensubtitles.org/.

IMPORTANT: If you use the OpenSubtitle corpus: Please, add a link to http://www.opensubtitles.org/ to your website and to your reports and publications produced with the data!

This is a slightly cleaner version of the subtitle collection using improved sentence alignment and better language checking.

62 languages, 1,782 bitexts
total number of files: 3,735,070
total number of tokens: 22.10G
total number of sentence fragments: 3.35G
```

*   **License**: No known license
*   **Version**: 2018.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10989

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "year": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "imdbId": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "subtitleId": {
            "bs": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            },
            "eo": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            }
        },
        "sentenceIds": {
            "bs": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "eo": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        }
    },
    "translation": {
        "languages": [
            "bs",
            "eo"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-hy


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:open_subtitles/fr-hy')
```

*   **Description**:

```
This is a new collection of translated movie subtitles from http://www.opensubtitles.org/.

IMPORTANT: If you use the OpenSubtitle corpus: Please, add a link to http://www.opensubtitles.org/ to your website and to your reports and publications produced with the data!

This is a slightly cleaner version of the subtitle collection using improved sentence alignment and better language checking.

62 languages, 1,782 bitexts
total number of files: 3,735,070
total number of tokens: 22.10G
total number of sentence fragments: 3.35G
```

*   **License**: No known license
*   **Version**: 2018.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 668

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "year": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "imdbId": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "subtitleId": {
            "fr": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            },
            "hy": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            }
        },
        "sentenceIds": {
            "fr": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "hy": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        }
    },
    "translation": {
        "languages": [
            "fr",
            "hy"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## da-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:open_subtitles/da-ru')
```

*   **Description**:

```
This is a new collection of translated movie subtitles from http://www.opensubtitles.org/.

IMPORTANT: If you use the OpenSubtitle corpus: Please, add a link to http://www.opensubtitles.org/ to your website and to your reports and publications produced with the data!

This is a slightly cleaner version of the subtitle collection using improved sentence alignment and better language checking.

62 languages, 1,782 bitexts
total number of files: 3,735,070
total number of tokens: 22.10G
total number of sentence fragments: 3.35G
```

*   **License**: No known license
*   **Version**: 2018.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 7543012

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "year": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "imdbId": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "subtitleId": {
            "da": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            },
            "ru": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            }
        },
        "sentenceIds": {
            "da": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "ru": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        }
    },
    "translation": {
        "languages": [
            "da",
            "ru"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:open_subtitles/en-hi')
```

*   **Description**:

```
This is a new collection of translated movie subtitles from http://www.opensubtitles.org/.

IMPORTANT: If you use the OpenSubtitle corpus: Please, add a link to http://www.opensubtitles.org/ to your website and to your reports and publications produced with the data!

This is a slightly cleaner version of the subtitle collection using improved sentence alignment and better language checking.

62 languages, 1,782 bitexts
total number of files: 3,735,070
total number of tokens: 22.10G
total number of sentence fragments: 3.35G
```

*   **License**: No known license
*   **Version**: 2018.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 93016

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "year": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "imdbId": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "subtitleId": {
            "en": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            },
            "hi": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            }
        },
        "sentenceIds": {
            "en": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "hi": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        }
    },
    "translation": {
        "languages": [
            "en",
            "hi"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## bn-is


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:open_subtitles/bn-is')
```

*   **Description**:

```
This is a new collection of translated movie subtitles from http://www.opensubtitles.org/.

IMPORTANT: If you use the OpenSubtitle corpus: Please, add a link to http://www.opensubtitles.org/ to your website and to your reports and publications produced with the data!

This is a slightly cleaner version of the subtitle collection using improved sentence alignment and better language checking.

62 languages, 1,782 bitexts
total number of files: 3,735,070
total number of tokens: 22.10G
total number of sentence fragments: 3.35G
```

*   **License**: No known license
*   **Version**: 2018.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 38272

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "meta": {
        "year": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "imdbId": {
            "dtype": "uint32",
            "id": null,
            "_type": "Value"
        },
        "subtitleId": {
            "bn": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            },
            "is": {
                "dtype": "uint32",
                "id": null,
                "_type": "Value"
            }
        },
        "sentenceIds": {
            "bn": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "is": {
                "feature": {
                    "dtype": "uint32",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        }
    },
    "translation": {
        "languages": [
            "bn",
            "is"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


