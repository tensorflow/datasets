# s2orc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/s2orc)
*   [Huggingface](https://huggingface.co/datasets/s2orc)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:s2orc')
```

*   **Description**:

```
A large corpus of 81.1M English-language academic papers spanning many academic disciplines.
Rich metadata, paper abstracts, resolved bibliographic references, as well as structured full
text for 8.1M open access papers. Full text annotated with automatically-detected inline mentions of
citations, figures, and tables, each linked to their corresponding paper objects. Aggregated papers
from hundreds of academic publishers and digital archives into a unified source, and create the largest
publicly-available collection of machine-readable academic text to date.
```

*   **License**: Semantic Scholar Open Research Corpus is licensed under ODC-BY.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 189674763

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
    "paperAbstract": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entities": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "s2Url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pdfUrls": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "s2PdfUrl": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "authors": [
        {
            "name": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "ids": {
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
    ],
    "inCitations": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "outCitations": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "fieldsOfStudy": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "year": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "venue": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "journalName": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "journalVolume": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "journalPages": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sources": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "doi": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "doiUrl": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pmid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "magId": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


