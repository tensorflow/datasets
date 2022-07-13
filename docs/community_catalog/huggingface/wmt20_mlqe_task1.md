# wmt20_mlqe_task1

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wmt20_mlqe_task1)
*   [Huggingface](https://huggingface.co/datasets/wmt20_mlqe_task1)


## en-de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task1/en-de')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 1 uses Wikipedia data for 6 language pairs that includes high-resource
English--German (En-De) and English--Chinese (En-Zh), medium-resource
Romanian--English (Ro-En) and Estonian--English (Et-En), and low-resource
Sinhalese--English (Si-En) and Nepalese--English (Ne-En), as well as a
dataset with a combination of Wikipedia articles and Reddit articles
for Russian-English (En-Ru). The datasets were collected by translating
sentences sampled from source language articles using state-of-the-art NMT
models built using the fairseq toolkit and annotated with Direct Assessment (DA)
scores by professional translators. Each sentence was annotated following the
FLORES setup, which presents a form of DA, where at least three professional
translators rate each sentence from 0-100 according to the perceived translation
quality. DA scores are standardised using the z-score by rater. Participating systems
are required to score sentences according to z-standardised DA scores.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "segid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "de"
        ],
        "id": null,
        "_type": "Translation"
    },
    "scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "z_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "z_mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "model_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nmt_output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_probas": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## en-zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task1/en-zh')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 1 uses Wikipedia data for 6 language pairs that includes high-resource
English--German (En-De) and English--Chinese (En-Zh), medium-resource
Romanian--English (Ro-En) and Estonian--English (Et-En), and low-resource
Sinhalese--English (Si-En) and Nepalese--English (Ne-En), as well as a
dataset with a combination of Wikipedia articles and Reddit articles
for Russian-English (En-Ru). The datasets were collected by translating
sentences sampled from source language articles using state-of-the-art NMT
models built using the fairseq toolkit and annotated with Direct Assessment (DA)
scores by professional translators. Each sentence was annotated following the
FLORES setup, which presents a form of DA, where at least three professional
translators rate each sentence from 0-100 according to the perceived translation
quality. DA scores are standardised using the z-score by rater. Participating systems
are required to score sentences according to z-standardised DA scores.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "segid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "zh"
        ],
        "id": null,
        "_type": "Translation"
    },
    "scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "z_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "z_mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "model_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nmt_output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_probas": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## et-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task1/et-en')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 1 uses Wikipedia data for 6 language pairs that includes high-resource
English--German (En-De) and English--Chinese (En-Zh), medium-resource
Romanian--English (Ro-En) and Estonian--English (Et-En), and low-resource
Sinhalese--English (Si-En) and Nepalese--English (Ne-En), as well as a
dataset with a combination of Wikipedia articles and Reddit articles
for Russian-English (En-Ru). The datasets were collected by translating
sentences sampled from source language articles using state-of-the-art NMT
models built using the fairseq toolkit and annotated with Direct Assessment (DA)
scores by professional translators. Each sentence was annotated following the
FLORES setup, which presents a form of DA, where at least three professional
translators rate each sentence from 0-100 according to the perceived translation
quality. DA scores are standardised using the z-score by rater. Participating systems
are required to score sentences according to z-standardised DA scores.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "segid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "et",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    },
    "scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "z_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "z_mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "model_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nmt_output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_probas": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ne-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task1/ne-en')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 1 uses Wikipedia data for 6 language pairs that includes high-resource
English--German (En-De) and English--Chinese (En-Zh), medium-resource
Romanian--English (Ro-En) and Estonian--English (Et-En), and low-resource
Sinhalese--English (Si-En) and Nepalese--English (Ne-En), as well as a
dataset with a combination of Wikipedia articles and Reddit articles
for Russian-English (En-Ru). The datasets were collected by translating
sentences sampled from source language articles using state-of-the-art NMT
models built using the fairseq toolkit and annotated with Direct Assessment (DA)
scores by professional translators. Each sentence was annotated following the
FLORES setup, which presents a form of DA, where at least three professional
translators rate each sentence from 0-100 according to the perceived translation
quality. DA scores are standardised using the z-score by rater. Participating systems
are required to score sentences according to z-standardised DA scores.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "segid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "ne",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    },
    "scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "z_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "z_mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "model_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nmt_output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_probas": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ro-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task1/ro-en')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 1 uses Wikipedia data for 6 language pairs that includes high-resource
