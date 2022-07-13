# spanish_billion_words

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/spanish_billion_words)
*   [Huggingface](https://huggingface.co/datasets/spanish_billion_words)


## corpus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:spanish_billion_words/corpus')
```

*   **Description**:

```
An unannotated Spanish corpus of nearly 1.5 billion words, compiled from different resources from the web.
This resources include the spanish portions of SenSem, the Ancora Corpus, some OPUS Project Corpora and the Europarl,
the Tibidabo Treebank, the IULA Spanish LSP Treebank, and dumps from the Spanish Wikipedia, Wikisource and Wikibooks.
This corpus is a compilation of 100 text files. Each line of these files represents one of the 50 million sentences from the corpus.
```

*   **License**: https://creativecommons.org/licenses/by-sa/4.0/
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 46925295

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


