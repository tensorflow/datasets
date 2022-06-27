# alt

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/alt)
*   [Huggingface](https://huggingface.co/datasets/alt)


## alt-parallel


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:alt/alt-parallel')
```

*   **Description**:

```
The ALT project aims to advance the state-of-the-art Asian natural language processing (NLP) techniques through the open collaboration for developing and using ALT. It was first conducted by NICT and UCSY as described in Ye Kyaw Thu, Win Pa Pa, Masao Utiyama, Andrew Finch and Eiichiro Sumita (2016). Then, it was developed under ASEAN IVO as described in this Web page. The process of building ALT began with sampling about 20,000 sentences from English Wikinews, and then these sentences were translated into the other languages. ALT now has 13 languages: Bengali, English, Filipino, Hindi, Bahasa Indonesia, Japanese, Khmer, Lao, Malay, Myanmar (Burmese), Thai, Vietnamese, Chinese (Simplified Chinese).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1019
`'train'` | 18094
`'validation'` | 1004

*   **Features**:

```json
{
    "SNT.URLID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "SNT.URLID.SNTID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "bg",
            "en",
            "en_tok",
            "fil",
            "hi",
            "id",
            "ja",
            "khm",
            "lo",
            "ms",
            "my",
            "th",
            "vi",
            "zh"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## alt-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:alt/alt-en')
```

*   **Description**:

```
The ALT project aims to advance the state-of-the-art Asian natural language processing (NLP) techniques through the open collaboration for developing and using ALT. It was first conducted by NICT and UCSY as described in Ye Kyaw Thu, Win Pa Pa, Masao Utiyama, Andrew Finch and Eiichiro Sumita (2016). Then, it was developed under ASEAN IVO as described in this Web page. The process of building ALT began with sampling about 20,000 sentences from English Wikinews, and then these sentences were translated into the other languages. ALT now has 13 languages: Bengali, English, Filipino, Hindi, Bahasa Indonesia, Japanese, Khmer, Lao, Malay, Myanmar (Burmese), Thai, Vietnamese, Chinese (Simplified Chinese).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1017
`'train'` | 17889
`'validation'` | 988

*   **Features**:

```json
{
    "SNT.URLID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "SNT.URLID.SNTID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "status": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## alt-jp


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:alt/alt-jp')
```

*   **Description**:

```
The ALT project aims to advance the state-of-the-art Asian natural language processing (NLP) techniques through the open collaboration for developing and using ALT. It was first conducted by NICT and UCSY as described in Ye Kyaw Thu, Win Pa Pa, Masao Utiyama, Andrew Finch and Eiichiro Sumita (2016). Then, it was developed under ASEAN IVO as described in this Web page. The process of building ALT began with sampling about 20,000 sentences from English Wikinews, and then these sentences were translated into the other languages. ALT now has 13 languages: Bengali, English, Filipino, Hindi, Bahasa Indonesia, Japanese, Khmer, Lao, Malay, Myanmar (Burmese), Thai, Vietnamese, Chinese (Simplified Chinese).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 931
`'train'` | 17202
`'validation'` | 953

*   **Features**:

```json
{
    "SNT.URLID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "SNT.URLID.SNTID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "status": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_alignment": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "jp_tokenized": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "en_tokenized": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## alt-my


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:alt/alt-my')
```

*   **Description**:

```
The ALT project aims to advance the state-of-the-art Asian natural language processing (NLP) techniques through the open collaboration for developing and using ALT. It was first conducted by NICT and UCSY as described in Ye Kyaw Thu, Win Pa Pa, Masao Utiyama, Andrew Finch and Eiichiro Sumita (2016). Then, it was developed under ASEAN IVO as described in this Web page. The process of building ALT began with sampling about 20,000 sentences from English Wikinews, and then these sentences were translated into the other languages. ALT now has 13 languages: Bengali, English, Filipino, Hindi, Bahasa Indonesia, Japanese, Khmer, Lao, Malay, Myanmar (Burmese), Thai, Vietnamese, Chinese (Simplified Chinese).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1018
`'train'` | 18088
`'validation'` | 1000

*   **Features**:

```json
{
    "SNT.URLID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "SNT.URLID.SNTID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## alt-km


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:alt/alt-km')
```

*   **Description**:

```
The ALT project aims to advance the state-of-the-art Asian natural language processing (NLP) techniques through the open collaboration for developing and using ALT. It was first conducted by NICT and UCSY as described in Ye Kyaw Thu, Win Pa Pa, Masao Utiyama, Andrew Finch and Eiichiro Sumita (2016). Then, it was developed under ASEAN IVO as described in this Web page. The process of building ALT began with sampling about 20,000 sentences from English Wikinews, and then these sentences were translated into the other languages. ALT now has 13 languages: Bengali, English, Filipino, Hindi, Bahasa Indonesia, Japanese, Khmer, Lao, Malay, Myanmar (Burmese), Thai, Vietnamese, Chinese (Simplified Chinese).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1018
`'train'` | 18088
`'validation'` | 1000

*   **Features**:

```json
{
    "SNT.URLID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "SNT.URLID.SNTID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "km_pos_tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "km_tokenized": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## alt-my-transliteration


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:alt/alt-my-transliteration')
```

*   **Description**:

```
The ALT project aims to advance the state-of-the-art Asian natural language processing (NLP) techniques through the open collaboration for developing and using ALT. It was first conducted by NICT and UCSY as described in Ye Kyaw Thu, Win Pa Pa, Masao Utiyama, Andrew Finch and Eiichiro Sumita (2016). Then, it was developed under ASEAN IVO as described in this Web page. The process of building ALT began with sampling about 20,000 sentences from English Wikinews, and then these sentences were translated into the other languages. ALT now has 13 languages: Bengali, English, Filipino, Hindi, Bahasa Indonesia, Japanese, Khmer, Lao, Malay, Myanmar (Burmese), Thai, Vietnamese, Chinese (Simplified Chinese).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 84022

*   **Features**:

```json
{
    "en": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "my": {
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
```



## alt-my-west-transliteration


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:alt/alt-my-west-transliteration')
```

*   **Description**:

```
The ALT project aims to advance the state-of-the-art Asian natural language processing (NLP) techniques through the open collaboration for developing and using ALT. It was first conducted by NICT and UCSY as described in Ye Kyaw Thu, Win Pa Pa, Masao Utiyama, Andrew Finch and Eiichiro Sumita (2016). Then, it was developed under ASEAN IVO as described in this Web page. The process of building ALT began with sampling about 20,000 sentences from English Wikinews, and then these sentences were translated into the other languages. ALT now has 13 languages: Bengali, English, Filipino, Hindi, Bahasa Indonesia, Japanese, Khmer, Lao, Malay, Myanmar (Burmese), Thai, Vietnamese, Chinese (Simplified Chinese).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 107121

*   **Features**:

```json
{
    "en": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "my": {
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
```


