# spc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/spc)
*   [Huggingface](https://huggingface.co/datasets/spc)


## af-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:spc/af-en')
```

*   **Description**:

```
This is a collection of parallel corpora collected by Hercules Dalianis and his research group for bilingual dictionary construction.
More information in: Hercules Dalianis, Hao-chun Xing, Xin Zhang: Creating a Reusable English-Chinese Parallel Corpus for Bilingual Dictionary Construction, In Proceedings of LREC2010 (source: http://people.dsv.su.se/~hercules/SEC/) and Konstantinos Charitakis (2007): Using Parallel Corpora to Create a Greek-English Dictionary with UPLUG, In Proceedings of NODALIDA 2007. Afrikaans-English: Aldin Draghoender and Mattias Kanhov: Creating a reusable English – Afrikaans parallel corpora for bilingual dictionary construction

4 languages, 3 bitexts
total number of files: 6
total number of tokens: 1.32M
total number of sentence fragments: 0.15M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 57351

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
            "af",
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
ds = tfds.load('huggingface:spc/el-en')
```

*   **Description**:

```
This is a collection of parallel corpora collected by Hercules Dalianis and his research group for bilingual dictionary construction.
More information in: Hercules Dalianis, Hao-chun Xing, Xin Zhang: Creating a Reusable English-Chinese Parallel Corpus for Bilingual Dictionary Construction, In Proceedings of LREC2010 (source: http://people.dsv.su.se/~hercules/SEC/) and Konstantinos Charitakis (2007): Using Parallel Corpora to Create a Greek-English Dictionary with UPLUG, In Proceedings of NODALIDA 2007. Afrikaans-English: Aldin Draghoender and Mattias Kanhov: Creating a reusable English – Afrikaans parallel corpora for bilingual dictionary construction

4 languages, 3 bitexts
total number of files: 6
total number of tokens: 1.32M
total number of sentence fragments: 0.15M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8181

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



## en-zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:spc/en-zh')
```

*   **Description**:

```
This is a collection of parallel corpora collected by Hercules Dalianis and his research group for bilingual dictionary construction.
More information in: Hercules Dalianis, Hao-chun Xing, Xin Zhang: Creating a Reusable English-Chinese Parallel Corpus for Bilingual Dictionary Construction, In Proceedings of LREC2010 (source: http://people.dsv.su.se/~hercules/SEC/) and Konstantinos Charitakis (2007): Using Parallel Corpora to Create a Greek-English Dictionary with UPLUG, In Proceedings of NODALIDA 2007. Afrikaans-English: Aldin Draghoender and Mattias Kanhov: Creating a reusable English – Afrikaans parallel corpora for bilingual dictionary construction

4 languages, 3 bitexts
total number of files: 6
total number of tokens: 1.32M
total number of sentence fragments: 0.15M
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2228

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
            "zh"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


