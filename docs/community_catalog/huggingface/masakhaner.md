# masakhaner

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/masakhaner)
*   [Huggingface](https://huggingface.co/datasets/masakhaner)


## amh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/amh')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 1750
`'validation'` | 250

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## hau


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/hau')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 552
`'train'` | 1912
`'validation'` | 276

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## ibo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/ibo')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 638
`'train'` | 2235
`'validation'` | 320

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## kin


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/kin')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 605
`'train'` | 2116
`'validation'` | 302

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## lug


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/lug')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 407
`'train'` | 1428
`'validation'` | 200

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## luo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/luo')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 186
`'train'` | 644
`'validation'` | 92

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## pcm


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/pcm')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 600
`'train'` | 2124
`'validation'` | 306

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## swa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/swa')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 604
`'train'` | 2109
`'validation'` | 300

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## wol


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/wol')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 539
`'train'` | 1871
`'validation'` | 267

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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



## yor


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:masakhaner/yor')
```

*   **Description**:

```
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 645
`'train'` | 2171
`'validation'` | 305

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
            "num_classes": 9,
            "names": [
                "O",
                "B-PER",
                "I-PER",
                "B-ORG",
                "I-ORG",
                "B-LOC",
                "I-LOC",
                "B-DATE",
                "I-DATE"
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


