# hrwac

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hrwac)
*   [Huggingface](https://huggingface.co/datasets/hrwac)


## hrwac


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hrwac/hrwac')
```

*   **Description**:

```
The Croatian web corpus hrWaC was built by crawling the .hr top-level domain in 2011 and again in 2014. The corpus was near-deduplicated on paragraph level, normalised via diacritic restoration, morphosyntactically annotated and lemmatised. The corpus is shuffled by paragraphs. Each paragraph contains metadata on the URL, domain and language identification (Croatian vs. Serbian).

Version 2.0 of this corpus is described in http://www.aclweb.org/anthology/W14-0405. Version 2.1 contains newer and better linguistic annotations.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1736944727

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