English--German (En-De) and English--Chinese (En-Zh), medium-resource
Romanian--English (Ro-En) and Estonian--English (Et-En), and low-resource
Sinhalese--English (Si-En) and Nepalese--English (Ne-En), as well as a
dataset with a combination of Wikipedia articles and Reddit articles
for Russian-English (En-Ru). The datasets were collected by translating
sentences sampled from source language articles using state-of-the-art NMT
models built using the fairseq toolkit and annotated with Direct Assessment (DA)
scores by professional translators. Each sentence was annotated following the
FLORES setup, which presents a form of DA, where at least three professional
translators rate each sentence from 0-100 according to the perceived translation
quality. DA scores are standardised using the z-score by rater. Participating systems
are required to score sentences according to z-standardised DA scores.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "segid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "ro",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    },
    "scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "z_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "z_mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "model_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nmt_output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_probas": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## si-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task1/si-en')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 1 uses Wikipedia data for 6 language pairs that includes high-resource
English--German (En-De) and English--Chinese (En-Zh), medium-resource
Romanian--English (Ro-En) and Estonian--English (Et-En), and low-resource
Sinhalese--English (Si-En) and Nepalese--English (Ne-En), as well as a
dataset with a combination of Wikipedia articles and Reddit articles
for Russian-English (En-Ru). The datasets were collected by translating
sentences sampled from source language articles using state-of-the-art NMT
models built using the fairseq toolkit and annotated with Direct Assessment (DA)
scores by professional translators. Each sentence was annotated following the
FLORES setup, which presents a form of DA, where at least three professional
translators rate each sentence from 0-100 according to the perceived translation
quality. DA scores are standardised using the z-score by rater. Participating systems
are required to score sentences according to z-standardised DA scores.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "segid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "si",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    },
    "scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "z_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "z_mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "model_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nmt_output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_probas": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ru-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt20_mlqe_task1/ru-en')
```

*   **Description**:

```
This shared task (part of WMT20) will build on its previous editions
to further examine automatic methods for estimating the quality
of neural machine translation output at run-time, without relying
on reference translations. As in previous years, we cover estimation
at various levels. Important elements introduced this year include: a new
task where sentences are annotated with Direct Assessment (DA)
scores instead of labels based on post-editing; a new multilingual
sentence-level dataset mainly from Wikipedia articles, where the
source articles can be retrieved for document-wide context; the
availability of NMT models to explore system-internal information for the task.

Task 1 uses Wikipedia data for 6 language pairs that includes high-resource
English--German (En-De) and English--Chinese (En-Zh), medium-resource
Romanian--English (Ro-En) and Estonian--English (Et-En), and low-resource
Sinhalese--English (Si-En) and Nepalese--English (Ne-En), as well as a
dataset with a combination of Wikipedia articles and Reddit articles
for Russian-English (En-Ru). The datasets were collected by translating
sentences sampled from source language articles using state-of-the-art NMT
models built using the fairseq toolkit and annotated with Direct Assessment (DA)
scores by professional translators. Each sentence was annotated following the
FLORES setup, which presents a form of DA, where at least three professional
translators rate each sentence from 0-100 according to the perceived translation
quality. DA scores are standardised using the z-score by rater. Participating systems
are required to score sentences according to z-standardised DA scores.
```

*   **License**: Unknown
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7000
`'validation'` | 1000

*   **Features**:

```json
{
    "segid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "ru",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    },
    "scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "z_scores": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "z_mean": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "model_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "doc_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "nmt_output": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_probas": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


