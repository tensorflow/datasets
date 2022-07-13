# prachathai67k

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/prachathai67k)
*   [Huggingface](https://huggingface.co/datasets/prachathai67k)


## prachathai67k


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:prachathai67k/prachathai67k')
```

*   **Description**:

```
`prachathai-67k`: News Article Corpus and Multi-label Text Classificdation from Prachathai.com
The prachathai-67k dataset was scraped from the news site Prachathai.
We filtered out those articles with less than 500 characters of body text, mostly images and cartoons.
It contains 67,889 articles wtih 12 curated tags from August 24, 2004 to November 15, 2018.
The dataset was originally scraped by @lukkiddd and cleaned by @cstorm125.
You can also see preliminary exploration at https://github.com/PyThaiNLP/prachathai-67k/blob/master/exploration.ipynb
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6789
`'train'` | 54379
`'validation'` | 6721

*   **Features**:

```json
{
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "body_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "politics": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "human_rights": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "quality_of_life": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "international": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "social": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "environment": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "economics": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "culture": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "labor": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "national_security": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "ict": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "education": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


