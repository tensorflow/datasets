# scb_mt_enth_2020

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/scb_mt_enth_2020)
*   [Huggingface](https://huggingface.co/datasets/scb_mt_enth_2020)


## enth


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scb_mt_enth_2020/enth')
```

*   **Description**:

```
scb-mt-en-th-2020: A Large English-Thai Parallel Corpus
The primary objective of our work is to build a large-scale English-Thai dataset for machine translation.
We construct an English-Thai machine translation dataset with over 1 million segment pairs, curated from various sources,
namely news, Wikipedia articles, SMS messages, task-based dialogs, web-crawled data and government documents.
Methodology for gathering data, building parallel texts and removing noisy sentence pairs are presented in a reproducible manner.
We train machine translation models based on this dataset. Our models' performance are comparable to that of
Google Translation API (as of May 2020) for Thai-English and outperform Google when the Open Parallel Corpus (OPUS) is
included in the training data for both Thai-English and English-Thai translation.
The dataset, pre-trained models, and source code to reproduce our work are available for public use.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 100177
`'train'` | 801402
`'validation'` | 100173

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "th"
        ],
        "id": null,
        "_type": "Translation"
    },
    "subdataset": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## then


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:scb_mt_enth_2020/then')
```

*   **Description**:

```
scb-mt-en-th-2020: A Large English-Thai Parallel Corpus
The primary objective of our work is to build a large-scale English-Thai dataset for machine translation.
We construct an English-Thai machine translation dataset with over 1 million segment pairs, curated from various sources,
namely news, Wikipedia articles, SMS messages, task-based dialogs, web-crawled data and government documents.
Methodology for gathering data, building parallel texts and removing noisy sentence pairs are presented in a reproducible manner.
We train machine translation models based on this dataset. Our models' performance are comparable to that of
Google Translation API (as of May 2020) for Thai-English and outperform Google when the Open Parallel Corpus (OPUS) is
included in the training data for both Thai-English and English-Thai translation.
The dataset, pre-trained models, and source code to reproduce our work are available for public use.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 100177
`'train'` | 801402
`'validation'` | 100173

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "th",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    },
    "subdataset": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


