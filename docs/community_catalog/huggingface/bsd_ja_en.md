# bsd_ja_en

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bsd_ja_en)
*   [Huggingface](https://huggingface.co/datasets/bsd_ja_en)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bsd_ja_en')
```

*   **Description**:

```
This is the Business Scene Dialogue (BSD) dataset,
a Japanese-English parallel corpus containing written conversations
in various business scenarios.

The dataset was constructed in 3 steps:
  1) selecting business scenes,
  2) writing monolingual conversation scenarios according to the selected scenes, and
  3) translating the scenarios into the other language.

Half of the monolingual scenarios were written in Japanese
and the other half were written in English.

Fields:
- id: dialogue identifier
- no: sentence pair number within a dialogue
- en_speaker: speaker name in English
- ja_speaker: speaker name in Japanese
- en_sentence: sentence in English
- ja_sentence: sentence in Japanese
- original_language: language in which monolingual scenario was written
- tag: scenario
- title: scenario title
```

*   **License**: CC BY-NC-SA 4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2120
`'train'` | 20000
`'validation'` | 2051

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "no": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "en_speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ja_speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "en_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ja_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


