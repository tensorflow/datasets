# opus_books

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_books)
*   [Huggingface](https://huggingface.co/datasets/opus_books)


## ca-de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/ca-de')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4445

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
            "ca",
            "de"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## ca-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/ca-en')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4605

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
            "ca",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-en')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 51467

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
            "de",
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
ds = tfds.load('huggingface:opus_books/el-en')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1285

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



## de-eo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-eo')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1363

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
            "de",
            "eo"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-eo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-eo')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1562

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
            "eo"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-es')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 27526

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
            "de",
            "es"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/el-es')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1096

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
            "es"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-es')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 93470

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
            "es"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## eo-es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/eo-es')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1677

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
            "eo",
            "es"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-fi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-fi')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3645

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
            "fi"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## es-fi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/es-fi')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3344

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
            "es",
            "fi"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-fr')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 34916

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
            "de",
            "fr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/el-fr')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1237

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
            "fr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-fr')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 127085

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
            "fr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## eo-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/eo-fr')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1588

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
            "eo",
            "fr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## es-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/es-fr')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 56319

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
            "es",
            "fr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fi-fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fi-fr')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3537

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
            "fi",
            "fr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## ca-hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/ca-hu')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4463

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
            "ca",
            "hu"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-hu')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 51780

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
            "de",
            "hu"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## el-hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/el-hu')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1090

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
            "hu"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-hu')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 137151

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
            "hu"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## eo-hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/eo-hu')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1636

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
            "eo",
            "hu"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fr-hu')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 89337

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
            "fr",
            "hu"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-it')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 27381

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
            "de",
            "it"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-it')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 32332

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
            "it"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## eo-it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/eo-it')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1453

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
            "eo",
            "it"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## es-it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/es-it')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 28868

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
            "es",
            "it"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fr-it')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 14692

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
            "fr",
            "it"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hu-it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/hu-it')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 30949

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
            "hu",
            "it"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## ca-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/ca-nl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4329

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
            "ca",
            "nl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-nl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 15622

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
            "de",
            "nl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-nl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 38652

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
            "nl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## es-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/es-nl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 32247

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
            "es",
            "nl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fr-nl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 40017

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
            "fr",
            "nl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hu-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/hu-nl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 43428

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
            "hu",
            "nl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## it-nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/it-nl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2359

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
            "it",
            "nl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-no


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-no')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3499

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
            "no"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## es-no


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/es-no')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3585

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
            "es",
            "no"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fi-no


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fi-no')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3414

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
            "fi",
            "no"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-no


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fr-no')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3449

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
            "fr",
            "no"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hu-no


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/hu-no')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3410

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
            "hu",
            "no"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-pl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2831

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
            "pl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fi-pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fi-pl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2814

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
            "fi",
            "pl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fr-pl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2825

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
            "fr",
            "pl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hu-pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/hu-pl')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2859

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
            "hu",
            "pl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-pt')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1102

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
            "de",
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-pt')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1404

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
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## eo-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/eo-pt')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1259

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
            "eo",
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## es-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/es-pt')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1327

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
            "es",
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fr-pt')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1263

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
            "fr",
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hu-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/hu-pt')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1184

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
            "hu",
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## it-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/it-pt')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1163

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
            "it",
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/de-ru')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 17373

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
            "de",
            "ru"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-ru')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 17496

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
            "ru"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## es-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/es-ru')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 16793

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
            "es",
            "ru"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fr-ru')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8197

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
            "fr",
            "ru"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hu-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/hu-ru')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 26127

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
            "hu",
            "ru"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## it-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/it-ru')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 17906

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
            "it",
            "ru"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-sv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/en-sv')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3095

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
            "sv"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fr-sv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/fr-sv')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3002

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
            "fr",
            "sv"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## it-sv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_books/it-sv')
```

*   **Description**:

```
This is a collection of copyright free books aligned by Andras Farkas, which are available from http://www.farkastranslations.com/bilingual_books.php
Note that the texts are rather dated due to copyright issues and that some of them are manually reviewed (check the meta-data at the top of the corpus files in XML). The source is multilingually aligned, which is available from http://www.farkastranslations.com/bilingual_books.php. In OPUS, the alignment is formally bilingual but the multilingual alignment can be recovered from the XCES sentence alignment files. Note also that the alignment units from the original source may include multi-sentence paragraphs, which are split and sentence-aligned in OPUS.
All texts are freely available for personal, educational and research use. Commercial use (e.g. reselling as parallel books) and mass redistribution without explicit permission are not granted. Please acknowledge the source when using the data!

16 languages, 64 bitexts
total number of files: 158
total number of tokens: 19.50M
total number of sentence fragments: 0.91M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2998

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
            "it",
            "sv"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


