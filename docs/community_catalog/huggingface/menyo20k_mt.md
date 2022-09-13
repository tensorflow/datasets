# menyo20k_mt

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/menyo20k_mt)
*   [Huggingface](https://huggingface.co/datasets/menyo20k_mt)


## menyo20k_mt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:menyo20k_mt/menyo20k_mt')
```

*   **Description**:

```
MENYO-20k is a multi-domain parallel dataset with texts obtained from news articles, ted talks, movie transcripts, radio transcripts, science and technology texts, and other short articles curated from the web and professional translators. The dataset has 20,100 parallel sentences split into 10,070 training sentences, 3,397 development sentences, and 6,633 test sentences (3,419 multi-domain, 1,714 news domain, and 1,500 ted talks speech transcript domain). The development and test sets are available upon request.
```

*   **License**: For non-commercial use because some of the data sources like Ted talks and JW news requires permission for commercial use.
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 10070

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "yo"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


