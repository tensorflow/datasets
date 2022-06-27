# wmt15

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wmt15)
*   [Huggingface](https://huggingface.co/datasets/wmt15)


## cs-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt15/cs-en')
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
`'test'` | 2656
`'train'` | 959768
`'validation'` | 3003

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
ds = tfds.load('huggingface:wmt15/de-en')
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
`'test'` | 2169
`'train'` | 4522998
`'validation'` | 3003

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



## fi-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt15/fi-en')
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
`'test'` | 1370
`'train'` | 2073394
`'validation'` | 1500

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "fi",
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
ds = tfds.load('huggingface:wmt15/fr-en')
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
`'test'` | 1500
`'train'` | 40853137
`'validation'` | 4503

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



## ru-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt15/ru-en')
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
`'test'` | 2818
`'train'` | 1495081
`'validation'` | 3003

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


