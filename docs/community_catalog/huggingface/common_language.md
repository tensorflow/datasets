# common_language

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/common_language)
*   [Huggingface](https://huggingface.co/datasets/common_language)


## full


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:common_language/full')
```

*   **Description**:

```
This dataset is composed of speech recordings from languages that were carefully selected from the CommonVoice database.
The total duration of audio recordings is 45.1 hours (i.e., 1 hour of material for each language).
The dataset has been extracted from CommonVoice to train language-id systems.
```

*   **License**: https://creativecommons.org/licenses/by/4.0/legalcode
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5963
`'train'` | 22194
`'validation'` | 5888

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "path": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "age": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gender": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "num_classes": 45,
        "names": [
            "Arabic",
            "Basque",
            "Breton",
            "Catalan",
            "Chinese_China",
            "Chinese_Hongkong",
            "Chinese_Taiwan",
            "Chuvash",
            "Czech",
            "Dhivehi",
            "Dutch",
            "English",
            "Esperanto",
            "Estonian",
            "French",
            "Frisian",
            "Georgian",
            "German",
            "Greek",
            "Hakha_Chin",
            "Indonesian",
            "Interlingua",
            "Italian",
            "Japanese",
            "Kabyle",
            "Kinyarwanda",
            "Kyrgyz",
            "Latvian",
            "Maltese",
            "Mangolian",
            "Persian",
            "Polish",
            "Portuguese",
            "Romanian",
            "Romansh_Sursilvan",
            "Russian",
            "Sakha",
            "Slovenian",
            "Spanish",
            "Swedish",
            "Tamil",
            "Tatar",
            "Turkish",
            "Ukranian",
            "Welsh"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


