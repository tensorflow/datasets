# wmt_t2t

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wmt_t2t)
*   [Huggingface](https://huggingface.co/datasets/wmt_t2t)


## de-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt_t2t/de-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3003
`'train'` | 4592289
`'validation'` | 3000

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "de",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


