# wmt17

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wmt17)
*   [Huggingface](https://huggingface.co/datasets/wmt17)


## cs-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt17/cs-en')
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
`'test'` | 3005
`'train'` | 1018291
`'validation'` | 2999

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
ds = tfds.load('huggingface:wmt17/de-en')
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
`'test'` | 3004
`'train'` | 5906184
`'validation'` | 2999

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
ds = tfds.load('huggingface:wmt17/fi-en')
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
`'test'` | 6004
`'train'` | 2656542
`'validation'` | 6000

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



## lv-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt17/lv-en')
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
`'test'` | 2001
`'train'` | 3567528
`'validation'` | 2003

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "lv",
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
ds = tfds.load('huggingface:wmt17/ru-en')
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
`'test'` | 3001
`'train'` | 24782720
`'validation'` | 2998

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



## tr-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt17/tr-en')
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
`'test'` | 3007
`'train'` | 205756
`'validation'` | 3000

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "tr",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## zh-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt17/zh-en')
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
`'test'` | 2001
`'train'` | 25134743
`'validation'` | 2002

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "zh",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


