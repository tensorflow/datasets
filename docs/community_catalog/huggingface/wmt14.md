# wmt14

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wmt14)
*   [Huggingface](https://huggingface.co/datasets/wmt14)


## cs-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt14/cs-en')
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
`'train'` | 953621
`'validation'` | 3000

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "cs",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt14/de-en')
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
`'train'` | 4508785
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



## fr-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt14/fr-en')
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
`'train'` | 40836715
`'validation'` | 3000

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "fr",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## hi-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt14/hi-en')
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
`'test'` | 2507
`'train'` | 32863
`'validation'` | 520

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "hi",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## ru-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt14/ru-en')
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
`'train'` | 1486965
`'validation'` | 3000

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "ru",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


