# wiki_lingua

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_lingua)
*   [Huggingface](https://huggingface.co/datasets/wiki_lingua)


## arabic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/arabic')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 9995

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## chinese


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/chinese')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6541

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## czech


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/czech')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2520

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## dutch


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/dutch')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10862

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## english


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/english')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 57945

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## french


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/french')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 21690

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## german


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/german')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 20103

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hindi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/hindi')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3402

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## indonesian


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/indonesian')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 16308

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## italian


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/italian')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 17673

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## japanese


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/japanese')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4372

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## korean


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/korean')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4111

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## portuguese


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/portuguese')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 28143

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## russian


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/russian')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 18143

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## spanish


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/spanish')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 38795

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## thai


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/thai')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5093

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## turkish


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/turkish')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1512

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## vietnamese


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_lingua/vietnamese')
```

*   **Description**:

```
WikiLingua is a large-scale multilingual dataset for the evaluation of
crosslingual abstractive summarization systems. The dataset includes ~770k
article and summary pairs in 18 languages from WikiHow. The gold-standard
article-summary alignments across languages was done by aligning the images
that are used to describe each how-to step in an article.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 1.1.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6616

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "article": {
        "feature": {
            "section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "document": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "summary": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "english_section_name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


