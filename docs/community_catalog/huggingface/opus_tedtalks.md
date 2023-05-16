# opus_tedtalks

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/opus_tedtalks)
*   [Huggingface](https://huggingface.co/datasets/opus_tedtalks)


## en-hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:opus_tedtalks/en-hr')
```

*   **Description**:

```
This is a Croatian-English parallel corpus of transcribed and translated TED talks, originally extracted from https://wit3.fbk.eu. The corpus is compiled by Željko Agić and is taken from http://lt.ffzg.hr/zagic provided under the CC-BY-NC-SA license.
2 languages, total number of files: 2
total number of tokens: 2.81M
total number of sentence fragments: 0.17M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 86348

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
            "hr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


