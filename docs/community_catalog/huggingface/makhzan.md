# makhzan

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/makhzan)
*   [Huggingface](https://huggingface.co/datasets/makhzan)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:makhzan')
```

*   **Description**:

```
An Urdu text corpus for machine learning, natural language processing and linguistic analysis.
```

*   **License**: All files in the /text directory are covered under standard copyright. Each piece of text has been included in this repository with explicity permission of respective copyright holders, who are identified in the <meta> tag for each file. You are free to use this text for analysis, research and development, but you are not allowed to redistribute or republish this text. Some cases where a less restrictive license could apply to files in the /text directory are presented below. In some cases copyright free text has been digitally reproduced through the hard work of our collaborators. In such cases we have credited the appropriate people where possible in a notes field in the file's metadata, and we strongly encourage you to contact them before redistributing this text in any form. Where a separate license is provided along with the text, we have provided corresponding data in the publication field in a file's metadata.
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5522

*   **Features**:

```json
{
    "file_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "metadata": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "num-words": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "contains-non-urdu-languages": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "document_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


