# ted_multi

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ted_multi)
*   [Huggingface](https://huggingface.co/datasets/ted_multi)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ted_multi/plain_text')
```

*   **Description**:

```
Massively multilingual (60 language) data set derived from TED Talk transcripts.
Each record consists of parallel arrays of language and text. Missing and
incomplete translations will be filtered out.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7213
`'train'` | 258098
`'validation'` | 6049

*   **Features**:

```json
{
    "translations": {
        "languages": [
            "ar",
            "az",
            "be",
            "bg",
            "bn",
            "bs",
            "calv",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "eo",
            "es",
            "et",
            "eu",
            "fa",
            "fi",
            "fr",
            "fr-ca",
            "gl",
            "he",
            "hi",
            "hr",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ka",
            "kk",
            "ko",
            "ku",
            "lt",
            "mk",
            "mn",
            "mr",
            "ms",
            "my",
            "nb",
            "nl",
            "pl",
            "pt",
            "pt-br",
            "ro",
            "ru",
            "sk",
            "sl",
            "sq",
            "sr",
            "sv",
            "ta",
            "th",
            "tr",
            "uk",
            "ur",
            "vi",
            "zh",
            "zh-cn",
            "zh-tw"
        ],
        "num_languages": 60,
        "id": null,
        "_type": "TranslationVariableLanguages"
    },
    "talk_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


