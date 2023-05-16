# bswac

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bswac)
*   [Huggingface](https://huggingface.co/datasets/bswac)


## bswac


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bswac/bswac')
```

*   **Description**:

```
The Bosnian web corpus bsWaC was built by crawling the .ba top-level domain in 2014. The corpus was near-deduplicated on paragraph level, normalised via diacritic restoration, morphosyntactically annotated and lemmatised. The corpus is shuffled by paragraphs. Each paragraph contains metadata on the URL, domain and language identification (Bosnian vs. Croatian vs. Serbian).

Version 1.0 of this corpus is described in http://www.aclweb.org/anthology/W14-0405. Version 1.1 contains newer and better linguistic annotations.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 354581267

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


